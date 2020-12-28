# From: https://realpython.com/pygame-a-primer/#background-and-setup
# Transformed as a class

# In pygame, everything is viewed on a single user-created display, which can be a window or a full screen.
# The display is created using .set_mode(), which returns a Surface representing the visible part of the window.
# It is this Surface that you pass into drawing functions like pygame.draw.circle(), and the contents of that Surface
# are pushed to the display when you call pygame.display.flip()

import pygame
# Import pygame.locals for easier access to key coordinates
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)

# How do you know if an obstacle has collided with the player?
# What happens when the obstacle flies off the screen?
# What if you want to draw background images that also move?
# What if you want your images to be animated?
#       You can handle all these situations and more with sprites.
#
# In programming terms, a sprite is a 2D representation of something on the screen.
# Essentially, it’s a picture.
# pygame provides a Sprite class, which is designed to hold one or several graphical representations of any game object
# that you want to display on the screen.
# To use it, you create a new class that extends Sprite
class MyPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,0))
        self.rect = self.surf.get_rect()


class PygameTest03:
    def __init__(self):
        self.__setupConstants()
        # Set up the drawing window
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def __setupConstants(self):
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = 800,600

    # Every cycle of the game loop is called a frame.
    # The quicker you can do things each cycle, the faster your game will run.
    # Frames continue to occur until some condition to exit the game is met.
    # During each game loop/frame, 4 important things happen
    #   1. Process User Input   2. Update states of all game objects    3. Update display and audio output  4. Maintain (slow) speed of game
    def run(self):
        # Run until the user asks to quit
        running = True

        player = MyPlayer()

        # Main game loop
        while running:
            # All events end up in a queue. Look at every event in the queue
            for event in pygame.event.get():
                # 1. PROCESS USER INPUT
                # Did the user press any key. Keypress events have the event type KEYDOWN.
                # The KEYDOWN event also has a variable called key to indicate which key was pressed
                if event.type == KEYDOWN:
                    # Was it the ESCAPE key, treat it as a QUIT
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == pygame.QUIT:
                    running = False

            # Fill the background with white
            self.screen.fill((255, 255, 255))

            # Create a surface and pass in a tuple containing its length and width
            surf = pygame.Surface((50, 50))
            # Give the surface a color to separate it from the background
            surf.fill((0, 0, 0))
            # Just creating a new Surface isn’t enough to see it on the screen.
            # To do that, you need to blit (blit stands for Block Transfer) the Surface onto another Surface.
            # <To_Surface>.blit(<FROM_Surface>, (xPos,yPos)) is how you copy the contents of one Surface to another.
            # You can only .blit() from one Surface to another, but since the screen is just another Surface, that’s not a problem
            self.screen.blit(surf,(self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2))

            self.screen.blit(player.surf,(self.SCREEN_WIDTH/4, self.SCREEN_HEIGHT/4))
            self.screen.blit(player.surf, player.rect)  # Uses the coordinates of the top left corner of Rect to draw the surface.

            # You can also access its underlying Rect using .get_rect(). Just saving it for later for now.
            rect = surf.get_rect()

            # # Draw a solid blue circle in the center. This utility function draw.circle does the Surface creation and blit operation in one.
            pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)

            # Update display with any changes made since the last flip. So, all surfaces at the last flip remain and new since then are shown.
            pygame.display.flip()


# Import and initialize the pygame library
# This function calls the separate init() functions of all the included pygame modules.
#       Since these modules are abstractions for specific hardware, this initialization step is required
#       so that you can work with the same code on Linux, Windows, and Mac.
pygame.init()

pygameTest = PygameTest03()
pygameTest.run()

# Done! Time to quit.
pygame.quit()
