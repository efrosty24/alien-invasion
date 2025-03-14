import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        '''Initialize button attributes'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (11, 194, 118)
        self.text_color = (4, 47, 9)
        self.font = pygame.font.Font("assets/invasion.otf", 40)

        # Build the buttons's rect object and center it.

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # the button message needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        '''Turn msg into a rendered image and center text on the button'''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class GameOver:
    def __init__(self, ai_game, msg):
        '''Initialize game over message attributes'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the game over message
        self.width, self.height = 400, 100
        self.button_color = (198, 24, 15) # red
        self.text_color = (255, 226, 224)
        self.font = pygame.font.Font("assets/invasion.otf", 40)

        # Build the game over message's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center 

        # The game over message needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        '''Turn msg into a rendered image and center text on the rect'''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_game_over(self):
        '''Draw game over message to the screen'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)