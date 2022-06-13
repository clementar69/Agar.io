import random

import pygame
from pygame import Vector2

class Pieges:
    def __init__(self):
        self.rayon=12
        self.couleur=(0, 255, 40)
        self.position=Vector2(random.randint(0, 1600), random.randint(0, 900))
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

    def mourir (self):
        self.couleur = (0, 255, 0)
        self.position = Vector2(random.randint(0, 1600), random.randint(0, 900))
