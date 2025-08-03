class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 15 
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed = 3
        self.max_aliens = 3
        self.aliens_to_kill = 10

        # Target settings
        self.target_speed = 2
        self.target_color = (230, 20, 20)
        self.target_miss_limit = 3
        self.target_width = 10
        self.target_height = 200
        # Direction in which the target is moving: 1 is down, -1 is up.
        self.target_direction = 1
