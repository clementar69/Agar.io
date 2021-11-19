import core
from pygame import Vector2
import pygame
import random

from Creep import Creep
from Joueur import Joueur


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [1600, 900]

    core.memory("centredecercle", Vector2(100, 200))
    core.memory("rayonducercle", 12)
    core.memory("couleurducercle", (255, 0, 0))

    core.memory("direction" ,Vector2(0, 0))
    core.memory("Fx", 0)
    core.memory("Ux", 0)
    core.memory("l", 0)
    core.memory("l0", 0.2)

    core.memory("L", 0)
    core.memory("Joueur", Joueur())
    core.memory("joueur",[])

    core.memory("Creep", "Creep_n°")
    core.memory("TableauDeCreeps", [])
    for i in range(100):
        core.memory("TableauDeCreeps").append(Creep())

    core.memory("Joueur").append(Joueur())

    print("Setup END-----------")


def run():
    core.cleanScreen()

    core.memory("Joueur").deplacement(core.getKeyPressList(pygame.K_z),core.getKeyPressList(pygame.K_s),
                core.getKeyPressList(pygame.K_q),core.getKeyPressList(pygame.K_d) )
    core.memory("Joueur").draw(core.screen)

    if core.getKeyPressList(pygame.K_r):
        core.memory("direction", Vector2(0, 0))


    if core.getKeyPressList(pygame.K_z):
       core.memory("direction", Vector2(core.memory("direction").x, -1))
    if core.getKeyPressList(pygame.K_s):
       core.memory("direction", Vector2(core.memory("direction").x, 1))
    if core.getKeyPressList(pygame.K_q):
       core.memory("direction", Vector2(-1, core.memory("direction").y))
    if core.getKeyPressList(pygame.K_d):
       core.memory("direction", Vector2(1, core.memory("direction").y))
    if core.memory("centredecercle").y  < 0  or core.memory("centredecercle").y > core.WINDOW_SIZE[1]:
       core.memory("direction", Vector2(core.memory("direction").x, core.memory("direction").y*0))

    if core.memory("centredecercle").x < 0 or core.memory("centredecercle").x > core.WINDOW_SIZE[0]:
       core.memory("direction", Vector2(core.memory("direction").x*0, core.memory("direction").y ))


    core.memory("centredecercle", core.memory("direction")+core.memory("centredecercle"))

    if core.getMouseLeftClick() is not None:
        core.memory("Ux", core.getMouseLeftClick() - core.memory("centredecercle"))
        core.memory("l", core.memory("Ux").length())
        core.memory("Ux", core.memory("Ux").normalize())
        core.memory("L", abs(core.memory("l") - core.memory("l0")))

    else:
        core.memory("Ux",Vector2(0, 0))

    for i in core.memory("TableauDeCreeps"):
        pygame.draw.circle(core.screen, i.couleur, i.position ,i.rayon)


    core.memory("Fx", core.memory("Ux"))
    core.memory("direction", core.memory("Fx"))
    core.memory("centredecercle", core.memory("direction") + core.memory("centredecercle"))
    pygame.draw.circle(core.screen, core.memory("couleurducercle"), core.memory("centredecercle"),
                       core.memory("rayonducercle"))

    for i in core.memory("TableauDeCreeps"):
        if i.position.distance_to(core.memory("centredecercle")) < (core.memory("rayonducercle") +i.rayon):
            i.mourir()
            core.memory("rayonducercle", core.memory("rayonducercle")+1)

    for i in core.memory("Joueur"):
        if i.position.distance_to(core.memory("centredecercle")) < (core.memory("rayonducercle") + i.rayon):
            core.memory("rayonducercle", core.memory("rayonducercle") /1.4)






core.main(setup, run)