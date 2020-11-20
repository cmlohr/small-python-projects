from turtle import Turtle, Screen
import random
import turtle as t
tom = t.Turtle()
tom.shape("circle")
tom.speed("fastest")
t.colormode(255)
tom.width(2)
tom.hideturtle()


def change_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    new_colors = (red, green, blue)
    return new_colors


def spiro(gap):
    for _ in range(int(360 / gap)):
        tom.color(change_color())
        tom.circle(100)
        tom.setheading(tom.heading() + gap)


spiro(5)


screen = Screen()
screen.exitonclick()
