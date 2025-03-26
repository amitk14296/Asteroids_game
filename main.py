# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import*
def main():
    pygame.init()#initializing the pygame library
    pygame.display.set_mode()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#this is taking screen_width and screen_height
    dt = 0
    clock = pygame.time.Clock()#creating a pygame.time.Clock() object
    
#Starting the game loop
    i = 0
    while i == 0:#loop will run till i is 0(no increment is setup for i to make it a infinite loop)
        for event in pygame.event.get():#to know when user quit the game(more to be read)
            if event.type == pygame.QUIT:
                return
        screen.fill("black")#here screen is object to the pygame.display.set_mode()
                            # and we are using fill method to put black color on the screen
        pygame.display.flip()#update full display surface to the screen
        dt = (clock.tick(60))/1000
if __name__ == "__main__":
    main()
