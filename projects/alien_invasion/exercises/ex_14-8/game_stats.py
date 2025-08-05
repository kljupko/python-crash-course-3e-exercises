from pathlib import Path
import json

class GameStats:
    """Class to track game statistics."""
    
    def __init__(self, ai_game):
        """Initialize the stats."""
        self.settings = ai_game.settings
        self.high_score = self.load_high_score()
        self.reset_stats()
    
    def reset_stats(self):
        """Reset the statistics."""
        self.ships_left = self.settings.ship_limit
        self.aliens_hit = 0
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Load the high score from the file."""
        path = Path(self.settings.score_path)
        if not path.exists():
            return 0

        content = path.read_text()
        return json.loads(content)

    def save_high_score(self):
        """Save the high score to the file."""
        path = Path(self.settings.score_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        content = json.dumps(self.high_score)

        path.write_text(content)
        return None
