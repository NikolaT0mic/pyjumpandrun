import pygame
from player import player
from obstacle import obstacle
from settings import *

pygame.init()

p = player()
o = (obstacle(100, 380), obstacle(400, 410))

def updateWindow(surface):

    surface.fill((255, 255, 255))
    pygame.draw.line(surface, (0, 0, 0), (0, 450), (800, 450))
    pygame.draw.line(surface, (0, 0, 0), (0, p.overhead), (800, p.overhead))
    pygame.draw.rect(
        surface, (0, 0, 0), (p.x, p.y, p.width, p.width))
    for i in o:
        pygame.draw.rect(
            surface, (255, 0, 0), (i.x, i.y, i.width, i.height))
        pygame.draw.line(surface, (0, 0, 0),
                         (i.bubble[0], 600), (i.bubble[0], 0))
        pygame.draw.line(surface, (0, 0, 0),
                         (i.bubble[1], 600), (i.bubble[1], 0))
    pygame.display.update()


def check_collisions(player, obstacle):
    for i in o:
        # if player.in_bubble(i) and pygame.Rect.colliderect(player, i):
            # if player.center < i.center:
                #player.x = i.x - player.width1
            # elif player.center > i.center:
                #player.x = i.x + i.width
            # break
        if player.in_bubble(i) and player.over_obstacle(i):
            player.ground = i.y - player.width
            break
        elif player.in_bubble(i) and not(player.over_obstacle(i)):
            player.overhead = i.y + i.height + 1
            break
        elif not(player.in_bubble(i)):
            player.ground = ground
            player.overhead = -frame_height

        # if player.center < i.center
            # player.x = i.x - player.width:
            # if (player.x + player.width > i.x) and (player.y + player.width) < i.y:
            #player.ground = i.y - player.width
            # break
            # elif player.x + player.width < i.x and player.ground != ground:
            #player.ground = ground
            # elif player.x + player.width > i.x and player.ground == ground:
            #player.x = i.x - player.width
            # break
            # break
        # elif player.center > i.center:
            # if (player.x < i.x + i.width) and (player.y + player.width) < i.y:
            # player.ground = i.y - player.width
            # break
            # elif player.x > i.x + i.width and player.ground != ground:
            #player.ground = ground
            # elif player.x < i.x + i.width and player.ground == ground:
            #player.x = i.x + i.width
            # break


def main():

    running = True
    while running:

        clock.tick(60)
        # Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    p.x_speed = -5

                if event.key == pygame.K_d:
                    p.x_speed = 5

                if event.key == pygame.K_SPACE and not p.isJump:
                    p.isJump = True
                    p.y_speed = -10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and p.x_speed < 0:
                    p.x_speed = 0

                if event.key == pygame.K_d and p.x_speed > 0:
                    p.x_speed = 0

        updateWindow(win)
        # Update player.x dependent on deltatime
        p.x += p.x_speed * clock.get_time() / 10
        # Center of moving objects
        p.center = p.x + p.width // 2

        # Jump Logic
        if p.isJump:
            if p.y <= p.overhead:
                p.y_speed = 0
            p.y_speed += gravity
            p.y += p.y_speed + 0.5 * gravity

        check_collisions(p, o)

        # Borders left/right
        if p.x <= 0:
            p.x = 0
        elif p.x >= frame_width - p.width:
            p.x = frame_width - p.width
        # lower y-Border (depends on player.ground)
        if p.y >= p.ground:
            p.y = p.ground
            p.isJump = False
            p.y_speed = 0
        else:
            p.isJump = True


if __name__ == '__main__':
    main()
