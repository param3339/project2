
import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create a Turtle object
house = turtle.Turtle()
house.color("red")
house.pensize(3)

# Draw the base of the house
house.penup()
house.goto(-100, -100)
house.pendown()
house.begin_fill()
house.forward(200)
house.left(90)
house.forward(150)
house.left(90)
house.forward(200)
house.left(90)
house.forward(150)
house.end_fill()

# Draw the roof
house.penup()
house.goto(-120, 50)
house.pendown()
house.begin_fill()
house.setheading(45)
house.forward(140)
house.setheading(0)
house.forward(100)
house.setheading(-45)
house.forward(140)
house.end_fill()

# Draw the door
house.penup()
house.goto(10, -100)
house.pendown()
house.color("brown")
house.begin_fill()
house.setheading(90)
house.forward(50)
house.left(90)
house.forward(40)
house.left(90)
house.forward(50)
house.end_fill()

# Draw the window
house.penup()
house.goto(30, 0)
house.pendown()
house.color("yellow")
house.begin_fill()
house.setheading(90)
house.forward(40)
house.left(90)
house.forward(30)
house.left(90)
house.forward(40)
house.end_fill()

# Close the Turtle graphics window on click
screen.exitonclick()
