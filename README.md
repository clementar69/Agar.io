import random
import pygame
from pygame.math import Vector2
import core
from Creep import Creep


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [1080, 720]

    core.memory("centredecercle", Vector2(100, 200))
    core.memory("rayonducercle", 12)
    core.memory("couleurducercle", (255, 0, 0))

    core.memory("direction" ,Vector2(0, 0))
    core.memory("Fx", 0)
    core.memory("Ux", Vector2(0, 0))
    core.memory("l", 0)
    core.memory("l0", 10)
    core.memory("L", 0)

    core.memory("Creep", "Creep_n°")
    core.memory("TableauDeCreeps", [])
    for i in range(100):
        core.memory("TableauDeCreeps").append(Creep())
    print("Setup END-----------")


def run():
    core.cleanScreen()
    pygame.draw.circle(core.screen, core.memory("couleurducercle"), core.memory("centredecercle"), core.memory("rayonducercle"))

    if core.getKeyPressList(pygame.K_r) :
        core.memory("direction", Vector2(0, 0))


    if core.getKeyPressList(pygame.K_z) :
       core.memory("direction", Vector2(core.memory("direction").x, -1))
    if core.getKeyPressList(pygame.K_s) :
       core.memory("direction", Vector2(core.memory("direction").x, 1))
    if core.getKeyPressList(pygame.K_q) :
       core.memory("direction", Vector2(-1, core.memory("direction").y))
    if core.getKeyPressList(pygame.K_d) :
       core.memory("direction", Vector2(1, core.memory("direction").y))
    if core.memory("centredecercle").y  < 0  or core.memory("centredecercle").y > core.WINDOW_SIZE[1] :
       core.memory("direction", Vector2(core.memory("direction").x, core.memory("direction").y*-1))
       core.memory("couleurducercle", (random.randint(0,255),random.randint(0,255), random.randint(0,255)))
    if core.memory("centredecercle").x < 0 or core.memory("centredecercle").x > core.WINDOW_SIZE[0]:
       core.memory("direction", Vector2(core.memory("direction").x*-1, core.memory("direction").y ))
       core.memory("couleurducercle", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

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
        print(Creep().position)

    core.memory("Fx", 0.00025 * (core.memory("L") * core.memory("Ux")))
    core.memory("direction", core.memory("direction") + core.memory("Fx"))
    core.memory("centredecercle", core.memory("direction") + core.memory("centredecercle"))

core.main(setup, run)
