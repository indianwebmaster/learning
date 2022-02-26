import time
import pygame

class TestPygame02:
    def __init__(self):
        self.screenSize=(500,500)

    def run1(self):
        circleXY = (int(self.screenSize[0]/2),int(self.screenSize[1]/2))
        circleMaxRadius = int(self.screenSize[0]/2)
        bg_rgb = (0,128,255)

        screen = pygame.display.set_mode(self.screenSize)

        circleRadius = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: running = False

            screen.fill(bg_rgb)
            bg_rgb = (bg_rgb[1],bg_rgb[2],bg_rgb[0])
            if circleRadius < circleMaxRadius:
                circleRadius += 10
            else:
                circleRadius = 0
            pygame.draw.circle(screen, bg_rgb, circleXY, circleRadius)

            pygame.display.flip()
            time.sleep(1)


    def run2(self):
        circleXY = (0,0)
        bg_rgb = (0,128,255)
        circleRGB = (0,64,128)

        screen = pygame.display.set_mode(self.screenSize)

        circleRadius = 10
        running = True
        while running:
            screen.fill(bg_rgb)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: running = False

            pygame.draw.circle(screen, circleRGB, circleXY, circleRadius)
            circleRGB = (circleRGB[1],circleRGB[2],circleRGB[0])
            circleXY = (circleXY[0]+10, circleXY[1]+10)
            if circleXY[0] > self.screenSize[0]: circleXY = (0,circleXY[1])
            if circleXY[1] > self.screenSize[1]: circleXY = (circleXY[0],0)

            pygame.display.flip()
            pygame.time.delay(125)

    def run3(self):
        bg_rgb = (0,128,255)
        xy = (0,0)
        rectRGB = (0,64,128)

        screen = pygame.display.set_mode(self.screenSize)

        widthHeight = (10,10)
        running = True
        while running:
            screen.fill(bg_rgb)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: running = False

            rect = pygame.Rect(xy,widthHeight)
            pygame.draw.rect(screen, rectRGB, rect)
            rectRGB = (rectRGB[1],rectRGB[2],rectRGB[0])
            xy = (xy[0]+10, xy[1]+10)
            if xy[0] > self.screenSize[0]: xy = (0,xy[1])
            if xy[1] > self.screenSize[1]: xy = (xy[0],0)

            pygame.display.flip()
            pygame.time.delay(125)

    def run4(self):
        bg_rgb = (0,128,255)
        xy = (0,0)
        rectRGB = (0,64,128)

        screen = pygame.display.set_mode(self.screenSize)

        screen.fill(bg_rgb)
        pygame.display.flip()

        widthHeight = (10,10)
        running = True
        while running:
            screen.fill(bg_rgb)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: running = False

                if event.type  == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if 1 in keys:
                        if keys[pygame.K_DOWN ]: xy = (xy[0], xy[1]+10)
                        if keys[pygame.K_UP   ]: xy = (xy[0], xy[1] - 10)
                        if keys[pygame.K_LEFT ]: xy = (xy[0] - 10, xy[1])
                        if keys[pygame.K_RIGHT]: xy = (xy[0] + 10, xy[1])

                        if xy[0] > self.screenSize[0]: xy = (0, xy[1])
                        if xy[1] > self.screenSize[1]: xy = (xy[0], 0)
                        if xy[0] < 0: xy = (self.screenSize[0], xy[1])
                        if xy[1] < 0: xy = (xy[0], self.screenSize[1])

                        rect = pygame.Rect(xy,widthHeight)
                        pygame.draw.rect(screen, rectRGB, rect)

                        rectRGB = (rectRGB[1],rectRGB[2],rectRGB[0])

                        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    game = TestPygame02()
    game.run4()
    pygame.quit()
