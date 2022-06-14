################################################# ###############################
# Écrit par : Clément ARCHIMBAUD et Samuel  #
# Me contacter : clement.archimbaud@etu.univ-lyon1.fr #
# Objectif : classe Ennemie du jeu Agar.io #
# Version : v4 #
################################################# ###############################

import random

import pygame
from pygame import Vector2

class Ennemis:
    def __init__(self):
        self.rayon=(random.randint(12, 110))
        self.couleur=(255, 255, 0)
        self.position=Vector2(random.randint(0, 1600), random.randint(0, 900))
        self.direction = Vector2(0, 0)


    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position,self.rayon)

    def mourir (self):
        self.couleur = (255, 255, 0)
        self.position = Vector2(random.randint(0, 1600), random.randint(0, 900))
