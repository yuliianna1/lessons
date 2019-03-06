import pygame, sys
from settings import Settings
from ship import Ship
import game_functions as g_f

def init_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width, game_settings.height))
    ship = Ship(screen)
    pygame.display.set_caption("The best game in the world")

    while True:
        g_f.check_events(ship)
        g_f.update_screen(screen, game_settings, ship)

init_game()