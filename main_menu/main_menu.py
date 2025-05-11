import pygame
import os
from game import Game

# Load assets
START_BUTTON_IMAGE = pygame.image.load(os.path.join("game_assets", "button_play.png")).convert_alpha()
LOGO_IMAGE = pygame.image.load(os.path.join("game_assets", "logo.png")).convert_alpha()
BACKGROUND_IMAGE = pygame.image.load(os.path.join("game_assets", "bg.png"))

class MainMenu:
    def __init__(self, win):
        self.win = win
        self.width, self.height = win.get_size()
        self.background = pygame.transform.scale(BACKGROUND_IMAGE, (self.width, self.height))
        self.start_button_rect = pygame.Rect(
            self.width // 2 - START_BUTTON_IMAGE.get_width() // 2,
            350,
            START_BUTTON_IMAGE.get_width(),
            START_BUTTON_IMAGE.get_height()
        )

    def run(self):
        running = True
        while running:
            self.handle_events()
            self.draw()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if self.start_button_rect.collidepoint(pygame.mouse.get_pos()):
                    game = Game(self.win)
                    game.run()
                    del game  # optional in Python, but safe for resource management

    def draw(self):
        self.win.blit(self.background, (0, 0))
        self.win.blit(LOGO_IMAGE, (self.width // 2 - LOGO_IMAGE.get_width() // 2, 0))
        self.win.blit(START_BUTTON_IMAGE, self.start_button_rect.topleft)
        pygame.display.update()
