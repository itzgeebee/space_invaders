from turtle import Turtle


class Wall:
    def __init__(self):
        self.wall_sections = []
        self.create_walls()
        self.move_distance = 10

    def create_walls(self):
        first_wall = []
        x = 430
        y = -150
        for i in range(30):
            coord = (x, y)
            first_wall.append(coord)
            x -= 30
        x = 430
        y = -130
        for i in range(30):
            coord = (x, y)
            first_wall.append(coord)
            x -= 30
        x = 430
        y = -110
        for i in range(30):
            coord = (x, y)
            first_wall.append(coord)
            x -= 30

        for n in first_wall:
            new_wall = Turtle("square")
            new_wall.penup()
            new_wall.shapesize(stretch_wid=0.5, stretch_len=0.5)
            new_wall.goto(n)
            new_wall.color("blue")
            new_wall.speed("slowest")
            self.wall_sections.append(new_wall)
        print(self.wall_sections)
        print(len(self.wall_sections))
