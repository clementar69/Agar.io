################################################# ###############################
# Écrit par : Clément ARCHIMBAUD et Samuel Marquat #
# Me contacter : clement.archimbaud@etu.univ-lyon1.fr #
# Objectif : Cree le jeu Agar.io #
# Version : v4 #
################################################# ###############################


import core
from pygame import Vector2
import pygame
import random

from Creep import Creep
from Ennemis import Ennemis
from Pièges import Pieges
import time


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [1600, 900]
    core.bgColor=(255,255,255)

    core.memory("centredecercle", Vector2(100, 200))
    core.memory("rayonducercle", 12)
    core.memory("couleurducercle", (255, 0, 0))

    core.memory("direction" ,Vector2(0, 0))
    core.memory("Fx", 0)
    core.memory("Ux", 0)
    core.memory("l", 0)
    core.memory("l0", 0.2)

    core.memory("Score",0)
    core.memory("defaite",0)

    core.memory("L", 0)
    core.memory("Ennemis", Ennemis())
    core.memory("TableauDEnnemis",[])
    for o in range(5):
        core.memory("TableauDEnnemis").append(Ennemis())

    core.memory("Pieges",Pieges())
    core.memory("TableauDePieges",[])
    for p in range(2):
        core.memory("TableauDePieges").append(Pieges())

    core.memory("TableauDeCreeps", [])
    for i in range(100):
        core.memory("TableauDeCreeps").append(Creep())




    print("Setup END-----------")


def run():
    core.cleanScreen()




    for o in core.memory("TableauDEnnemis"):
        pygame.draw.circle(core.screen, o.couleur, o.position ,o.rayon)

    for i in core.memory("TableauDeCreeps"):
        pygame.draw.circle(core.screen, i.couleur, i.position, i.rayon)

    for p in core.memory("TableauDePieges"):
        pygame.draw.circle(core.screen, p.couleur, p.position, p.rayon)


    if core.getKeyPressList(pygame.K_r):
        core.memory("direction", Vector2(0, 0))



    if core.memory("centredecercle").y  < 0  or core.memory("centredecercle").y > core.WINDOW_SIZE[1]:
       core.memory("direction", Vector2(core.memory("direction").x, core.memory("direction").y*0))

    if core.memory("centredecercle").x < 0 or core.memory("centredecercle").x > core.WINDOW_SIZE[0]:
       core.memory("direction", Vector2(core.memory("direction").x*0, core.memory("direction").y ))


    core.memory("centredecercle", core.memory("direction")+core.memory("centredecercle"))

    if core.memory("defaite")<1:
        if core.getMouseLeftClick() is not None:
            core.memory("Ux", core.getMouseLeftClick() - core.memory("centredecercle"))
            core.memory("l", core.memory("Ux").length())
            core.memory("Ux", core.memory("Ux").normalize())
            core.memory("L", abs(core.memory("l") - core.memory("l0")))

        else:
            core.memory("Ux",Vector2(0, 0))

    else:
        core.memory("Ux", Vector2(0, 0))

    core.memory("Fx", core.memory("Ux"))
    core.memory("direction", core.memory("Fx"))
    core.memory("centredecercle", core.memory("direction") + core.memory("centredecercle"))
    pygame.draw.circle(core.screen, core.memory("couleurducercle"), core.memory("centredecercle"),
                       core.memory("rayonducercle"))
#Pièges
    for p in core.memory("TableauDePieges"):
        if p.position.distance_to(core.memory("centredecercle")) < (core.memory("rayonducercle") +p.rayon):
            p.mourir()
            core.memory("rayonducercle", core.memory("rayonducercle")/2)
#Manger des Creeps
    for i in core.memory("TableauDeCreeps"):
        if i.position.distance_to(core.memory("centredecercle")) < (core.memory("rayonducercle") +i.rayon):
            i.mourir()
            core.memory("rayonducercle", core.memory("rayonducercle")+0.2)
            core.memory("Score",core.memory("Score")+1)
#Manger des Ennemis
    for o in core.memory("TableauDEnnemis"):
        if o.position.distance_to(core.memory("centredecercle")) < (core.memory("rayonducercle") +o.rayon) and core.memory("rayonducercle") > o.rayon:

            o.mourir()
            core.memory("rayonducercle", core.memory("rayonducercle") + o.rayon/4)
            core.memory("Score", core.memory("Score") + o.rayon)

#Score

    core.Draw.text((255,0,0), f'Score : {core.memory("Score")}', [10, 10])


#Game over
    for o in core.memory("TableauDEnnemis"):
        if o.position.distance_to(core.memory("centredecercle")) < (core.memory("rayonducercle") +o.rayon) and core.memory("rayonducercle") < o.rayon or (core.memory("rayonducercle")<10) :
            pygame.draw.circle(core.screen, (0,0,0), (0,0), 9999)
            core.Draw.text((255, 0, 0), f'Score : {core.memory("Score")}', [700, 400])
            core.Draw.text((255, 0, 0), f'GameOver ' ,[700, 300])
            core.Draw.text((255, 0, 0), f'Press "r" pour quitter ', [650, 500])
            core.memory("direction", Vector2(0, 0))
            core.memory("defaite",core.memory("defaite")+2)

            if core.getKeyPressList("r"):
                pygame.quit()













core.main(setup, run)
