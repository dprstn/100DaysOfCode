import turtle
import random
from colorgram import extract
from turtle import Turtle, Screen
colors = extract("hirstspotpainting.jpg", 6)
ColorPallet = [(colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b) for i in range(len(colors))]


TimTheTurtle = Turtle()
turtle.colormode(255)
Screen = Screen()
Screen.setup(width=620, height=580)
Screen.screensize(canvwidth=320, canvheight=240, bg='white')
TimTheTurtle.penup()
TimTheTurtle.speed('fastest')
CurrentX = -300.0
CurrentY = -200.0
TimTheTurtle.goto(x=CurrentX, y=CurrentY)
TimTheTurtle.hideturtle()


while not TimTheTurtle.ycor() + 40 == Screen.canvwidth:

    TimTheTurtle.dot(20, random.choice(ColorPallet))
    TimTheTurtle.forward(45)
    TimTheTurtle.penup()

    if TimTheTurtle.xcor() > float(Screen.canvwidth):
        CurrentY += 40
        TimTheTurtle.goto(CurrentX, CurrentY)




Screen.exitonclick()