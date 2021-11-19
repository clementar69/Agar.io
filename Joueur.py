import random

import pygame
from pygame import Vector2

class Joueur:
    def __init__(self):
        self.rayon=12
        self.couleur=(255, 255, 0)
        self.position=Vector2(100, 200)
        self.direction = Vector2(0, 0)

    def deplacement(self,z,s,q,d):

        if z:
            self.direction = Vector2(self.direction.x, -1)
        if s:
            self.direction = Vector2(self.direction.x, 1)
        if q:
            self.direction = Vector2(-1, self.direction.y)
        if d:
            self.direction = Vector2(1, self.direction.y)
    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position,self.rayon)
