from turtle import *

def star(t , width , size , color):
    t.color(color)
    t.width(width)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(144)
    t.end_fill()

def circle(t , radius , color):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

t = Turtle()
ask = input("Enter shape: ")
while ask != "done":
    if ask == "star":
        width = int(input("Enter width: "))
        col = input("Enter a color: ")
        size = int(input("Enter a size"))
        star(t,width ,size , col )
    elif ask == "circle":
        radius = int(input("Enter a radius"))
        col = input("Enter a color: ") 
        circle(t , radius , col)
    else:
        print("no shape entered")
        ask = input("Enter shape: ")
    break

done()


# # for steps in range(100):
# #     for c in ('blue', 'red', 'green'):
# #         color(c)
# #         forward(steps)
# #         right(30)

# import turtle as t
# from random import random

# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)