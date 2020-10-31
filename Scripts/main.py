import pygame
from player import player

pygame.init()


def redrawWindow(surface):
    global p

    surface.fill((255, 255, 255))
    pygame.draw.line(surface, (0, 0, 0), (0, 450), (800, 450))
    pygame.draw.rect(
        surface, (0, 0, 0), (p.x, p.y, p.width, p.width))
    pygame.draw.rect(surface, (0, 0, 0), (100, 410, 100, 20))
    pygame.display.update()


def main():
    global p

    width = 800
    height = 600

    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Jump N' Run")

    clock = pygame.time.Clock()

    p = player()

    gravity = 5

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

        if not p.isJump and p.standing:
            p.y += gravity
        elif p.isJump:
            p.y_speed -= 5
            p.y += p.y_speed
            if p.y_speed <= -30:
                p.isJump = False
                p.y_speed = 0

        # Borders left/right
        if p.x <= 0:
            p.x = 0
        elif p.x >= width - p.width:
            p.x = width - p.width
        # y-Border
        if p.y >= 410:
            p.y = 410

        p.x += p.x_speed
        redrawWindow(win)


if __name__ == '__main__':
    main()





