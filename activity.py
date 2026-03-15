# TODO: To run, type "python activity.py" in the terminal

import turtle
turtle.showturtle()


# TODO: Write your code below (feel free to delete the example code):
turtle.left(90) # Turn turtle to face up
turtle.speed(3)
turtle.color("red")
turtle.pendown()

turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.color("blue")
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.penup()
turtle.forward(100)


# Ends the drawing
turtle.hideturtle()
turtle.done() # Must be the last line of code