from turtle import Turtle

class Paddle(Turtle):
    irx = 380
    iry = 0
    ilx = -390
    ily = 0
    x = 0
    y = 0
    paddle_shape = 'square'
    stretchl = 1
    stretchw = 5
    paddle_color = 'white'
    def __init__(self):
        super().__init__()


    def create_paddle(self, position):
        self.shape(self.paddle_shape)
        # turtles start off with default pixel size 20 x 20.
        # to get a paddle of width 20 , the stretch_len is set to 1
        # to get a paddle of length 100 (height), set stretch_wid to 5 (20 * 5 = 100
        # rpaddle.turtlesize(stretch_wid=5, stretch_len=1)
        self.shapesize(stretch_len=self.stretchl, stretch_wid=self.stretchw)
        self.color(self.paddle_color)
        self.penup()
        # print(f"inside create_paddle function. position: {position}")
        if position == 'l':
            x = self.ilx
            y = self.ily
        else:
            x = self.irx
            y = self.iry
        # print(f"inside create_paddle function. position: {position}, [x, y]: {x}, {y}")
        self.goto(x, y)
        self.pendown()

    def move_up(self):
        x = self.xcor()
        y = self.ycor()
        y += 20
        if (y < 245):
            self.penup()
            self.goto(x, y)
            self.pendown()
            # print(f"[x, y]: [{x}, {y}]")
    def move_down(self):
        x = self.xcor()
        y = self.ycor()
        y -= 20
        if (y > -245):
            self.penup()
            self.goto(x, y)
            self.pendown()
            # print(f"[x, y]: [{x}, {y}]")