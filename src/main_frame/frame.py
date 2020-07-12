from tkinter import *
from tkinter import messagebox
from .SerialInterface.serial_ports import getArduinoDevice
from .SerialInterface.serial_con import connectTo, Dumping
import threading
import matplotlib
from src.memory_man.manager import memoryManager
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import time

fig = Figure(figsize=(13,7), dpi=100)
ax1 = fig.add_subplot(111)

buffer = ""

def animate(i):
    global buffer
    print("DEBUG::animate: Activated")
    graph_data= open(buffer, "r").read()
    main_lines = graph_data.split('\n')
    lines = main_lines[-50:]
    if(len(main_lines) >=50):

        xs = list()
        ys = list()
        for line in lines:
            if len(line) > 1:
                y, x = line.split(' ')
                xs.append(float(x))
                ys.append(float(y))


    else:
        xs = [i for i in range(50)]
        ys = [0 for i in range(50)]

    ax1.clear()
    ax1.grid(True)
    ax1.set_ylim(0,8)
    ax1.set_xlim(xs[0], xs[-1])
    ax1.plot(xs, ys)

class App(threading.Thread):


    def __init__(self, buffer_file):
        global buffer
        self.device_detected = False
        self.device_connected = False
        self.dumping = False
        self.buffer = buffer_file
        buffer = buffer_file
        self.manager = memoryManager(self.buffer)
        self.dumpingObj = Dumping()
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.title("Arduino OSCILLOSCOPE")
        self.root.geometry("1370x840")

        self.text = Label(self.root, text="")
        self.text.grid(column=1, row=1)
        self.connect_button = Button(self.root, text="CONNECT", command=self.establish_serial_communication)
        self.connect_button.grid(column=2, row=1)
        self.update_device_list(self.text)

        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        # self.canvas.get_tk_widget().grid(column=3, row=3)
        self.canvas.get_tk_widget().grid_forget()

        ani = animation.FuncAnimation(fig, animate, 100)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.manager.thread_killed = True
            self.root.destroy()

    def establish_serial_communication(self):
        interface = getArduinoDevice()
        self.ser_obj = connectTo(interface, baud_rate=115200)
        self.device_connected = True
        self.text.configure(text=str(interface.manufacturer)+"  CONNECTED!      ")
        self.dump_button = Button(self.root, text="START", command=self.start_dumping)
        self.dump_button.grid(column=3, row=1)

    def start_dumping(self):
        print("DEBUG:::start_dumping: Activated")
        self.dump_button["state"] = "disable"
        self.dumping = True
        self.close_connection = Button(self.root, text="STOP", command=self.stop_dumping)
        self.close_connection.grid(column=4, row=1)
        self.dumpingObj.dumpTo(self.ser_obj, file_url=self.buffer)
        self.canvas.get_tk_widget().grid(column=1, row=2, rowspan=9, columnspan= 15, sticky="nsew")


    def stop_dumping(self):
        print("DEBUG:::stop_dumping: Activated")
        self.dumping = False
        self.dumpingObj.stopped = True
        self.ser_obj.close()
        self.close_connection.destroy()
        self.dump_button.destroy()
        self.manager.thread_killed = True

    def update_device_list(self, text):
        # Set the arduino device list
        if(not self.device_connected):
            interfaces = getArduinoDevice()
            try:
                default_device = str(interfaces.manufacturer) + "   waiting for connection...       "
                text.configure(text=default_device)
                self.device_detected = True
                self.connect_button["state"] = "normal"
            except Exception as e:
                print("DEBUG:::update_device_list:"+str(e))
                default_device = str("No Device Found")
                text.configure(text=default_device)
                self.device_detected = False
                self.connect_button["state"] = "disable"
            self.root.after(1000, self.update_device_list, text)
        else:
            pass
