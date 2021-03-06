################################################# ###############################
# Écrit par : Clément ARCHIMBAUD et Samuel Marquat #
# Me contacter : clement.archimbaud@etu.univ-lyon1.fr #
# Objectif : classe Creep du jeu Agar.io #
# Version : v4 #
################################################# ###############################

import random
from pygame import Vector2

class Creep:

    def __init__(self):
        self.rayon = 3
        self.couleur = (random.randint(20, 215), random.randint(20, 215), random.randint(20, 215))
        self.position = Vector2(random.randint(0, 1600), random.randint(0, 900))

    def mourir (self):
        self.couleur = (random.randint(20, 215), random.randint(20, 215), random.randint(20, 215))
        self.position = Vector2(random.randint(0, 1600), random.randint(0, 900))

