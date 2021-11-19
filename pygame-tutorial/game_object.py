""" Holds the base GameObject and Vector for positioning """
import pygame
from pygame import Vector2


class GameObject:
    """ The Base Game Object that is used for all game objects """
    def __init__(self, pos: Vector2, width: float, height: float,
                 image_path: str) -> None:
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, (width, height))
        self.pos: Vector2 = pos
        self.width = width
        self.height = height

    def render_to(self, screen: pygame.surface.Surface):
        """Render the game object to the given screen"""
        screen.blit(self.image, (self.pos.x, self.pos.y))
