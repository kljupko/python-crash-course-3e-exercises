import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from raindrop import Raindrop

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

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.raindrops = pygame.sprite.Group()

        self._create_fleet()
        self._create_raindrops()

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_raindrops()
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
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
               self.bullets.remove(bullet)

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room
        # left. Spacing between aliens is one alien width and height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            # Draw one row of aliens.
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_raindrops(self):
        """Check if droplet is at the bottom, remove, then update."""
        for droplet in self.raindrops.sprites().copy():
            if droplet.check_bottom():
                at_bottom = True
                self.raindrops.remove(droplet)
        
        # Check if there's room for new row.
        # Get highest droplet. Start by assigning lowest one.
        highest = self.raindrops.sprites()[-1]
        for droplet in self.raindrops.sprites():
            # Loop through the droplets, find highest one.
            if droplet.y < highest.y:
                highest = droplet
        
        # If there is room for a new row, add it.
        if highest.y > highest.rect.height * 2:
            self._create_raindrops_row(0, 0)
        # Update raindrops.
        self.raindrops.update()

    def _create_raindrops(self):
        # Create a droplet and keep adding until there's no room left.
        droplet = Raindrop(self)
        droplet_width, droplet_height = droplet.rect.size
        
        current_x, current_y = 0, 0
        while current_y < self.settings.screen_height:
            # Create a row of raindrops
            self._create_raindrops_row(current_x, current_y)

            # Finished a row; reset x value, increment y value.
            current_x = 0
            current_y += 2 * droplet_height
            
    def _create_raindrops_row(self, x_position, y_position):
        """Create a row of raindrops."""
        droplet = Raindrop(self)
        droplet_width, droplet_height = droplet.rect.size
        while x_position < self.settings.screen_width:
                self._create_droplet(x_position, y_position)
                x_position += 2 * droplet_width

    def _create_droplet(self, x_position, y_position):
        """Create a raindrop and add it to the screen."""
        new_droplet = Raindrop(self)
        new_droplet.y = y_position
        new_droplet.rect.x = x_position
        new_droplet.rect.y = y_position
        self.raindrops.add(new_droplet)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the fleet and change direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        for bullet in self.bullets.sprites():
                bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
