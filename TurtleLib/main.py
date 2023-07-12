import random
from turtle import Turtle, Screen


def MakeASquare():
    for _ in range(4):
        TimTheTurtle.forward(100)
        TimTheTurtle.right(90)


def DrawADottedLine():
    while not screen.canvwidth == int(TimTheTurtle.xcor()):
        TimTheTurtle.pendown()
        TimTheTurtle.forward(25)
        TimTheTurtle.penup()
        TimTheTurtle.forward(25)


def DrawAShape(sides):
    if sides > 9:
        return
    angle = 360 // sides

    for _ in range(sides):
        TimTheTurtle.forward(55)
        TimTheTurtle.right(angle)
    return DrawAShape(sides + 1)


def RandomWalking():
    TimTheTurtle.speed(10)
    while True:
        headings: int = random.choice([0, 90, 180, 270])
        RandomWalk: dict = {'left': TimTheTurtle.left, 'right': TimTheTurtle.right}
        var: str = random.choice(list(RandomWalk.keys()))
        TimTheTurtle.pencolor(random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple']))
        TimTheTurtle.pensize(8)
        TimTheTurtle.forward(25)
        RandomWalk.get(var)(headings)

def MakeASpirograph():
    TimTheTurtle.speed('fastest')
    while not int(TimTheTurtle.heading()) == 350:
        TimTheTurtle.circle(80)
        TimTheTurtle.setheading(TimTheTurtle.heading() + 10)
        print(TimTheTurtle.heading())


TimTheTurtle = Turtle()

MakeASpirograph()
screen = Screen()
screen.exitonclick()
