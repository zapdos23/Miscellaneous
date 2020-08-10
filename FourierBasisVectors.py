# Interactive exploration of fourier basis
# We take as input the length of the finite length signal. Then corresponding to it, we find and plot the real and imaginary parts of
# the various fourier basis vectors

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from Tkinter import *



master = Tk()

length = StringVar(master)
indexOfVector = StringVar(master)
Label(master, text="Length of the signal").grid(row=0)
e1 = Entry(master, textvariable=length)
e1.grid(row=0, column = 1)
Label(master, text="Basis Vector").grid(row=1)
e2 = Entry(master, textvariable = indexOfVector)
e2.grid(row=1, column = 1)

def plotme():
    global master, e1, e2, length, indexOfVariable
    fig = Figure(figsize=(7,7))

    x = np.arange(0, int(e1.get()), 1)
    #for i in range(int(e1.get())):
    #    x[i] = 2*np.pi*i*float(e2.get())/float(e1.get())
    #x *= 2*np.pi*float(e2.get())/float(e1.get())
    
    real_part = np.cos(x*2*np.pi*float(e2.get())/float(e1.get()))
    imag_part = -1*np.sin(x*2*np.pi*float(e2.get())/float(e1.get()))
    
    a = fig.add_subplot(211)
    a.stem(x, real_part, '-', bottom = 0,color='blue', use_line_collection=True)

    b = fig.add_subplot(212)
    b.stem(x, imag_part, '-', bottom = 0,color='red', use_line_collection=False)

    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.get_tk_widget().grid(row=3)
    canvas.draw()
    
    #print ("I was clicked")

Button(master, text="Plot", command=plotme).grid(row=2)

mainloop()

