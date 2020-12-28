# From: https://realpython.com/pygame-a-primer/#background-and-setup
# Transformed as a class

# In pygame, everything is viewed on a single user-created display, which can be a window or a full screen.
# The display is created using .set_mode(), which returns a Surface representing the visible part of the window.
# It is this Surface that you pass into drawing functions like pygame.draw.circle(), and the contents of that Surface
# are pushed to the display when you call pygame.display.flip()

import pygame
# Import pygame.locals for easier access to key coordinates
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)

# CONSTANTS
SCREEN_WIDTH,SCREEN_HEIGHT = 800,600

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

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)    # Use .move_ip(), which stands for move in place, to move the current Rect.
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        # Keep player on screen
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.right > SCREEN_WIDTH: self.rect.right = SCREEN_WIDTH
        if self.rect.bottom > SCREEN_HEIGHT: self.rect.bottom = SCREEN_HEIGHT

class PygameTest04:
    def __init__(self):
        self.__setupConstants()
        # Set up the drawing window
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def __setupConstants(self):
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = SCREEN_WIDTH,SCREEN_HEIGHT

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
            # Fill the background with white
            self.screen.fill((255, 255, 255))

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

            # Get all the keys currently pressed
            pressed_keys = pygame.key.get_pressed()  # returns a dictionary containing all the current KEYDOWN events in the queue
            # Update the player sprite based on the keys pressed
            player.update(pressed_keys)

            # Pass the player sprite's surface
            self.screen.blit(player.surf, player.rect)  # Uses the coordinates of the top left corner of Rect to draw the surface.

            # Update display with any changes made since the last flip. So, all surfaces at the last flip remain and new since then are shown.
            pygame.display.flip()


# Import and initialize the pygame library
# This function calls the separate init() functions of all the included pygame modules.
#       Since these modules are abstractions for specific hardware, this initialization step is required
#       so that you can work with the same code on Linux, Windows, and Mac.
pygame.init()

pygameTest = PygameTest04()
pygameTest.run()

# Done! Time to quit.
pygame.quit()
