import turtle
import random
painter = turtle.Turtle()
turtle.bgcolor("black")

colors = ["blue", "white", "red", "yellow", "green", "orange"]
def matryoshka(length):
    painter.pencolor(colors[random.randint(0,5)])
    painter.forward(length)
    painter.left(60)
    painter.forward(length)
    painter.left(30)
    painter.forward(length)
    painter.left(45)
    painter.forward(length)
    painter.right(30)
    painter.forward(length)
    painter.left(75)
    painter.forward(length)
    painter.left(70)
    painter.forward(length)
    painter.right(25)
    painter.forward(length)
    painter.left(45)
    painter.forward(length)
    painter.left(30)
    painter.forward(length)
    painter.left(60)
    painter.forward(length)
    if length > 2:
        matryoshka(length * 0.9)

turtle.speed(0)
painter.hideturtle()
painter.penup()
painter.goto(0,-300)
painter.showturtle()
painter.pendown()
matryoshka(165)
turtle.done()






