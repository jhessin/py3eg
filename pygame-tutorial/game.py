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
    level: float = 1.0
    screen: pygame.surface.Surface
    clock: pygame.time.Clock = pygame.time.Clock()
    background: GameObject
    treasure: GameObject
    player: Player
    enemies: list[Enemy]

    def __init__(self) -> None:
        self.reset()

    def reset(self):
        """Reset the game"""
        scale_factor: float = 50
        treasure_x: float = self.screen_width / 2 - scale_factor / 2
        treasure_y: float = self.screen_height / 12
        player_x: float = self.screen_width / 2 - scale_factor / 2
        player_y: float = self.screen_height * 5 / 6
        player_speed: float = 10
        speed: float = 5 + (self.level * 5)

        self.screen = pygame.display.set_mode(
                (self.screen_width, self.screen_height))
        self.background = GameObject(Vector2(), self.screen_width,
                self.screen_height,
                'assets/background.png')
        self.treasure = GameObject(Vector2(treasure_x, treasure_y),
                scale_factor, scale_factor,
                'assets/treasure.png')

        self.player = Player(Vector2(player_x, player_y),
                Vector2(scale_factor, scale_factor), 'assets/player.png',
                player_speed)

        if self.level >= 4.0:
            self.enemies = [
                    Enemy(Vector2(0, 600), Vector2(scale_factor, scale_factor),
                        'assets/enemy.png', speed),
                    Enemy(Vector2(750, 400), Vector2(scale_factor, scale_factor),
                        'assets/enemy.png', speed),
                    Enemy(Vector2(0, 200), Vector2(scale_factor, scale_factor),
                        'assets/enemy.png', speed),
                    ]
        elif self.level >= 3.0:
            self.enemies = [
                    Enemy(Vector2(0, 600), Vector2(scale_factor, scale_factor),
                        'assets/enemy.png', speed),
                    Enemy(Vector2(0, 200), Vector2(scale_factor, scale_factor),
                        'assets/enemy.png', speed),
                    ]
        else:
            self.enemies = [
                    Enemy(Vector2(750, 400), Vector2(scale_factor, scale_factor),
                        'assets/enemy.png', speed),
                    ]

    def draw_objects(self):
        """ Draw all game objects to the screen """
        self.screen.fill(self.fill_color)
        self.background.render_to(self.screen)
        self.treasure.render_to(self.screen)
        self.player.render_to(self.screen)
        for enemy in self.enemies:
            enemy.render_to(self.screen)
        pygame.display.update()

    def detect_collisions(self):
        """Detect all types of collision"""
        for enemy in self.enemies:
            if self.player.detect_collision(enemy):
                return 'lose'
        if self.player.detect_collision(self.treasure):
            return 'win'
        return None


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
            for enemy in self.enemies:
                enemy.move(self.screen_width)
            # Update display
            self.draw_objects()

            match self.detect_collisions():
                case 'win':
                    self.level += 0.5
                    self.reset()
                case 'lose':
                    self.level = 1.0
                    self.reset()
                case None:
                    pass

            self.clock.tick(60)
