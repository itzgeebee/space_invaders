from turtle import Turtle


class Bullet(Turtle):

    def __init__(self, position):
        """projectile objects """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.2, stretch_len=0.5)
        self.penup()
        self.hideturtle()
        self.y_move = 300
        self.game_speed = 0.1
        self.goto(position)
        self.bullet_state = "ready"

    def shoot(self):
        """changes the state of the projectile object"""
        self.showturtle()
        self.setheading(90)
        self.bullet_state = "fire"

    def reset_bullet(self, x, y):
        """moves projectile to a specified position and changes it's state"""
        self.setposition((x, y))
        self.bullet_state = "ready"
        self.hideturtle()
