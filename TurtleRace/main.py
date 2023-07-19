from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()
turtle.hideturtle()
screen.setup(width=1200, height=500)
turtle.penup()
turtle.pencolor('black')
turtle.pensize(5)
turtle.goto(x=200, y=-200)
turtle.setheading(90)
turtle.pendown()
turtle.goto(x=200, y=200)
turtle.penup()
turtle.setx(0)

COLORS = ['green', 'purple', 'red', 'blue', 'orange', 'pink']


def SetUpPos():
    Turtles = []
    for i in range(1, len(COLORS) + 1):
        NewNode = Turtle(shape='turtle')
        NewNode.speed('fastest')
        NewNode.penup()
        NewNode.goto(x=-580, y=-250 + i * 65)
        ChosenColor = random.choice(COLORS)
        NewNode.color(ChosenColor)
        COLORS.remove(ChosenColor)
        Turtles.append(NewNode)
    return Turtles


def PlayGame():
    Turtles = SetUpPos()
    BetOn = screen.textinput(title='TurtleRace', prompt='Placing Your Bets On...')
    GameOver, Pos = False, 0

    if isinstance(BetOn, str) and BetOn.isalpha():
        while not GameOver:
            Turtles[Pos].forward(random.randint(5,35))
            if Turtles[Pos].xcor() > 200:
                GameOver = True
            elif Pos == len(Turtles)-1:
                Pos = 0
            else:
                Pos += 1
        WonColor = Turtles[Pos].fillcolor()
        turtle.pencolor(BetOn)
        turtle.write(f"{'Winner!' if BetOn.lower() == WonColor else 'Loser!'}",
                     font=('Arial', 30, 'normal'), align='center', move=True)
        turtle.pencolor('black')
        turtle.write(f" The Turtle Color Was: ", font=('Arial', 30, 'normal'), move=True)
        turtle.pencolor(WonColor)
        turtle.write(f'{WonColor.title()}', font=('Arial', 30, 'normal'))


PlayGame()
screen.mainloop()
