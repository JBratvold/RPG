import pygame
import sys
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 900))

bg = pygame.image.load("images\\test chocobo.jpg")

pygame.mouse.set_visible(0)

ship = pygame.image.load("images\\test military rifle.png")
ship_top = screen.get_height() - ship.get_height()
ship_left = screen.get_width()/2 - ship.get_width()/2

screen.blit(ship, (ship_left, ship_top))

shot = pygame.image.load("images\\test wizard.png")
shoot_y = 0


pygame.display.set_caption('galaxy invaders')

while True:
    clock.tick(60)
    screen.fill([255, 255, 255])

    x, y = pygame.mouse.get_pos()
    screen.blit(ship, (x-ship.get_width()/2, ship_top))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            shoot_y = 500
            shoot_x = x-250

    if shoot_y > 0:
        screen.blit(shot, (shoot_x, shoot_y))
        shoot_y -= 5

    pygame.display.update()