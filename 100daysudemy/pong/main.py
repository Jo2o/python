from turtle import Turtle, Screen
import paddle
import ball

def setup_screen(scr):
    scr.title("PING-PONG   >>> Jo2o <<<")
    scr.colormode(255)
    scr.bgcolor(0, 35, 35)
    scr.setup(width=1424, height=790, startx=None, starty=50)

def setup_net():
    net = Turtle()
    net.hideturtle()
    net.speed(5)
    net.color(255, 255, 255)
    net.penup()
    net.setposition(0, 380)
    net.pendown()
    net.goto(0, -380)

def setup_paddles(scr):
    scr.register_shape(paddle.PADDLE_IMAGE_LEFT)
    scr.register_shape(paddle.PADDLE_IMAGE_RIGHT)
    pl = paddle.Paddle(paddle.Type.left)
    pl.goto(-678, 0)
    pr = paddle.Paddle(paddle.Type.right)
    pr.goto(673, 0)
    return pl, pr

def setup_ball(scr):
    scr.register_shape(ball.BALL_IMAGE)
    return ball.Ball()

def setup_score():
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
    return left_score, right_score


screen = Screen()
setup_screen(screen)
setup_net()

# screen.tracer(0)
setup_score()
# screen.update()

b = setup_ball(screen)
(paddle_left, paddle_right) = setup_paddles(screen)
# screen.onkey(lambda: turtle.forward(10), "w")


screen.listen()
game_over = False
# while not game_over:




screen.exitonclick()
