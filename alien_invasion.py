import sys
import pygame
from settings import Settings

class AlienInvasion:
    '''Managing game assets and behanvior'''

    def __init__(self):
        '''Initializing game and creating game resources'''

        pygame.init()

        
        pygame.display.set_caption("Alien Invasion")

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    def run_game(self):
        '''Start main loop for the game'''

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

    
if __name__ == '__main__':
    # Making a game instance and running the game
    ai = AlienInvasion()
    ai.run_game()




