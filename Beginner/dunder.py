from turtle import *
from random import *

t = Turtle()

for i in range(10):
    radius = randint(5, 100)
    x = randint(-200 , 200)
    y = randint(-200 , 200)

    t.up()
    t.goto(x ,y)
    t.down()

    t.circle(radius)

done()

