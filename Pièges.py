################################################# ###############################
# Écrit par : Clément ARCHIMBAUD et Samuel  #
# Me contacter : clement.archimbaud@etu.univ-lyon1.fr #
# Objectif : classe Pièges du jeu Agar.io #
# Version : v4 #
################################################# ###############################

import random


import pygame
from pygame import Vector2
screen = None

class Pieges:
    def __init__(self):
        self.rayon=12
        self.couleur=(0, 255, 40)
        self.position=Vector2(random.randint(0, 1600), random.randint(0, 900))
        self.direction = Vector2(0, 0)


    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position,self.rayon)

    def mourir (self):
        self.couleur = (0, 255, 0)
        self.position = Vector2(random.randint(0, 1600), random.randint(0, 900))

