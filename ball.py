# -----------------------------------------------------------------------------
# create a ball class to implement the ball that shuttles between the paddles
# specs:
# width = 20
# height = 20
# x pos = 0
# y pos = 0
# -----------------------------------------------------------------------------

from constants import RIGHT_WALL, LEFT_WALL, BOTTOM_WALL, TOP_WALL
from turtle import Turtle
from random import randint
import time
class Ball(Turtle):
    ball_shape = 'circle'
    stretchl = 1
    stretchw = 5
    ball_color = 'white'
    def __init__(self):
        origin_tuples = []
        for i in range(0, 1240):
            li = [randint((-1 * i), i), randint((-1 * i), i)]
            origin_tuples.append(li)
        # origin_tuples = [(0, 0), (20, 120), (-40, -40)]
        super().__init__()
        self.shape(self.ball_shape)
        # default widths used (20 x 20)
        self.color(self.ball_color)
        self.penup()
        # print(len(origin_tuples))
        origin = (309, -131) #origin_tuples[randint(0, len(origin_tuples) - 1)]
        # print(f"origin_tuples: {origin_tuples}")
        # print(f"Origin: {origin}")
        self.goto(tuple(origin))
        # self.goto(0, 0)
        self.pendown()

    def check_collision(self, lpx, lpy, rpx, rpy):
        # print(f"lpx: {lpx}, lpy: {lpy}, rpx:{rpx}, rpy:{rpy}")
        l_paddle_xmin = lpx + 1
        l_paddle_xmax = lpx + 0.5
        l_paddle_ymin = lpy - 2.5
        l_paddle_ymax = lpy + 2.5

        r_paddle_xmin = rpx
        r_paddle_xmax = rpx - 0.5
        r_paddle_ymin = rpy - 2.5
        r_paddle_ymax = rpy + 2.5
        # load them into a list for ease of use and to avoide typos
        pc = [l_paddle_xmin, l_paddle_xmax, l_paddle_ymin, l_paddle_ymax, r_paddle_xmin, r_paddle_xmax, r_paddle_ymin,
              r_paddle_ymax]

        # if self.xcor() < -300: # or self.xcor() > 300:
        #      print(f"ball: ({self.xcor()}, {self.ycor()}). paddle: {pc}")
        # if self.xcor() > pc[0] and self.xcor() <= pc[1] and\
        #         self.ycor() >= pc[2] and self.ycor() <= pc[3]:
        #     print(f"ball: ({self.xcor()}, {self.ycor()}(. paddle: pc")
        #     return 5
        if self.xcor() >= RIGHT_WALL[0][0]:
            return 1  # hit the right wall
        if self.xcor() <= LEFT_WALL[0][0]:
            return 2  # hit the left  wall
        if self.ycor() <= BOTTOM_WALL[0][1]:
            return 3  # hit the BOTTOM  wall
        if self.ycor() >= TOP_WALL[0][1]:
            return 4  # hit the TOP  wall
        #  return 5 if ball hits the left paddle
        #  return 6 if ball hits the right paddle
        return 0

    def move(self, a):
        # print(f"angle in move method: {a}")
        time.sleep(0.1)
        # self.penup()
        self.setheading(a)
        x_incre = 0
        y_incre = 0
        # [45, 135, 225, 315]
        if a == 45:
            x_incre = 10
            y_incre = 10
        elif a == 135:
            x_incre = -10
            y_incre = 10
        elif a == 225:
            x_incre = -10
            y_incre = -10
        else:
            x_incre = 10
            y_incre = -10
        x_incre /= 1
        y_incre /= 1
        x = self.xcor() + x_incre
        y = self.ycor() + y_incre
        self.goto(x, y)
        self.pendown()
