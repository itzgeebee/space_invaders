import random
import time
from turtle import Screen
from player import Player
from bullets import Bullet
from invaders import Invaders

# initialize the screen attributes
screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
position = (0, -250)
bullet_speed = 10
main_char = Player(position)
player_bullet = Bullet((main_char.xcor(), main_char.ycor()))
alien = Invaders()

random_alien = random.choice(alien.sections)
enemy_bullet = Bullet((random_alien.xcor(), random_alien.ycor()))

screen.listen()
screen.onkey(fun=main_char.move_left, key="Left")
screen.onkey(fun=main_char.move_right, key="Right")
screen.onkey(fun=player_bullet.shoot, key="Up")

bounce_count = 0
while True:

    delay = 0.2
    screen.update()
    time.sleep(delay)
    alien.move()
    for i in alien.sections:
        if i.xcor() < -430 or i.xcor() > 420:
            alien.reverse()
            bounce_count += 1
            if bounce_count % 2 == 0:
                alien.move_down()

    for i in alien.sections:
        if i.distance(player_bullet) < 20:
            alien.go_boom(i)
            x = main_char.xcor()
            y = main_char.ycor()
            player_bullet.reset_bullet(x, y)

    if enemy_bullet.distance(main_char) < 40:
        main_char.reset_player()

    if player_bullet.bullet_state == "fire":

        y = player_bullet.ycor()
        y += bullet_speed
        player_bullet.sety(y)
        if player_bullet.ycor() > 280:
            x = main_char.xcor()
            y = main_char.ycor()
            player_bullet.reset_bullet(x, y)

    enemy_bullet.shoot()
    r = enemy_bullet.ycor()
    r -= bullet_speed
    enemy_bullet.sety(r)
    if enemy_bullet.ycor() < -280:
        random_alien = random.choice(alien.sections)
        enemy_bullet.setposition((random_alien.xcor(), random_alien.ycor()))
