class GameStats:
    """Class to track game statistics."""
    
    def __init__(self, ai_game):
        """Initialize the stats."""
        self.settings = ai_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        """Reset the statistics."""
        self.ships_left = self.settings.ship_limit
        self.aliens_hit = 0
