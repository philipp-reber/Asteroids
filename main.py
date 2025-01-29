# use "source venv/bin/activate" in the Terminal (after directing to the appropriate directory) to activate the environment before running this file
import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    #this initiates pygame
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #this sets the screen parameters
    while True:
        #this is the main loop for the game to run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #this makes the game stop when the user closes the game-screen
                return
        player.update(dt)
        #gives the ability to move the player
        screen.fill((0,0,0))
        #this fills the screen with the color black
        player.draw(screen)
        #this draws the player
        pygame.display.flip()
        #this helps display the screen
        dt = clock.tick(60)/1000
        #this limits the framerate to 60 FPS
if __name__ == "__main__":
    main()