#!./bin/python

import pygame
from game import Game


def main():
    pygame.init()

    # Game Code
    game = Game()
    game.game_loop()

    # Quit the game
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
