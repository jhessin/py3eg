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

    def detect_collision(self, other) -> bool:
        """ Detect collision with another object """
        object_1 = self.pos
        object_2 = other.pos
        if object_1.y > (object_2.y + other.height):
            return False
        elif (object_1.y + self.height) < object_2.y:
            return False

        if object_1.x > (object_2.x + other.width):
            return False
        elif (object_1.x + self.width) < object_2.x:
            return False

        return True
