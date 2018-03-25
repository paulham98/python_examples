from tkinter import *
def onKeyDown(event):
    #print onKeyDown(event):
    s = "char: {}, keysym:{}, keycode:{}".format(
               event.char,event.keysym, event.keycode)
    labelWidget[ "text" ] = s
    root.title(event.keysym)

    if event.state & 0x0001:
        cVar1.set(1)
    else:
        cVar1.set(0)

    if event.state & 0x0004:
        cVar2.set(1)
    else:
        cVar2.set(0)

def onKeyUp(event):
    #print("onKeyUp")
    labelWidget[ "text" ] = ""
    cVar1.set(0)
    cVar2.set(0)

if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, bg= "gray40", width=300, height= 200)
    canvas.pack(expand=YES, fill=BOTH)

    labelWidget = Label(canvas, text="", width=30)
    canvas.create_window(150, 100, window=labelWidget)

    cVar1 = IntVar()
    cVar2 = IntVar()
    C1 = Checkbutton(root, text = "shift", variable = cVar1,
                     onvalue = 1, offvalue = 0, height=5, width =20).pack()
    C2 = Checkbutton(root, text = "Ctrl", variable = cVar2,
                     onvalue = 1, offvalue = 0, height=5, width= 20).pack()
    root.bind_all("<KeyPress>", onKeyDown)
    root.bind_all("<KeyRelease>", onKeyUp)
    root.mainloop()