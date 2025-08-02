import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop and set its starting position."""

    def __init__(self, ai_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrot at the top left of the screen.
        self.rect.x = 0
        self.rect.y = 0

        # Store the raindrop's exact vertical position
        self.y = float(self.rect.y)

    def update(self):
        """Move the raindrop down."""
        self.y += self.settings.rain_speed
        self.rect.y = self.y

    def check_bottom(self):
        """Return True if the raindrop is at the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        return self.rect.top >= screen_rect.bottom
