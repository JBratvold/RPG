"""
-----------------------------------------------------------------------------------------------------------------------
COMMENTS:

I've created a general layout, not sure if it's good.
On Run:

Loads Main Menu (White Background with red rectangle)
To play, click "p"
    Brings you to Game (White Background with black rectangle)
    To go back to Main Menu, click "ESCAPE"
    To go to inventory, click "i"
        Brings you to Inventory (Black Background with red rectangle)
        To go back to game, click "ESCAPE"
    Brings you back to Game (White Background with black rectangle)

I'd like to put words in the menus, and eventually buttons instead.

This is a test number 7
-----------------------------------------------------------------------------------------------------------------------
"""

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
GOLD = (255, 215, 0)

# Initializing fonts
GABRIOLA = pygame.font.match_font("gabriola")

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


# @Purpose: To write to the screen a message or text.
# @PARAM: When using this function, it accepts 1 parameter, a string of text.
# Goals:
#       - Puts text in a button (Start Game, Settings, Load, Etc...)
#       - Pops message up on screen (EXP, Item obtained, Etc...)
#       - More . . . ?
def game_run():
    # Start of running, open main menu
    game_mainMenu()

    # Starts gameExit as false
    gameExit = False

    # A loop to keep track of events in the game while not closed
    while not gameExit:

        for event in pygame.event.get():
            print(event)  # Prints out all the events (Such as mouse movement, button click, keyboard input)
            if event.type == pygame.QUIT:  # If user closes the game
                pygame.quit()  # Stops the program
                quit()  # Closes everything

            if event.type == pygame.KEYDOWN:  # If a key is pressed
                if event.key == pygame.K_ESCAPE:  # If the key pressed was "ESCAPE" on keyboard
                    game_mainMenu()  # Bring us to main menu
            if event.type == pygame.KEYDOWN:  # If a key is pressed
                if event.key == pygame.K_i:  # If the key pressed was "i" on keyboard
                    game_inventoryMenu()  # Bring us to inventory menu

        # While game is not in Exit:
        gameDisplay.fill(WHITE)  # Make the game have a white background
        pygame.draw.rect(gameDisplay, BLACK, (400, 400, 50, 25))  # NOT NEEDED, just to make sure its working
        displayMessage("PLAYING", DISPLAY_WIDTH / 3, 20, 50, GOLD)
        pygame.display.update()  # Updates the display, otherwise it just keeps it was initialized


# @Purpose: To write to the screen a message or text.
# @PARAM: When using this function, it accepts 1 parameter, a string of text.
# Goals:
#       - Puts text in a button (Start Game, Settings, Load, Etc...)
#       - Pops message up on screen (EXP, Item obtained, Etc...)
#       - More . . . ?
def displayMessage(Message_To_Display,X_Coordinate, Y_Coordinate, Font_Size, Color):
    font = pygame.font.Font(GABRIOLA, Font_Size)
    text = font.render(Message_To_Display, True, Color)
    gameDisplay.blit(text, (X_Coordinate,Y_Coordinate))



# @Purpose: To be the main controller for the main menu.
#           It's started in game_run(), and called again if the player pressed the Escape Key
#           It will always be running, and updating while the player is in the Main Menu.
# @PARAM:
# @Goals:
#       - Buttons (Start Game, Settings, Load, Etc...)
#       - Soundtrack (Opening game music)
#       - Cool Background
#       - More . . . ?
#       -
def game_mainMenu():
    mainMenu = True  # Setting this mainMenu variable to be true always

    # A loop to keep track of events in the main menu
    while mainMenu:
        for event in pygame.event.get():
            print(event)  # Prints out all the events (Such as mouse movement, button click, keyboard input)
            if event.type == pygame.QUIT:  # If user closes the game
                pygame.quit()  # Stops the program
                quit()  # Closes everything
            if event.type == pygame.KEYDOWN:  # If there's a key pressed (key down)
                if event.key == pygame.K_p:  # If the key pressed (key down) is " P "hhh
                    mainMenu = False  # End the loop, returning us back to game_run()

        # While in main menu:
        gameDisplay.fill(WHITE)  # Make the starting main Menu have a white background
        pygame.draw.rect(gameDisplay, RED, (400, 400, 50, 25))  # NOT NEEDED, just to make sure its working
        displayMessage("MAIN MENU", DISPLAY_WIDTH/3, 20 , 50, GOLD)
        pygame.display.update()  # Updates the display, otherwise it just keeps it was initialized


# @Purpose: To be the main controller for the inventory menu.
#           It's called if the player pressed the "i" Key
#           It will always be running if "i" is pressed, and updating while the player is in the inventory Menu.
# @PARAM: None
# @Goals:
#       - Show items we have
#       -
def game_inventoryMenu():
    inventoryMenu = True  # Setting this mainMenu variable to be true always

    # A loop to keep track of events in the inventory menu
    while inventoryMenu:
        for event in pygame.event.get():
            print(event)  # Prints out all the events (Such as mouse movement, button click, keyboard input)
            if event.type == pygame.QUIT:  # If user closes the game
                pygame.quit()  # Stops the program
                quit()  # Closes everything
            if event.type == pygame.KEYDOWN:  # If there's a key pressed (key down)
                if event.key == pygame.K_ESCAPE:  # If the key pressed (key down) is " P "
                    inventoryMenu = False  # End the loop, returning us back to game_run()

        # While in inventory menu:
        gameDisplay.fill(BLACK)  # Make the inventory Menu have a black background
        pygame.draw.rect(gameDisplay, RED, (400, 400, 50, 25))  # NOT NEEDED, just to make sure its working
        displayMessage("INVENTORY", DISPLAY_WIDTH / 3, 20, 50, GOLD)
        pygame.display.update()  # Updates the display, otherwise it just keeps it was initialized


"""
-----------------------------------------------------------------------------------------------------------------------
GAME RUNNING 
(Code that is on a continuous loop to keep updating)
while(alive) - render mobs
while(dead) - go into start menu
while(game_startup) - load the main menu
-----------------------------------------------------------------------------------------------------------------------
"""
# This is the function call, it runs the game.
game_run()
