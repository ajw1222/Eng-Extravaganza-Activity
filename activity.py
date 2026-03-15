# TODO: To run, type "python activity.py" in the terminal

import turtle
turtle.showturtle()


# TODO: Try to draw 1 shape in each quadrant of the canvas' coordinate plane. (4 shapes total)
# Feel free to delete, copy, or edit the sample code below

turtle.penup()
turtle.goto(-200,-200)
turtle.left(90) # Turn turtle to face upwards (toward positive y-axis)
turtle.speed(2) # Increase the number to make turtle draw faster

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