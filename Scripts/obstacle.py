import pygame


class obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 20
        self.center = self.x + self.width / 2 + self.height / 2

