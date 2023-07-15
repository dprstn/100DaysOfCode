from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.listen()


def clear(n=None):
    turtle.reset()


func: dict = {'w': turtle.forward, 's': turtle.backward, 'a': turtle.left, 'd': turtle.right, 'c': clear}

for n in func.keys():
    screen.onkey(key=str(n), fun=lambda n=n: func.get(n)(20))

screen.exitonclick()
