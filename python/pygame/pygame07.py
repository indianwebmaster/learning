# From: https://realpython.com/pygame-a-primer/#background-and-setup
# Transformed as a class

# In pygame, everything is viewed on a single user-created display, which can be a window or a full screen.
# The display is created using .set_mode(), which returns a Surface representing the visible part of the window.
# It is this Surface that you pass into drawing functions like pygame.draw.circle(), and the contents of that Surface
# are pushed to the display when you call pygame.display.flip()

import pygame
# Import pygame.locals for easier access to key coordinates
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, K_SPACE, KEYDOWN, QUIT)
from pygame.locals import RLEACCEL  # constant is an optional parameter that helps pygame render more quickly on non-accelerated displays
import random

# CONSTANTS
SCREEN_WIDTH,SCREEN_HEIGHT = 800,600

# How do you know if an obstacle has collided with the fighter?
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
class MyFighter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.surf = pygame.Surface((75,25))
        # self.surf.fill((255,255,0))
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL) # Show color==white as transparent. Use accelerated rendering
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)    # Use .move_ip(), which stands for move in place, to move the current Rect.
        elif pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        # elif pressed_keys[K_LEFT]:
        #     self.rect.move_ip(-5, 0)  # CANNOT MOVE BACKWARDS
        elif pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep fighter on screen
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.right > SCREEN_WIDTH: self.rect.right = SCREEN_WIDTH
        if self.rect.bottom > SCREEN_HEIGHT: self.rect.bottom = SCREEN_HEIGHT


class MyBullet(pygame.sprite.Sprite):
    def __init__(self, fighter):
        super().__init__()
        self.surf = pygame.Surface((10,5))
        self.surf.fill ((0x0,0xff,0x0))
        self.rect = self.surf.get_rect(center=(fighter.rect.right,fighter.rect.bottom))
        self.speed = 25

    def update(self):
        self.rect.move_ip(self.speed,0) # Only move to the right
        if self.rect.left > SCREEN_WIDTH: self.kill()


class MyMissile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.surf = pygame.Surface((20,10))
        # self.surf.fill((255,0,0))
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL) # Show color==white as transparent. Use accelerated rendering
        # update rect to be a random location with the center just off the screen.
        # It’s located at some position between 20 and 100 pixels away from the right edge, and somewhere between the top and bottom edges.
        self.rect = self.surf.get_rect(
                center=(
                        random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                        random.randint(0, SCREEN_HEIGHT)
                )
        )
        # Define .speed as a random number between 5 and 20. This specifies how fast this missile moves towards the fighter
        self.speed = random.randint(5,20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)   # Only move towards the left
        if self.rect.right < 0: self.kill()     # Remove sprite when it moves pass the left edge, This will prevent it from processing further.


class MyCloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.surf = pygame.Surface((100,50))
        # self.surf.fill((255,0,0))
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL) # Show color==white as transparent. Use accelerated rendering
        # update rect to be a random location with the center just off the screen.
        # It’s located at some position between 20 and 100 pixels away from the right edge, and somewhere between the top and bottom edges.
        self.rect = self.surf.get_rect(
                center=(
                        random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                        random.randint(0, SCREEN_HEIGHT)
                )
        )
        # Define .speed as a constant speed for the clouds movement
        self.speed = 5

    def update(self):
        self.rect.move_ip(-self.speed, 0)   # Only move towards the left
        if self.rect.right < 0: self.kill()     # Remove sprite when it moves pass the left edge, This will prevent it from processing further.


