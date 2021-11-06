from turtle import Turtle, Screen
from random import randint

class Square(Turtle):
  def __init__(self, square, x, y, next):
    self.square = square
    self.next = next


food = Turtle("circle")
food.color("green")
food.setx(randint(-300, 300))
food.sety(randint(-300, 300))


turtle1 = Turtle("square")
turtle2 = Turtle("square")
turtle3 = Turtle("square")

square3 = Square(turtle1, None)
square2 = Square(turtle1, square3)
square1 = Square(turtle1, square2)








screen = Screen()


screen.onkey(lambda: turtle1.forward(100), "Up")
screen.onkey(lambda: turtle1.setheading(turtle1.heading() + 90), "Left")
screen.onkey(lambda: turtle1.setheading(turtle1.heading() - 90), "Right")



screen.listen()
screen.exitonclick()
