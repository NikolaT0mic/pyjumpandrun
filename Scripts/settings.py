import pygame

frame_width = 800
frame_height = 600

win = pygame.display.set_mode((frame_width, frame_height))
pygame.display.set_caption("Jump N' Run")

clock = pygame.time.Clock()

gravity = 0.5
ground = 410

player_width = 40
