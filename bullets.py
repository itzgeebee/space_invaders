from turtle import Turtle


class Bullet(Turtle):

    def __init__(self, position):
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


    # def shoot_up(self):
    #     new_y = self.ycor() + self.y_move
    #     self.goto(self.xcor(), new_y)
    #
    # def shoot_down(self):
    #     new_y = self.ycor() - self.y_move
    #     self.goto(self.xcor(), new_y)

    def shoot(self):
        self.showturtle()
        self.setheading(90)
        self.bullet_state = "fire"
        # new_y = self.ycor() + self.y_move
        # self.goto(self.xcor(), new_y)
        # self.fd(300)
        # self.hideturtle()
        # self.backward(300)

    def reset_bullet(self, x, y):
        self.setposition((x, y))
        self.bullet_state = "ready"
        self.hideturtle()




