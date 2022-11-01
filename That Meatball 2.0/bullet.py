import pygame
import math

class Bullet:
    def __init__(self, x, y):
        self.pos = (x, y)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.dir = (mouse_x - x, mouse_y - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.bullet = pygame.Surface((7, 2)).convert_alpha()
        self.bullet.fill((255, 255, 255))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 2

    def update(self):  
        self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                    self.pos[1]+self.dir[1]*self.speed)

    def draw(self, surf):
        bullet_rect = self.bullet.get_rect(center = self.pos)
        surf.blit(self.bullet, bullet_rect)