from random import randint

class BallMover:

    def __init__(self, ball):
        self.ball = ball

    def get_angle_deviation(self, angle):
        return angle + randint(int(-angle/4), int(angle/4))

    def move(self, ball):
        self.goto(100, 100)

    def toss(self):
        self.ball.setheading(randint(0, 359))
