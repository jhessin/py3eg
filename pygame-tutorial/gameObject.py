import pygame


class GameObject:
    def __init__(self, x: float, y: float, width: float, height: float,
                 image_path: str) -> None:
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, (width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def renderTo(self, screen: pygame.surface.Surface):
        screen.blit(self.image, (self.x, self.y))
