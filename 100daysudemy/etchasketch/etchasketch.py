# https://docs.python.org/3/library/turtle.html
#
# W - forward
# S - backward
# A - ccw
# D - cw
# C - clear

from turtle import Turtle, Screen

turtle = Turtle()
turtle.speed("fastest")

screen = Screen()

screen.listen()

screen.onkey(lambda: turtle.forward(10), "w")
screen.onkey(lambda: turtle.backward(10), "s")
screen.onkey(lambda: turtle.setheading(turtle.heading() + 10), "a")
screen.onkey(lambda: turtle.setheading(turtle.heading() - 10), "d")
screen.onkey(lambda: turtle.clear(), "c")

screen.exitonclick()
