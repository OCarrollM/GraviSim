import numpy as np
import pygame

TIME_DELAY = 0.0005 # Makes simulation actually visible

class Body:
    def __init__(self, position_array, mass, colour, radius=10):
            self.velocity = np.array([[0, 0, 0]])
            self.force = np.array([[0, 0, 0]])
            self.mass = mass
            self.position = position_array
            self.radius = radius
            self.thickness = self.radius * 2
            self.colour = colour
            
def draw(self, surface):
    pygame.draw.circle(surface, self.colour, (self.position[0][0], self.position[0][1]), self.radius, self.thickness)
    
def add_velocity(self, velocity_array):
    self.velocity = self.velocity + velocity_array
    
def add_force(self, force_array):
    self.force = self.force + force_array
    
def move(self):
    self.velocity = self.velocity + ((self.force / self.mass) * TIME_DELAY)
    self.position = self.position + self.velocity * TIME_DELAY