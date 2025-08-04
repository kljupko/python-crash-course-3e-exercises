from pathlib import Path
import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statictics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Load the high score from the save file."""
        path = Path(self.settings.score_path)
        if not path.exists():
            return 0

        content = path.read_text()
        score = json.loads(content)
        return int(score)

    def save_high_score(self):
        """Save the high score to the save file."""
        path = Path(self.settings.score_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        content = json.dumps(self.high_score)
        
        path.write_text(content)
