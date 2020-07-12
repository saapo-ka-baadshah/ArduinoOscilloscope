import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
def animate(i):
    graph_data= open("../SerialInterface/data/temp.txt", "r").read()
    lines = graph_data.split('\n')[-50:]
    xs = list()
    ys = list()
    for line in lines:
        if len(line) > 1:
            y, x = line.split(' ')
            xs.append(float(x))
            ys.append(float(y))

    ax1.clear()
    ax1.grid(True)
    ax1.set_ylim(0,8)
    ax1.set_xlim(xs[0], xs[-1])
    ax1.plot(xs, ys)



ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()
