import pygame
from pygame import mixer

class Audio:
    """A class that handles music and sound effects."""

    def __init__(self, ai_game):
        """Loads the required resources for playing sound."""
        self.settings = ai_game.settings

        # Initialize the mixer.
        mixer.init()

        # Load the background music.
        mixer.music.load(self.settings.music_path)

        # Load the sound effects.
        self.pew_sound = mixer.Sound(self.settings.pew_path)
        self.explosion_sound = mixer.Sound(self.settings.explosion_path)
        self.explosion_sound.set_volume(0.2)

    def play_music(self):
        """Play the background music."""
        mixer.music.stop()
        mixer.music.rewind()
        # Play the music, loop indefinitely
        mixer.music.play(loops=-1)

    def play_pew(self):
        """Play the sound when the bullet fires."""
        self.pew_sound.play()

    def play_explosion(self):
        """Play the sound when a ship or alien is destroyed."""
        self.explosion_sound.play()
