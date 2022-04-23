from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.score = 000
        self.lives = 4
        self.color("white")
        self.speed("fastest")
        self.update_score()

    def update_score(self):
        """ updates the score board"""
        self.goto(-370, 220)
        self.write(arg=f"score: {self.score}", move=False, align='left', font=('Courier', 40, 'normal'))
        self.goto(70, 220)
        self.write(arg=f"Lives: 00{self.lives}", move=False, align='left', font=('Courier', 40, 'normal'))

    def game_over(self):
        """prints out the final messages when game termination condition is met"""
        self.goto(-150, 0)
        self.write(arg="Game Over", move=False, align='left', font=('Courier', 50, 'normal'))
