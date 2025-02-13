import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Managing game assets and behanvior'''

    def __init__(self):
        '''Initializing game and creating game resources'''

        pygame.init()

        
        pygame.display.set_caption("Alien Invasion")

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)

    def run_game(self):
        '''Start main loop for the game'''

        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        '''Respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        '''update images on the screen and flip to another screen'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Making a game instance and running the game
    ai = AlienInvasion()
    ai.run_game()




