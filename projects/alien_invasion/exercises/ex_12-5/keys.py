import sys

import pygame

class KeysDisplay:
    """A class that displays keypresses in pygame."""
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Keys Display")
    
    def run_logger(self):
        """The function that runs the keylogger (not malicious)."""
        
        while True:
            self._check_events()
            self.clock.tick(60)
    
    def _check_events(self):
        """Function that checks which keys are pressed, or if quitting."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event)

if __name__ == '__main__':
    # Make an instance of the logger and run it.
    kd = KeysDisplay()
    kd.run_logger()
