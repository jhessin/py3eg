import pygame
from gameObject import GameObject


class Player(GameObject):
    def __init__(self, x: float, y: float, width: float, height: float,
                 image_path: str, speed: int) -> None:
        super().__init__(x, y, width, height, image_path)
        self.speed: int = speed

    def move(self, direction):
        self.y += (direction * self.speed)
