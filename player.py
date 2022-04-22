import time
from turtle import Turtle


class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=2)
        self.color("white")
        self.position = position
        self.goto(position)

    def move_left(self):
        """moves the paddle in the left direction"""
        new_x = (self.xcor() - 20)
        self.goto(new_x, self.ycor())

    def move_right(self):
        """moves the paddle in the right direction"""
        new_x = (self.xcor() + 20)
        self.goto(new_x, self.ycor())

    def reset_player(self):
        self.goto(self.position)
        time.sleep(2)

    # def new_bullet(self, position):
    #     self.bullet = Turtle()
    #     self.bullet.shape("square")
    #     self.bullet.penup()
    #     self.bullet.shapesize(stretch_wid=0.3, stretch_len=0.7)
    #     self.bullet.color("yellow")
    #     self.bullet.goto(position)
    #
    # def shoot(self):
    #     self.bullet.upwa
    #




