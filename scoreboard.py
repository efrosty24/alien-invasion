import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    '''A class to report scoring information'''

    def __init__(self, ai_game):
        '''Initialize scorekeeping attributes'''
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for the scoring information
        self.text_color = (250, 236, 226) # soft white
        self.font = pygame.font.Font("assets/invasion.otf", 30)
        self.end_game_text_color = (255, 226, 224) # soft pink

        # Prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.prep_game_over()

    def prep_ships(self):
        '''Show how many ships are left'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = self.screen_rect.width - ship.rect.width - ship_number * ship.rect.width - 10
            ship.rect.y = self.screen_rect.height // 100
            self.ships.add(ship)

    def prep_level(self):
        '''Turn the level into a rendered image'''
        level_str = str(self.stats.level)
        self.level_image = self.font.render(f'Level: {level_str}', True, self.text_color, self.settings.bg_color)

        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.score_rect.left
        self.level_rect.top = self.score_rect.bottom + 5

    def prep_high_score(self):
        '''Turn the high score into a rendered image'''
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(f'High Score: {high_score_str}', True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.height // 100

    def prep_score(self):
        '''Turn the score into a rendered image'''
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(f'Score: {score_str}', True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = self.screen_rect.height // 100

    def prep_game_over(self):
        '''Turn the game over message into a rendered image'''
        game_over_str = "Game Over"
        self.game_over_image = self.font.render(game_over_str, True, self.end_game_text_color, self.settings.bg_color)

        # Center the game over message
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.center = self.screen_rect.center

    def show_score(self):
        '''Draw score to the screen'''
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

        if not self.stats.game_active and self.stats.ships_left == 0:
            self.screen.fill(self.settings.bg_color)
            self.screen.blit(self.game_over_image, self.game_over_rect)

    def check_high_score(self):
        '''Check to see if there is a new high score'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

