import pygame
import settings


class obstacle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 20
        self.center = self.x + self.width // 2
        self.bubble = (self.x - settings.player_width // 2,
                       self.x + self.width + settings.player_width // 2,
                       self.y - settings.player_width // 2,
                       self.y + self.height + settings.player_width // 2)

