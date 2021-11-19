from typing import Tuple
import pygame
from gameObject import GameObject
from player import Player


class Game:
    def __init__(self) -> None:
        self.screen_width: int = 900
        self.screen_height: int = 1000
        self.fill_color: Tuple[int, int, int] = (0, 255, 255)

        item_scale: float = 50
        treasure_x: float = self.screen_width / 2 - item_scale / 2
        treasure_y: float = self.screen_height / 12
        player_x: float = self.screen_width / 2 - item_scale / 2
        player_y: float = self.screen_height * 5 / 6
        player_speed: float = 10

        self.screen: pygame.surface.Surface = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.background: GameObject = GameObject(0, 0, self.screen_width,
                                                 self.screen_height,
                                                 'assets/background.png')
        self.treasure: GameObject = GameObject(treasure_x, treasure_y,
                                               item_scale, item_scale,
                                               'assets/treasure.png')

        self.player: Player = Player(player_x, player_y, item_scale,
                                     item_scale, 'assets/player.png',
                                     player_speed)

    def draw_objects(self):
        self.screen.fill(self.fill_color)
        self.background.renderTo(self.screen)
        self.treasure.renderTo(self.screen)
        self.player.renderTo(self.screen)
        pygame.display.update()

    def game_loop(self):
        player_direction = 0
        while True:
            # Handle Events
            events = pygame.event.get()
            for event in events:
                match event.type:
                    case pygame.QUIT:
                        return
                    case pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            # move player up
                            player_direction = -1
                        elif event.key == pygame.K_DOWN:
                            # move player down
                            player_direction = 1
                        else:
                            player_direction = 0
                    case pygame.KEYUP:
                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            player_direction = 0
                    case _ :
                        pass
            # Execute logic
            self.player.move(player_direction)
            # Update display
            self.draw_objects()

            self.clock.tick(60)
