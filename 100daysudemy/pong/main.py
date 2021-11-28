from turtle import Turtle, Screen
import ball
import paddle
from ballmover import BallMover

TABLE_WIDTH_HALF = 712
TABLE_HEIGHT_HALF = 345
PADDLES_OFFSET = 39

def setup_screen(screen):
    screen.title("PING-PONG   >>> Jo2o <<<")
    screen.colormode(255)
    screen.bgcolor(0, 35, 35)
    screen.setup(width = TABLE_WIDTH_HALF * 2, height = TABLE_HEIGHT_HALF * 2, startx=None, starty=50)

def setup_net():
    net = Turtle()
    net.hideturtle()
    net.speed(5)
    net.color(255, 255, 255)
    net.penup()
    net.setposition(0, 380)
    net.pendown()
    net.goto(0, -380)

def setup_paddles(screen):
    screen.tracer(0)
    screen.register_shape(paddle.PADDLE_IMAGE_LEFT)
    screen.register_shape(paddle.PADDLE_IMAGE_RIGHT)
    paddle_left = paddle.Paddle(paddle.Type.left)
    paddle_left.goto(-TABLE_WIDTH_HALF + PADDLES_OFFSET, 0)
    screen.onkey(paddle_left.move_up, "q")
    screen.onkey(paddle_left.move_down, "a")
    paddle_right = paddle.Paddle(paddle.Type.right)
    paddle_right.goto(TABLE_WIDTH_HALF - PADDLES_OFFSET, 0)
    screen.onkey(paddle_right.move_up, "p")
    screen.onkey(paddle_right.move_down, "l")
    screen.tracer(1)
    return paddle_left, paddle_right

def setup_ball(screen):
    screen.register_shape(ball.BALL_IMAGE)
    return ball.Ball()

def setup_score(left, right):
    screen.tracer(0)
    left_score = Turtle()
    left_score.penup()
    left_score.hideturtle()
    left_score.color(255, 255, 255)
    left_score.goto(150, 280)
    left_score.write(left, font=('Courier New', 30, 'normal'), align='center')
    right_score = Turtle()
    right_score.penup()
    right_score.hideturtle()
    right_score.color(255, 255, 255)
    right_score.goto(-150, 280)
    right_score.write(right, font=('Courier New', 30, 'normal'), align='center')
    screen.tracer(1)
    return left_score, right_score

def set_score(ball):
    if ball.xcor() > 0:
        right_score.clear()
        setup_score("0", "1")
    else:
        left_score.clear()
        setup_score("1", "0")


def is_game_over():
    return (abs(ball.xcor()) > TABLE_WIDTH_HALF)

def should_bounce():
    return (abs(ball.ycor()) >= TABLE_HEIGHT_HALF - 40) \
           or ((-paddle_left.xcor() + ball.xcor() < 20) and (paddle_left.ycor() - ball.ycor() < 110)) \
           or ((paddle_right.xcor() - ball.xcor() < 20) and (paddle_right.ycor() - ball.ycor() < 110))

def ball_move():
    ball.forward(10)
    if not is_game_over():
        screen.ontimer(ball_move, 10)

screen = Screen()
setup_screen(screen)
setup_net()
(left_score, right_score) = setup_score("0", "0")

ball = setup_ball(screen)
(paddle_left, paddle_right) = setup_paddles(screen)

ballmover = BallMover(ball)
ballmover.toss()
ball_move()

screen.listen()

while not is_game_over():
    screen.update()
    if should_bounce():
        ball.setheading(ballmover.calculate_new_heading(TABLE_WIDTH_HALF, TABLE_HEIGHT_HALF))

set_score(ball)

screen.exitonclick()
