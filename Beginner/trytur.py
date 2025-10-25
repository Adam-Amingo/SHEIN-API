from turtle import *
from random import randint




# colors = ['red' , 'blue' , 'green' ,'yellow' , 'brown']
# for i in range(4):
#     ###position
#     x = randint(-200 , 200)
#     y = randint(-200 , 200)

#     ##color
#     r = randint(0,255)
#     g = randint(0,255)
#     b = randint(0,255)
#     color = (r/255, g/255, b/255)
    
#     ##liftPosition
#     t.up()
#     t.goto(x, y)
#     t.down()

#     t.color(color)
#     t.begin_fill()

#     size = randint(100 , 200)
#     for i in range(4):
#         t.fd(size)
#         t.lt(90)
#     t.end_fill()

# done()

##############################################
##########################################


# def square(t , size , color):
#     t.color(color)
#     t.begin_fill()
#     for i in range(4):
#         t.fd(size)
#         t.lt(90)
#     t.end_fill()


# def circle(t , radius , color):
#     t.color(color)
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()

# def pentagon(t , color , size):
#     t.color(color)
#     t.begin_fill()
#     for i in range(5):
#         t.fd(size)
#         t.lt(72)
#     t.end_fill()



# start = input("square/circle/pentagon ").lower()

# while start != "stop":
#     if start == 'square':
#         size = int(input("Enter size: "))
#         color = input("Enter color: ")
#         square(t , size , color)
#     elif start == 'circle':
#         color = input("Enter color: ")
#         radius = int(input("Enter the radius"))
#         circle(t , radius , color)
#     elif start == 'pentagon':
#         size = int(input("Enter size: "))
#         color = input("Enter color: ")
#         pentagon(t , color , size)
#     else:
#         print("Error shape not found")
    
#     start = input("square/circle/pentagon ").lower()
    
    


# done()

########################################
#######################################

# for i in range(10):
#     radius = randint(5 , 100)
#     x = randint(-200 , 200)
#     y = randint(-200 , 200)

#     t.up()
#     t.goto(x, y)
#     t.down()

#     t.circle(radius)

# done()

#######################################
############################


t1 = Turtle()
t2 =Turtle()
t3 = Turtle()
t4 = Turtle()

def triangle (t , color ):
    t.color(color)
    t.begin_fill()
    for i in range(3):
        t.fd(100)
        t.lt(120)
    t.end_fill()

turtle = [t1 , t2 , t3 , t4]
y = 100
for t in turtle:
    t.up()
    t.goto(0, y)
    t.down()
    y -= 100

triangle(t1, 'red')
triangle(t2, 'yellow')
triangle(t3, 'green')
triangle(t4, 'blue')

done()


