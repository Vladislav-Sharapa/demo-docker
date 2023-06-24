from tkinter import Tk, Button
from controller import *

root = Tk()
root.title("Application")
root.geometry("250x200")


btn2 = Button(text="Histogram", width=15, command=output_hist)
btn2.pack()

btn3 = Button(text="Bar chart", width=15, command=output_bar)
btn3.pack()

btn4 = Button(text="Pie", width=15, command=output_pie)
btn4.pack()

btn5 = Button(text="Export excel", width=15,command=export_to_excel)
btn5.pack()


def run() -> None: 
    '''Start the event loop''' 
    root.mainloop()

