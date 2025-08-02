import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star and set its starting position."""

    def __init__(self, ai_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # Start each new star at the top left of the screen.
        self.rect.x = 0
        self.rect.y = 0

        # Store the star's exact horizontal position
        self.x = float(self.rect.x)