class PygameTest07:
    def __init__(self):
        self.__setupConstants()
        # Set up the drawing window
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # The event loop is designed to look for ALL events occurring every frame and deal with them appropriately.
        # pygame doesn’t restrict you to using only the event types it has defined. You can define your own events to handle as you see fit.

        # Create a CUSTOM event for adding a new Missile object in the game
        self.ADD_ENEMY = pygame.USEREVENT + 1    # The last event (int val) pygame reserves is called USEREVENT, so +1 ensures it’s unique
        pygame.time.set_timer(self.ADD_ENEMY, 1000)   # insert this new event into the event queue at regular intervals throughout the game
        self.ADD_CLOUD = pygame.USEREVENT + 2    # The last event (int val) pygame reserves is called USEREVENT, so +1 ensures it’s unique
        pygame.time.set_timer(self.ADD_CLOUD, 1000)   # insert this new event into the event queue at regular intervals throughout the game

        pygame.mixer.init()  # Setup for sounds. Just use default args, which is fine
        self.bulletFiredSound = pygame.mixer.Sound('bulletFired.mp3')
        self.planeExplodesSound = pygame.mixer.Sound('planeExplodes.mp3')
        self.missileExplodesSound = pygame.mixer.Sound('missileExplodes.mp3')

        # Game loop processes frames as fast as the processor and environment will allow.
        # Since all the sprites move once per frame, they can move hundreds of times each second.
        # The number of frames handled each second is called the frame rate

        # Normally, you want as high a frame rate as possible, but for this game, you need to slow it down a bit for the game to be playable.
        # Fortunately, the module time contains a Clock which is designed exactly for this purpose
        # Setup the clock for a decent framerate
        self.clock = pygame.time.Clock()

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

        fighter = MyFighter()

        # Another super useful class that pygame provides is the Sprite Group.
        # This is an object that holds a group of Sprite objects.
        # So why use it? Can’t you just track your Sprite objects in a list instead?
        #       Well, you can, but the advantage of using a Group lies in the methods it exposes.
        #       These methods help to detect whether any Missile has collided with the Fighter, which makes updates much easier
        all_sprites = pygame.sprite.Group()     # will hold every Sprite in the game
        missiles = pygame.sprite.Group()         # hold just the Missile objects
        clouds = pygame.sprite.Group()         # hold just the Cloud objects
        bullets = pygame.sprite.Group()         # hold the Bullet objects

        all_sprites.add(fighter)

        # Main game loop
        while running:
            # Fill the background with white
            self.screen.fill((0x87, 0xCE, 0xEB))

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

                elif event.type == self.ADD_ENEMY:
                    # Create a new Missile and add to the sprite groups
                    new_missile = MyMissile()
                    missiles.add(new_missile)
                    all_sprites.add(new_missile)

                elif event.type == self.ADD_CLOUD:
                    # Create a new Missile and add to the sprite groups
                    new_cloud = MyCloud()
                    clouds.add(new_cloud)
                    all_sprites.add(new_cloud)

            # Get all the keys currently pressed
            pressed_keys = pygame.key.get_pressed()  # returns a dictionary containing all the current KEYDOWN events in the queue
            # Update the fighter sprite based on the keys pressed
            fighter.update(pressed_keys)
            if pressed_keys[K_SPACE]:
                new_bullet = MyBullet(fighter)
                self.bulletFiredSound.play()
                bullets.add(new_bullet)
                all_sprites.add(new_bullet)

            # Update missile and clouds position
            missiles.update()
            clouds.update()
            bullets.update()

            # Now that we have a sprite.Group(), draw all sprites in a loop
            for entity in all_sprites:
                # Pass the sprite's surface
                self.screen.blit(entity.surf, entity.rect)  # Uses the coordinates of the top left corner of Rect to draw the surface.

            # Check if any missiles have collided with the fighter
            fighterHit = pygame.sprite.spritecollideany(fighter, missiles) # args = (sprite, sprite.Group). Returns first collision sprite within spriteGroup.
            if fighterHit is not None:
                # If so, then remove the fighter and stop the loop
                self.planeExplodesSound.play()
                pygame.time.wait(1000)
                fighter.kill()
                running = False

            for bullet in bullets:
                missileDestroyed = pygame.sprite.spritecollideany(bullet, missiles)
                if missileDestroyed is not None:
                    # If so, then remove the missile and bullet
                    self.missileExplodesSound.play()
                    missileDestroyed.kill()
                    bullet.kill()

            # Update display with any changes made since the last flip. So, all surfaces at the last flip remain and new since then are shown.
            pygame.display.flip()

            # Ensure program maintains a rate of 10 frames per second. Smaller the number, slower the speed.
            self.clock.tick(10)


# Import and initialize the pygame library
# This function calls the separate init() functions of all the included pygame modules.
#       Since these modules are abstractions for specific hardware, this initialization step is required
#       so that you can work with the same code on Linux, Windows, and Mac.
pygame.init()

pygameTest = PygameTest07()
pygameTest.run()

# Done! Time to quit.
pygame.quit()
