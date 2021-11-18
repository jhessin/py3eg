#!/usr/bin/env python3

import pygame


def main():
    pygame.init()

    # Game Code
    width = 800
    height = 800
    fill_color = (0, 255, 255)

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    def game_loop():
        while True:
            # Handle Events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
            # Execute logic
            # Update display
            screen.fill(fill_color)
            pygame.display.update()

            clock.tick(60)

    game_loop()

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
