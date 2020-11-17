import pygame
import settings

class player:

    def __init__(self):
        self.x = 20
        self.y = settings.ground
        self.width = settings.player_width
        self.x_speed = 0
        self.y_speed = 0
        self.isJump = False
        self.ground = settings.ground
        self.overhead = -settings.frame_height
        self.center = self.x + self.width // 2

    def in_bubble(self, obstacle):
        if self.center > obstacle.bubble[0] and self.center < obstacle.bubble[1]:
            return True
        else:
            return False

    def over_obstacle(self, obstacle):
        if self.y + self.width <= obstacle.y:
            return True
        else:
            return False

    def col_obstacle(self, obstacle):
        if self.center < obstacle.bubble[2] and self.center > obstacle.bubble[3]:
            return True
        else:
            return False


