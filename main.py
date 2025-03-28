# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import*
from player import*

def main():
    pygame.init()#initializing the pygame library
    pygame.display.set_mode()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#this is taking screen_width and screen_height
    dt = 0
    clock = pygame.time.Clock()#creating a pygame.time.Clock() object
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
#Starting the game loop
    i = 0
    while i == 0:#loop will run till i is 0(no increment is setup for i to make it a infinite loop)
        for event in pygame.event.get():#to know when user quit the game(more to be read)
            if event.type == pygame.QUIT:
                return
        screen.fill("black")#here screen is object to the pygame.display.set_mode()
                            # and we are using fill method to put black color on the screen
        for d in drawable:
            d.draw(screen)#player has to be drawn before updating display surface to screen and after background color
        updatable.update(dt)
        pygame.display.flip()#update full display surface to the screen
        dt = (clock.tick(60))/1000# calling the .tick(method) dividign its output by 1000 to convert is to seconds
                                #and passing that output to dt variable
        
if __name__ == "__main__":
    main()
