from turtle import Turtle
import enum

PADDLE_IMAGE_LEFT = "imgs/racket-left.gif"
PADDLE_IMAGE_RIGHT = "imgs/racket-right.gif"

class Type(enum.Enum):
    left = "left"
    right = "right"

class Paddle(Turtle):

    def __init__(self, paddle_type):
        super().__init__()
        self.penup()
        self.speed(8)
        if paddle_type == Type.left:
            self.shape(PADDLE_IMAGE_LEFT)
        elif paddle_type == Type.right:
            self.shape(PADDLE_IMAGE_RIGHT)

    def move_up(self):
        self.sety(self.ycor() + 100)

    def move_down(self):
        self.sety(self.ycor() - 100)

