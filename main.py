import math
import random
import pygame

WIDTH, HEIGHT = 1200, 700

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Solar System")
CX, CY = WIDTH / 2, HEIGHT / 2

CAMX, CAMY = 0, 0

G = 6.67428e-11
AU = 149.9e9
SOLAR_MASS = 1.989e30
EARTH_MASS = 5.972e24

ZOOM = 8e-10
TIMESTEP = 2600*24

ORBIT_TRAIL_LENGTH = 600

OBJECTS = []


class Resources:
    font = pygame.font.SysFont('Consolas', 12)
    space_image = pygame.transform.scale(
        pygame.image.load("space.jpg").convert(),
        (WIDTH, WIDTH)
    )


class Object:
    def __init__(self, name, mass, x, y, r, c=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 vx = 0, vy = 0):
        self.name = name
        self.mass = mass
        self.x = x
        self.y = y
        self.r = r
        self.c = c
        self.vx = vx
        self.vy = vy

        OBJECTS.append(self)
