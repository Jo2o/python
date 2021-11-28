from turtle import Turtle

BALL_IMAGE = "imgs/ball-25.gif"

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle") #self.shape(BALL_IMAGE)
        self.color("white")
        self.penup()
        self.speed(8)
