from turtle import *
import tkinter as TK
def main():
    root = TK.Tk()
    cv1 = TK.Canvas(root, width=400, height=300)
    cv2 = TK.Canvas(root, width=400, height=300)
    cv1.pack()
    cv2.pack()
    # cv1.pack(side="right")
    # cv2.pack(side="right")
    s1 = TurtleScreen(cv1)
    s1.bgcolor("white")

    s2 = TurtleScreen(cv2)
    s2.colormode(255)
    s2.bgcolor(128, 128, 128)

    t1 = RawTurtle(s1)
    t2 = RawTurtle(s2)
    # t3 = Turtle()

    t2.shape("turtle")
    t2.pencolor("red")
    t2.pensize(5)
    for i in range(4):

        t1.fd(50)
        t1.lt(90)

        t2.fd(50)
        t2.lt(90)
        #root.mainloop()

if __name__ == '__main__':
    main()
    TK.mainloop()
