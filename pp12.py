import core
from pygame import Vector2
import pygame
import random

from Creep import Creep
from Ennemis import Ennemis
from Pièges import Pieges


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




    core.memory("Fx", core.memory("Ux"))
    core.memory("direction", core.memory("Fx"))
    core.memory("centredecercle", core.memory("direction") + core.memory("centredecercle"))
    pygame.draw.circle(core.screen, core.memory("couleurducercle"), core.memory("centredecercle"),
                       core.memory("rayonducercle"))

    for p in core.memory("TableauDePieges"):
        if p.position.distance_to(core.memory("centredecercle")) < (core.memory("rayonducercle") +p.rayon):
            p.mourir()
            core.memory("rayonducercle", core.memory("rayonducercle") - p.rayon)

    for i in core.memory("TableauDeCreeps"):
        if i.position.distance_to(core.memory("centredecercle")) < (core.memory("rayonducercle") +i.rayon):
            i.mourir()
            core.memory("rayonducercle", core.memory("rayonducercle")+0.2)

    for o in core.memory("TableauDEnnemis"):
        if o.position.distance_to(core.memory("centredecercle")) < (core.memory("rayonducercle") +o.rayon) and core.memory("rayonducercle") > o.rayon:

            o.mourir()
            core.memory("rayonducercle", core.memory("rayonducercle") + o.rayon/4)
    for o in core.memory("TableauDEnnemis"):
        if o.position.distance_to(core.memory("centredecercle")) < (core.memory("rayonducercle") +o.rayon) and core.memory("rayonducercle") < o.rayon or (core.memory("rayonducercle")<2) :
            pygame.draw.circle(core.screen, (0,0,0), (0,0), 9999)










core.main(setup, run)