# From: https://realpython.com/pygame-a-primer/#background-and-setup
# Transformed as a class

# In pygame, everything is viewed on a single user-created display, which can be a window or a full screen.
# The display is created using .set_mode(), which returns a Surface representing the visible part of the window.
# It is this Surface that you pass into drawing functions like pygame.draw.circle(), and the contents of that Surface
# are pushed to the display when you call pygame.display.flip()

import pygame

class PygameTest01:
    def __init__(self):
        # Set up the drawing window
        self.screen = pygame.display.set_mode([500, 500])

    def run(self):
        # Run until the user asks to quit
        running = True
        while running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the background with white
            self.screen.fill((255, 255, 255))

            # Draw a solid blue circle in the center
            pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)
            # You can also load a disk image and load into the Surface object (self.screen)
            #   See: https://www.pygame.org/docs/ref/image.html

            # Flip the display
            pygame.display.flip()

# Import and initialize the pygame library
# This function calls the separate init() functions of all the included pygame modules.
#       Since these modules are abstractions for specific hardware, this initialization step is required
#       so that you can work with the same code on Linux, Windows, and Mac.
pygame.init()

pygameTest = PygameTest01()
pygameTest.run()

# Done! Time to quit.
pygame.quit()
