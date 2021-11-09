from turtle import Turtle, Screen
import paddle
import ball

def setup_screen(screen):
    screen.title("PING-PONG   >>> Jo2o <<<")
    screen.colormode(255)
    screen.bgcolor(0, 35, 35)
    screen.setup(width=1424, height=790, startx=None, starty=50)

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
    paddle_left.goto(-678, 0)
    screen.onkey(paddle_left.move_up, "q")
    screen.onkey(paddle_left.move_down, "a")
    paddle_right = paddle.Paddle(paddle.Type.right)
    paddle_right.goto(673, 0)
    screen.onkey(paddle_right.move_up, "p")
    screen.onkey(paddle_right.move_down, "l")
    screen.tracer(1)
    return paddle_left, paddle_right

def setup_ball(screen):
    screen.register_shape(ball.BALL_IMAGE)
    return ball.Ball()

def setup_score(screen):
    screen.tracer(0)
    left_score = Turtle()
    left_score.penup()
    left_score.hideturtle()
    left_score.color(255, 255, 255)
    left_score.goto(150, 345)
    left_score.write("0", font=('Courier New', 30, 'normal'), align='center')
    right_score = Turtle()
    right_score.penup()
    right_score.hideturtle()
    right_score.color(255, 255, 255)
    right_score.goto(-150, 345)
    right_score.write("0", font=('Courier New', 30, 'normal'), align='center')
    screen.tracer(1)
    return left_score, right_score


screen = Screen()
setup_screen(screen)
setup_net()
setup_score(screen)

b = setup_ball(screen)
(paddle_left, paddle_right) = setup_paddles(screen)

screen.listen()
# game_over = False
# while not game_over:
#     pass




screen.exitonclick()
