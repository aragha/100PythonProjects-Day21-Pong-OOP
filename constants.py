RIGHT_WALL = [(390, -280), (390, 280)]
LEFT_WALL = [(-385, -280), (-385, 280)]
BOTTOM_WALL = [(-390, -280), (390, -280)]
TOP_WALL = [(-390, 280), (390, 280)]
COLLISION_DICT = ["Proceed", "Hit right wall ", "Hit left wall ",
             "Hit bottom wall ", "Hit top wall ", "Hit right paddle", "Hit left paddle"]
DEBUG_HELP = """
RIGHT_WALL = [(390, -240), (390, 240)]
LEFT_WALL = [(-390, -240), (-390, 240)]
BOTTOM_WALL = [(-390, -240), (390, -240)]
TOP_WALL = [(-390, 240), (390, 240)]

(-390,  240)-------------- (390, 240)
|                                   |
|                                   |
|                                   |
(-390, -240)------------- (390, -240)

coll_dict = ["All good", "Hit right wall ", "Hit left wall ", "Hit bottom wall ", "Hit top wall "]

    def check_collision(self):
        if self.xcor() >= RIGHT_WALL[0][0]:
            return 1  # hit the right wall
        if self.xcor() <= LEFT_WALL[0][0]:
            return 2  # hit the left  wall
        if self.ycor() <= BOTTOM_WALL[0][1]:
            return 3  # hit the BOTTOM  wall
        if self.ycor() >= TOP_WALL[0][1]:
            return 4  # hit the TOP  wall
        return 0
"""