import pygame, sys

def check_events(ship):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                ship.moving_right = True
            if i.key == pygame.K_LEFT:
                ship.moving_left = True
            if i.key == pygame.K_DOWN:
               ship.moving_bottom = True

            if i.key == pygame.K_UP:
                ship.moving_up = True
                ship.jump = True




        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_RIGHT:
                ship.moving_right = False
            if i.key == pygame.K_LEFT:
                ship.moving_left = False
            if i.key == pygame.K_DOWN:
                ship.moving_bottom = False




def update_screen(screen, game_settings, ship):
    pygame.display.flip()
    screen.fill(game_settings.bg_color)
    ship.blitme()
    ship.update()
