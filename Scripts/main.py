import pygame
from player import player
from obstacle import obstacle

pygame.init()


def redrawWindow(surface):
    global p, o, p_modell, o_modell

    surface.fill((255, 255, 255))
    pygame.draw.line(surface, (0, 0, 0), (0, 450), (800, 450))
    p_modell = pygame.draw.rect(
        surface, (0, 0, 0), (p.x, p.y, p.width, p.width))
    o_modell = pygame.draw.rect(
        surface, (255, 0, 0), (o.x, o.y, o.width, o.height))
    pygame.display.update()


def main():
    global p, o, p_modell, o_modell

    width = 800
    height = 600

    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Jump N' Run")

    clock = pygame.time.Clock()

    p = player()
    o = obstacle(100, 410)

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

        redrawWindow(win)
        p.x += p.x_speed

        # Jump Logic
        if not p.isJump:
            p.y += gravity
        elif p.isJump:
            p.y_speed -= 5
            p.y += p.y_speed
            if p.y_speed <= -30:
                p.isJump = False
                p.y_speed = 0
        # Jump on obstacle
        if (p.x + p.width > o.x or p.x < o.x + o.width) and (p.y + p.width) < o.y:
            p.ground = o.y - p.width
        elif p.ground == o.y - p.width and p.x + p.width < o.x:
            p.ground = 410
        elif p.ground == o.y - p.width and p.x > o.x + o.width:
            p.ground = 410
        elif pygame.Rect.colliderect(p_modell.inflate(1, 0), o_modell) and p.x + p.width > o.x and p.ground == 410:
            p.x = o.x - p.width
        elif pygame.Rect.colliderect(p_modell, o_modell.inflate(1, 0)) and p.x < o.x + o.width and p.ground == 410:
            p.x = o.x + o.width
        # Borders left/right
        if p.x <= 0:
            p.x = 0
        elif p.x >= width - p.width:
            p.x = width - p.width
        # y-Border (depends on player.ground)
        if p.y >= p.ground:
            p.y = p.ground


if __name__ == '__main__':
    main()





