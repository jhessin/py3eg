""" Holds the Player GameObject and logic """
from game_object import GameObject
from pygame import Vector2


class Player(GameObject):
    """ The Player class handles player movement, score, etc """
    def __init__(self, pos: Vector2, scale: Vector2, image_path: str,
                 speed: float) -> None:
        """ Initializes the Player """
        super().__init__(pos, scale.x, scale.y, image_path)
        self.speed: float = speed

    def move(self, direction: int, max_height: float):
        """ Move the player """
        if (self.pos.y >= max_height - self.height
                and direction > 0) or (self.pos.y <= 0 and direction < 0):
            return
        self.pos.y += (direction * self.speed)
