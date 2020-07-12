import serial
import threading
import time

def connectTo(ser_interface, baud_rate):
    try:
        ser_obj = serial.Serial(str(ser_interface.device), baud_rate)
        ser_obj.flush()
        print("DEBUG::connectTo:"+"connection_established")
        return ser_obj
    except Exception as e:
        print("DEBUG::connectTo:" + str(e))
        return None

class Dumping:
    def __init__(self):
        self.stopped = False

    def dumping_task(self, ser_obj, file_url="/data/temp.txt"):
        file = open(file_url, "+a")
        self.stopped = False
        while (not self.stopped):
            time.sleep(0.1)
            line = str(ser_obj.read_all())[2:-1]
            all_data = line.split('\\r\\n')
            for i in all_data[1:-1]:
                file.write(i+"\r\n")
            # print(all_data)

    def dumpTo(self, ser_obj, file_url="/data/temp.txt"):
        dump_thread = threading.Thread(target= self.dumping_task, args=(ser_obj, file_url,))
        dump_thread.start()


