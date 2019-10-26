"""
-----------------------------------------------------------------------------------------------------------------------
IMPORTS & LIBRARIES
-----------------------------------------------------------------------------------------------------------------------
"""
import pygame

"""
-----------------------------------------------------------------------------------------------------------------------
GAME SET UP 
(Initializations)
(Static/Non-changing variables) - Like game size x + y, menu size x + y [I use all caps for static variables]
-----------------------------------------------------------------------------------------------------------------------
"""
pygame.init()  # Initializing pygame

# Initializing colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

DISPLAY_WIDTH = 800  # Width of game screen
DISPLAY_HEIGHT = 600  # Height of game screen
GAME_NAME = "JT's RPG"  # Name of game

pygame.display.set_caption(GAME_NAME)  # Setting display caption to our game name

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))  # Setting display size to our width and height


"""
-----------------------------------------------------------------------------------------------------------------------
FUNCTIONS/DEFINITIONS 
This will probably be the largest portion.
-----------------------------------------------------------------------------------------------------------------------
"""

def game_mainMenu():
    mainMenu = True  # Setting this mainMenu variable to be true always

    while mainMenu:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(WHITE)
        pygame.draw.rect(gameDisplay, RED, (400, 400, 50, 25))
        pygame.display.update()






"""
-----------------------------------------------------------------------------------------------------------------------
GAME RUNNING 
(Code that is on a continuous loop to keep updating)
while(alive) - render mobs
while(dead) - go into start menu
while(game_startup) - load the main menu
-----------------------------------------------------------------------------------------------------------------------
"""
game_mainMenu()
#
#
#