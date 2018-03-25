from tkinter import *
import sys
def printMsg():
    print("Hello, world")
def ExitWindow():
    root.destroy()
    sys.exit()

root = Tk()
myCanvas = Canvas(width=300, height=300)
myCanvas.pack()
labelWidget = Label(myCanvas, text= "controls on Canvas", fg="blue")
myCanvas.create_window(100, 100, window=labelWidget)
button1 = Button(myCanvas, text="Print", command=printMsg)
myCanvas.create_window(100, 140, window=button1)
button2 = Button(myCanvas, text="Exit", command=ExitWindow)
myCanvas.create_window(100, 200, window=button2)
