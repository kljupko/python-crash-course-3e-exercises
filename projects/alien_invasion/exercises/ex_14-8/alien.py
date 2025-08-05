from random import randint

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to manage the alien."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and get its rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Start the alien at a random position on the right.
        self.rect.x = self.settings.screen_width - self.rect.width
        self.rect.y = randint(0, self.settings.screen_height - self.rect.height)

        # Store a float for the alien's exact horizontal position.
        self.x = float(self.rect.x)


    def update(self):
        """Move the alien to the left."""
        # Update the ship's x value (internal position)
        self.x -= self.settings.alien_speed

        # Update the ship's rect object (drawn position) from self.x
        self.rect.x = self.x
    
    def check_edge(self):
        """Return True if the ship is at the left edge."""
        return self.x <= 0
