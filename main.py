import random
import time
from turtle import Screen
from player import Player
from bullets import Bullet
from invaders import Invaders

# initialize the screen attributes
from score_and_lives import ScoreBoard
from walls import Wall

screen = Screen()
screen.setup(width=900, height=600)
screen.bgpic("stars-g2ffe12732_1920.gif")
screen.title("Space Invaders")
screen.tracer(0)

# register images
alien_image = "ufo-g5df1555f0_1280.gif"
brick_image = "bricks-g5d0de5048_1920.gif"
screen.addshape(alien_image)
screen.addshape(brick_image)

position = (0, -250)
bullet_speed = 15


main_char = Player(position)
player_bullet = Bullet((main_char.xcor(), main_char.ycor()))
player_bullet.color("yellow")


alien = Invaders()
for i in alien.sections:
    i.shape(alien_image)


score_board = ScoreBoard()

random_alien = random.choice(alien.sections)
enemy_bullet = Bullet((random_alien.xcor(), random_alien.ycor()))
enemy_bullet.color("red")

fence = Wall()
for i in fence.wall_sections:
    i.shape(brick_image)


screen.listen()
screen.onkey(fun=main_char.move_left, key="Left")
screen.onkey(fun=main_char.move_right, key="Right")
screen.onkey(fun=player_bullet.shoot, key="Up")


def go_boom(container, content):
    """make object disappear from screen"""
    container.remove(content)
    content.goto(0, 3000)


bounce_count = 0
delay = 0.2

game_on = True
while game_on:

    screen.update()
    time.sleep(delay)
    alien.move()

    if score_board.lives == 0:
        game_on = False

    if not alien.sections:
        alien.create_ship()


    for i in alien.sections:
        if i.xcor() < -420 or i.xcor() > 420:
            alien.reverse()
            bounce_count += 1
            if bounce_count % 2 == 0:
                alien.move_down()

        if i.distance(player_bullet) < 20:
            score_board.score += 1
            score_board.clear()
            score_board.update_score()
            go_boom(alien.sections, i)
            x = main_char.xcor()
            y = main_char.ycor()
            player_bullet.reset_bullet(x, y)

    if enemy_bullet.distance(player_bullet) < 10:
        x = main_char.xcor()
        y = main_char.ycor()
        player_bullet.reset_bullet(x, y)
        random_alien = random.choice(alien.sections)
        enemy_bullet.setposition((random_alien.xcor(), random_alien.ycor()))

    if enemy_bullet.distance(main_char) < 30:
        main_char.reset_player()
        score_board.lives -= 1
        score_board.clear()
        score_board.update_score()

    for i in fence.wall_sections:
        if enemy_bullet.distance(i) < 10:
            go_boom(fence.wall_sections, i)
            random_alien = random.choice(alien.sections)
            enemy_bullet.setposition((random_alien.xcor(), random_alien.ycor()))
        if player_bullet.distance(i) < 10:
            go_boom(fence.wall_sections, i)
            x = main_char.xcor()
            y = main_char.ycor()
            player_bullet.reset_bullet(x, y)

            # if i.distance(alien.sections) < 10:
            pass
            # go_boom(fence.wall_sections, i)

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
