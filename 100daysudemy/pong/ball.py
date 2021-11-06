from turtle import Turtle

BALL_IMAGE = "imgs/ball-25.gif"

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(BALL_IMAGE)
        self.penup()
        # self.goto(100, 100)



