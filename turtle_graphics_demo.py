#There are different programs, so please use comment
#to perform each program at a time.

import turtle  #allows us to use turtles
wn = turtle.Screen()  #Creates graphic window
alex = turtle.Turtle()

#drawing randomly
alex.forward(150)
alex.left(90)
alex.forward(75)
wn.exitonclick()

#to change color
wn.bgcolor("light green") #changing background color
alex.color("white")  #changing turtle color

#for loop
for _ in range(4):
    alex.forward(150)
    alex.left(90)


#drawing a rectangle using for loop
for _ in range(2):
    alex.forward(150)
    alex.left(90)
    alex.forward(100)
    alex.left(90)
wn.exitonclick()


#for pentagon
alex = turtle.Turtle()
for i in range (5):
    alex.forward(100)
    alex.right(72)


#turtle moving spirally
alex.shape("turtle")
distance = 10
alex.up()
for _ in range(50):
    alex.stamp()
    alex.forward(distance)
    alex.right(24)
    distance = distance + 2
wn.exitonclick()




