import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from audio import Audio
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                self.settings.screen_height))
        pygame.display.set_caption("Sideways shooter")
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.audio = Audio(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_aliens()

        # Create the play button.
        self.play_button = Button(self, "Play")
        
        self.game_active = False

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            self.clock.tick(60)

# ----------------------------------------------------------------------
# EVENT HANDLING
# ----------------------------------------------------------------------
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._prepare_quit_game()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mousedown_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_q:
            self._prepare_quit_game()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _check_mousedown_events(self, event):
        """Respond to mouse clicks."""
        mouse_pos = pygame.mouse.get_pos()
        self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Respond to clicking the play button."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self._start_game()

# ----------------------------------------------------------------------
# GAME FLOW CONTROL
# ----------------------------------------------------------------------
    def _start_game(self):
        """Prepare the game for play."""
        if self.game_active:
            return None
        
        # Reset the game statistics and settings.
        self.stats.reset_stats()
        self.settings.initialize_dynamic_settings()
        self.sb.prep_scoreboard()

        # Get rid of remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship.
        self._create_aliens()
        self.ship.center_ship()

        # Set up the display.
        pygame.mouse.set_visible(False)

        # Set up the audio
        self.audio.play_music()

        # Start the game.
        self.game_active = True

    def _end_game(self):
        """Clean up the game after winning or losing."""
        print("Game over!")
        pygame.mouse.set_visible(True)
        self.game_active = False

    def _prepare_quit_game(self):
        """Save the high score to the file."""
        self.stats.save_high_score()

# ----------------------------------------------------------------------
# ENTITY MANAGEMENT
# ----------------------------------------------------------------------

#   CREATION
#   --------
    def _create_aliens(self):
        """Creates an alien at a random spot on the right."""
        x_position = self.settings.screen_width
        while len(self.aliens) < self.settings.max_aliens:
            alien = Alien(self)
            alien.x  = x_position - alien.rect.width
            self.aliens.add(alien)
            x_position -= 3 * alien.rect.width

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.audio.play_pew()

#   UPDATING
#   --------
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullest that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.settings.screen_width:
               self.bullets.remove(bullet)
               self._create_aliens()
    
    def _update_aliens(self):
        """Move the aliens to the left."""
        for alien in self.aliens.sprites().copy():
            if alien.check_edge():
                self._ship_hit()
        
        if self.game_active:
            self._create_aliens()
            self.aliens.update()
        
        # Look for collisions with the ship.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_bullet_alien_collisions()

#   COLLISION CHECK
#   ---------------
    def _check_bullet_alien_collisions(self):
        """Check if any aliens are hit. Create new alien."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if collisions:
            self._alien_hit(collisions)

#   COLLISION RESPONSE
#   ------------------
    def _alien_hit(self, collisions):
        """Respond to aliens being hit by bullets."""
        self.audio.play_explosion()
        
        self.stats.aliens_hit += len(collisions)
        
        for aliens in collisions.values():
            self.stats.score += self.settings.alien_points * len(collisions)
        self.sb.prep_score()
        self.sb.check_high_score()

        if self.stats.aliens_hit >= self.settings.aliens_to_hit:
            self.stats.aliens_hit = self.stats.aliens_hit % 10
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        self.audio.play_explosion()

        if self.stats.ships_left <= 0:
            self._end_game()
            return None

        # Decrement ships_left.
        self.stats.ships_left -= 1
        self.stats.aliens_hit = 0
        print(f"You have {self.stats.ships_left} lives left.")
            
        # Get rid of any remaining aliens and bullets.
        self.bullets.empty()
        self.aliens.empty()
            
        # Create 3 new aliens and center the ship.
        self._create_aliens()
        self.ship.center_ship()
            
        # Pause
        sleep(0.5)

# ----------------------------------------------------------------------
# DISPLAY MANAGEMENT
# ----------------------------------------------------------------------
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()

        # Draw the scoreboard.
        self.sb.show_score()

        # Draw the play button
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

# ----------------------------------------------------------------------
# RUN THE GAME
# ----------------------------------------------------------------------
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
