# this class handles the movement and
# the collision detection of space objects

import pygame
import random


class Space:
    def __init__(self, is_earth, surface):

        # Initializes a space object.
        # - self is the space object to initialize
        # - center is the center of the object
        # - radius is the radius of the dot
        # - velocity is a list containing the x and y speed
        # - surface is the window's pygame.surface object

        self.surface = surface

        width, height = pygame.display.get_surface().get_size()

        if is_earth:
            self.center = (width/2, height/2)
            self.radius = 100
            self.velocity = (0,0)
            self.color = pygame.Color("blue")
        else:
            self.center = (random.randint(0, width), random.randint(0, height))
            self.velocity = (random.randint(1, 10), random.randint(1, 10))
            self.radius = random.randint(20, 30)
            self.color = pygame.Color("orange")

    def move(self):
        # changes the locations of the space object by adding the
        # x and y speed values to the x and y coordinates of the center

        self.center[0] += self.velocity[0]
        self.center[1] += self.velocity[1]

    def draw(self):
        # Draw the object on the surface
        # self is the space object
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)