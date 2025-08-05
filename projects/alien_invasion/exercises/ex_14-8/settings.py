class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # I/O settings
        self.score_path = "data/score.json"
        self.music_path = "sound/music/evil_by_black_box.ogg"
        self.pew_path = "sound/effects/pew.ogg"
        self.explosion_path = "sound/effects/explosion.ogg"

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 15 
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Alien settings
        self.max_aliens = 3
        self.aliens_to_hit = 10

        # Scoring settings
        self.alien_points = 50

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.point_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change during gameplay."""
        self.ship_speed = 5
        self.bullet_speed = 7
        self.alien_speed = 2

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.point_scale)
