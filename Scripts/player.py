import pygame

class player:

    def __init__(self):
        self.x = 20
        self.y = 410
        self.width = 40
        self.x_speed = 0
        self.y_speed = 0
        self.isJump = False
        self.ground = 410
        self.center = self.x + self.width / 2 + self.width / 2

