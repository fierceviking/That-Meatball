from turtle import Screen
import pygame
from settings import Settings
from bullet import Bullet
 
class Player:
 
    def __init__(self, ai_game):
        self.settings = Settings()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/meatball.png')
        self.image = pygame.transform.scale(self.image,(75,75))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
        self.meatball_rect = self.standing_surface.get_rect(center=(self.x_position, self.y_position))
        self.jump_height = 20
        self.y_velocity = self.jump_height

        self.standing_surface = pygame.transform.scale(pygame.image.load("meatball.png"), (200, 200))
        self.jumping_surface = pygame.transform.scale(pygame.image.load("meatball.png"), (200, 200))
        self.background = pygame.transform.scale(pygame.image.load("Background.jpg"), (1920,1080))

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
        
        if jumping:
            self.y_position -= y_velocity
            y_velocity -= self.y_gravity
        if y_velocity < -self.jump_height:
            jumping = False
            y_velocity = Settings.jump_height
            self.meatball_rect = self.jumping_surface.get_rect(center=(self.x_position, self.y_position))
            self.screen.blit(self.jumping_surface, self.meatball_rect)
        else:
            self.meatball_rect = self.standing_surface.get_rect(center=(self.x_position, self.y_position))
            self.screen.blit(self.standing_surface, self.meatball_rect)

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)