import pygame

class Target:
    "A class to manage the target."""

    def __init__(self, ai_game):
        """Initialize the target."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.color = self.settings.target_color

        # Create a rectangle at (0, 0) then center on the right.
        self.rect = pygame.Rect(0, 0, self.settings.target_width,
                                self.settings.target_height)
        self.rect.midright = self.screen_rect.midright

        # Store the target's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the target up and down."""
        if self.rect.bottom >= self.screen_rect.bottom:
            self.settings.target_direction = -1
        if self.rect.top <= 0:
            self.settings.target_direction = 1
        self.y += self.settings.target_speed * self.settings.target_direction
        self.rect.y = self.y

    def draw_target(self):
        """Draw the target on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def reset_target(self):
        """Recenter the target and set direction to down."""
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)
        self.settings.target_direction = 1
