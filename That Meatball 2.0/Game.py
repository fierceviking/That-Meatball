import sys
from turtle import pos
import pygame

from bullet import Bullet
from settings import Settings

class ThatMeatball:
    """variables start"""
    player_x = 0
    player_y = 0
    moving_right = False
    moving_left = False
    shooting = False
    jumping = False
    bullets = []
    pos = player_x, player_y
    """variables end"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()


        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("That Meatball")

        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            """self._update_bullets()"""
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False

    def _fire_bullet(self):

        
        if len(self.bullets) < 100:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = ThatMeatball()
    ai.run_game()
