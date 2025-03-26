# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import*
def main():
    pygame.init
    pygame.display.set_mode()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    i = 0
    while i == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
if __name__ == "__main__":
    main()
