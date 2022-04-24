from turtle import Turtle


class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")

        self.penup()
        self.color("white")
        self.position = position
        self.goto(position)
        self.player_state = "stable"

    def move_left(self):
        """moves the paddle in the left direction"""
        new_x = (self.xcor() - 20)
        self.goto(new_x, self.ycor())
        self.player_state = "moving"

    def move_right(self):
        """moves the paddle in the right direction"""
        new_x = (self.xcor() + 20)
        self.goto(new_x, self.ycor())

    def reset_player(self):
        self.goto(self.position)
