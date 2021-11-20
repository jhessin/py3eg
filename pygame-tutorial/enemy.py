""" The Enemy! """
from game_object import GameObject
from pygame import Vector2


class Enemy(GameObject):
    """ The Enemy class handles enemy movement, speed, etc """
    def __init__(self, pos: Vector2, scale: Vector2, image_path: str,
                 speed: float) -> None:
        """ Initializes the Player """
        super().__init__(pos, scale.x, scale.y, image_path)
        self.speed: float = speed

    def move(self, max_width: float):
        """ Move the enemy """
        if self.pos.x <= 0:
            self.speed = abs(self.speed)
        elif self.pos.x >= max_width - self.width:
            self.speed = -abs(self.speed)
        self.pos.x += self.speed
