import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().width
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_aliens()
        
        self.game_active = True

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

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
    
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

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullest that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.settings.screen_width:
               self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        """Check if any aliens are hit. Create new alien."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if collisions:
            print(len(collisions))
            self.stats.aliens_hit += len(collisions)
            print(f"Hit {self.stats.aliens_hit} of "
                f"{self.settings.aliens_to_kill} aliens.")
            if self.stats.aliens_hit >= self.settings.aliens_to_kill:
                print("You win!")
                self.game_active = False
            else:
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

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
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
        else:
            print("Game over!")
            self.game_active = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
