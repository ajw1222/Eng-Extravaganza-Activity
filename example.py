# Draw a snowman example
# TODO: To run, type "python example.py" in the terminal

import turtle
turtle.showturtle()
turtle.speed(15)

# Move into starting position
turtle.penup()
turtle.right(90)
turtle.forward(175)
turtle.left(90)


# Draw the 3 circles of the snowman's body
turtle.fillcolor("white")
turtle.pencolor("black")
turtle.pendown()
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(140)
turtle.right(90)
turtle.pendown()
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.pendown()
turtle.begin_fill()
turtle.circle(45)
turtle.end_fill()


# Create the snowman's buttons
turtle.fillcolor("orange")
turtle.pencolor("orange")
turtle.penup()
turtle.goto(0, -20)
turtle.pendown()
turtle.begin_fill()
turtle.circle(11)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 12)
turtle.pendown()
turtle.begin_fill()
turtle.circle(9)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 42)
turtle.pendown()
turtle.begin_fill()
turtle.circle(7)
turtle.end_fill()


# Draw the snowman's eyes
turtle.fillcolor("black")
turtle.pencolor("black")
turtle.penup()
turtle.goto(0, 105)
turtle.forward(20)
turtle.pendown()
turtle.begin_fill()
turtle.circle(9)
turtle.end_fill()

turtle.penup()
turtle.goto(-20, 105)
turtle.pendown()
turtle.begin_fill()
turtle.circle(9)
turtle.end_fill()


# Draw the snowman's hat
turtle.speed(10)
turtle.penup()
turtle.fillcolor("blue")
turtle.pencolor("orange")
turtle.pensize(2)
turtle.goto(0, 135)
turtle.pendown()
turtle.begin_fill()
turtle.forward(60)
turtle.left(90)
turtle.forward(20)
turtle.left(60)
turtle.forward(40)
turtle.right(60)
turtle.forward(40)
turtle.left(90)


# top of hat length
turtle.forward(50)

turtle.left(90)
turtle.forward(40)
turtle.right(60)
turtle.forward(40)
turtle.left(60)
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.end_fill()


# Draw the snowman's arms
# Left arm
turtle.penup()
turtle.fillcolor("brown")
turtle.pencolor("brown")
turtle.pensize(5)
turtle.goto(0, 42)
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.left(50)
turtle.forward(60)


# Left fingers
turtle.left(45)
turtle.forward(10)
turtle.penup()
turtle.back(10)
turtle.right(45)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.back(10)
turtle.right(45)
turtle.pendown()
turtle.forward(10)


# Right arm
turtle.penup()
turtle.goto(0, 42)
turtle.setheading(180)
turtle.forward(50)
turtle.pendown()
turtle.left(60)
turtle.forward(110)


# Right fingers
turtle.right(45)
turtle.forward(10)
turtle.penup()
turtle.back(10)
turtle.left(45)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.back(10)
turtle.left(45)
turtle.pendown()
turtle.forward(10)


# Draw the snowman's mouth
turtle.penup()
turtle.fillcolor("green")
turtle.pencolor("green")
turtle.goto(-25, 90)
turtle.left(70)
turtle.right(30)
turtle.pensize(3)
turtle.pendown()
turtle.circle(40, 80)


turtle.hideturtle()
turtle.done()