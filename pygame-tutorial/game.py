"""
    This holds the Game class that will run all game logic.
"""
from typing import Tuple
import pygame
from pygame import Vector2
from game_object import GameObject
from player import Player
from enemy import Enemy

class Game:
    """ The Game Class """
    screen_width: int = 900
    screen_height: int = 1000
    fill_color: Tuple[int, int, int] = (0, 255, 255)


    def __init__(self) -> None:
        item_scale: float = 50
        treasure_x: float = self.screen_width / 2 - item_scale / 2
        treasure_y: float = self.screen_height / 12
        player_x: float = self.screen_width / 2 - item_scale / 2
        player_y: float = self.screen_height * 5 / 6
        player_speed: float = 10

        self.screen: pygame.surface.Surface = pygame.display.set_mode(
                (self.screen_width, self.screen_height))
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.background: GameObject = GameObject(Vector2(), self.screen_width,
                self.screen_height,
                'assets/background.png')
        self.treasure: GameObject = GameObject(Vector2(treasure_x, treasure_y),
                item_scale, item_scale,
                'assets/treasure.png')

        self.player: Player = Player(Vector2(player_x, player_y),
                Vector2(item_scale, item_scale), 'assets/player.png',
                player_speed)
        self.enemy: Enemy = Enemy(Vector2(50, 600), Vector2(50, 50),
                'assets/enemy.png', 10)

    def draw_objects(self):
        """ Draw all game objects to the screen """
        self.screen.fill(self.fill_color)
        self.background.render_to(self.screen)
        self.treasure.render_to(self.screen)
        self.player.render_to(self.screen)
        self.enemy.render_to(self.screen)
        pygame.display.update()

    def game_loop(self):
        """ The Main Game Loop """
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
                        if event.key in (pygame.K_UP, pygame.K_DOWN):
                            player_direction = 0
                    case _ :
                        pass
            # Execute Logic
            self.player.move(player_direction, self.screen_height)
            self.enemy.move(self.screen_width)
            # Update display
            self.draw_objects()

            self.clock.tick(60)
