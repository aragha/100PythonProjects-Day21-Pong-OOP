from turtle import Screen
from paddles import Paddle
from ball import Ball
from constants import DEBUG_HELP, COLLISION_DICT
from random import choice
from scoreboard import Scoreboard
# setup the screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.listen()
# remove animation where paddle moves from center to right or left by using the tracer method
screen.tracer(0)

rp = Paddle()
rp.create_paddle('r')
lp = Paddle()
lp.create_paddle('l')
ball = Ball()
scoreboard = Scoreboard()
# figure out how to move it up and down
# we need screen listen to register key strokes


def r_go_up():
    rp.move_up()


def r_go_down():
    rp.move_down()


def l_go_up():
    lp.move_up()


def l_go_down():
    lp.move_down()


def end_game():
    game_is_on = False
    # screen.bye()


screen.listen()
screen.onkey(fun=r_go_up, key="Up")
screen.onkey(fun=r_go_down, key="Down")
screen.onkey(fun=l_go_up, key="w")
screen.onkey(fun=l_go_down, key="s")
screen.onkey(fun=l_go_up, key="W")
screen.onkey(fun=l_go_down, key="S")
screen.onkey(fun=end_game, key="Escape")

coll_dict = COLLISION_DICT
floc = "C:/Users/aras2/Desktop/reports/report.txt"
f = open(floc, 'w')
fstr = DEBUG_HELP + '\n'
f.write(fstr)
fstr = ''
f.close()
f = open(floc, 'a')
game_is_on = True

heading_angles = [45, 135, 225, 315]
# heading = 45
heading = choice(heading_angles)
while game_is_on:
    # call update method to redraw the paddle whose path is being erased by the tracer() method
    screen.update()
    ball.move(heading)
    collision_status = ball.check_collision(lp.xcor(), lp.ycor(), rp.xcor(), rp.ycor())
    # print(f"{collision_status}: {coll_dict[collision_status]} [{ball.xcor()}, {ball.ycor()}]")
    # fstr = '-----------------------------------------------------------------------------------\n'
    # detect collision with rpaddle
    if ball.distance(rp) < 50 and ball.xcor() >  361:
        collision_status = 5
        print(f"{coll_dict[collision_status]} at: {ball.xcor()}, {ball.ycor()}")
    if ball.distance(lp) < 50 and ball.xcor() <  -364:
        collision_status = 6
        print(f"{coll_dict[collision_status]} at: {ball.xcor()}, {ball.ycor()}")
    if collision_status > 0:
        fstr += f"{collision_status}: {coll_dict[collision_status]} [{ball.xcor()}, {ball.ycor()}], angle:{heading}"
        fstr += '\n'
    if collision_status == 1: #right wall
        if ball.heading() == 45:
            hsave = ball.heading()
            ball.setheading(135)
            heading = 135
            # fstr += f"{collision_status}. Curr Heading: {hsave} changed to {ball.heading()}\n"
        elif ball.heading() == 315:
            hsave = ball.heading()
            ball.setheading(225)
            heading = 225
            # fstr += f"{collision_status}. Curr Heading: {hsave} changed to {ball.heading()}\n"
        scoreboard.l_point()
    elif collision_status == 2: #left wall
        if ball.heading() == 135:
            hsave = ball.heading()
            ball.setheading(45)
            heading = 45
            # fstr += f"{collision_status}. Curr Heading: {hsave} changed to {ball.heading()}\n"
        elif ball.heading() == 225:
            hsave = ball.heading()
            ball.setheading(315)
            heading = 315
            # fstr += f"{collision_status}. Curr Heading: {hsave} changed to {ball.heading()}\n"
        scoreboard.r_point()
    elif collision_status == 3: #bottom wall
        if ball.heading() == 225:
            hsave = ball.heading()
            ball.setheading(135)
            heading = 135
            # fstr += f"{collision_status}. Curr Heading: {hsave} changed to {ball.heading()}\n"
        elif ball.heading() == 315:
            hsave = ball.heading()
            ball.setheading(45)
            heading = 45
            # fstr += f"{collision_status}. Curr Heading: {hsave} changed to {ball.heading()}\n"
    elif collision_status == 4: #top wall
        if ball.heading() == 135:
            hsave = ball.heading()
            ball.setheading(225)
            heading = 225
            # fstr += f"{collision_status}. Curr Heading: {hsave} changed to {ball.heading()}\n"
        elif ball.heading() == 45:
            hsave = ball.heading()
            ball.setheading(315)
            heading = 315
            # fstr += f"{collision_status}. Curr Heading: {hsave} changed to {ball.heading()}\n"
    elif collision_status == 5: #ball hit right paddle
        if ball.heading() == 315:
            hsave = ball.heading()
            ball.setheading(225)
            heading = 225
            # fstr += f"{collision_status}. Curr Heading: {hsave} changed to {ball.heading()}\n"
        elif ball.heading() == 45:
            hsave = ball.heading()
            ball.setheading(135)
            heading = 135
            # fstr += f"{collision_status}. Curr Heading: {hsave} changed to {ball.heading()}\n"
    elif collision_status == 6: #ball hit right paddle
        if ball.heading() == 225:
            hsave = ball.heading()
            ball.setheading(315)
            heading = 315
            # fstr += f"{collision_status}. Curr Heading: {hsave} changed to {ball.heading()}\n"
        elif ball.heading() == 135:
            hsave = ball.heading()
            ball.setheading(45)
            heading = 45
            # fstr += f"{collision_status}. Curr Heading: {hsave} changed to {ball.heading()}\n"
    else: #collision_status = 0 - continue
         pass
    ball.move(heading)
    f.write(fstr)
    # print(f"lp coordinates: {lp.xcor()}, {lp.ycor()}")
screen.exitonclick()

f.close()