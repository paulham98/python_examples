from turtle import *
screen = Screen()
name = screen.textinput("Input", "name:")
name

age = screen.numinput("Input", "age:", 20, minval=20, maxval=100)
age