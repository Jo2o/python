from random import randint
from enum import Enum, auto

class Quadrant(Enum):
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()

class BallMover:

    def __init__(self, ball):
        self.ball = ball

    def get_angle_deviation(self, angle):
        return angle + randint(int(-angle/10), int(angle/10))

    def toss(self):
        self.ball.setheading(randint(0, 359))

    def is_leftright_side_collision(self, x, y, table_width_half, table_height_half):
        return abs(abs(x) - abs(table_width_half)) < abs(abs(y) - abs(table_height_half))

    def calculate_new_heading(self, table_width_half, table_height_half):
        current_x = self.ball.xcor()
        current_y = self.ball.ycor()
        current_angle = self.ball.heading()

        quadrant = Quadrant.ONE
        if current_angle >= 90 and current_angle < 180:
            quadrant = Quadrant.TWO
        elif current_angle >= 180 and current_angle < 270:
            quadrant = Quadrant.THREE
        elif current_angle >= 270 and current_angle < 360:
            quadrant = Quadrant.FOUR

        if quadrant == Quadrant.ONE:
            if self.is_leftright_side_collision(current_x, current_y, table_width_half, table_height_half):
                return self.get_angle_deviation(current_angle)
            else:
                return -self.get_angle_deviation(current_angle)
        elif quadrant == Quadrant.TWO:
            if self.is_leftright_side_collision(current_x, current_y, table_width_half, table_height_half):
                return 90 - (self.get_angle_deviation(current_angle) - 90)
            else:
                return (180 - self.get_angle_deviation(current_angle)) + 180
        elif quadrant == Quadrant.THREE:
            if self.is_leftright_side_collision(current_x, current_y, table_width_half, table_height_half):
                return (270 - self.get_angle_deviation(current_angle)) + 270
            else:
                return 180 - self.get_angle_deviation(current_angle - 180)
        elif quadrant == Quadrant.FOUR:
            if self.is_leftright_side_collision(current_x, current_y, table_width_half, table_height_half):
                return 270 - (self.get_angle_deviation(current_angle) - 270)
            else:
                return self.get_angle_deviation(360 - current_angle)
