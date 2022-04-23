from turtle import Turtle

START_POSITION_1 = [(170, 200), (140, 200), (110, 200), (80, 200), (50, 200), (20, 200), (-10, 200), (-40, 200),
                    (-70, 200), (-100, 200), (-130, 200)]
START_POSITION_2 = [(170, 170), (140, 170), (110, 170), (80, 170), (50, 170), (20, 170), (-10, 170), (-40, 170),
                    (-70, 170), (-100, 170), (-130, 170)]
START_POSITION_3 = [(170, 140), (140, 140), (110, 140), (80, 140), (50, 140), (20, 140), (-10, 140), (-40, 140),
                    (-70, 140), (-100, 140), (-130, 140)]
ALL_POSITIONS = [START_POSITION_1, START_POSITION_2, START_POSITION_3]

class Invaders:

    def __init__(self):

        self.sections = []
        self.create_ship()
        self.move_distance = 10

    def create_ship(self):
        for positions in ALL_POSITIONS:
            for i in positions:
                alien_ship = Turtle()
                alien_ship.penup()
                alien_ship.goto(i)
                alien_ship.color("red")
                alien_ship.speed("slowest")
                self.sections.append(alien_ship)

    def move(self):
        for seg_num in range(len(self.sections)):
            self.sections[seg_num - 1].forward(self.move_distance)

    def reverse(self):
        self.move_distance *= -1

    def move_down(self):
        for seg_num in range(len(self.sections)):
            y = self.sections[seg_num - 1].ycor() - 1
            self.sections[seg_num - 1].sety(y)





