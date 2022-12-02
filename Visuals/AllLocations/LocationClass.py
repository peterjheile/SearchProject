import pygame
from random import randint
import math

class Location:
    #this creates the information to draw a block that 
    #represents a house/location on the map
    def __init__(self,xRange,yRange, destination = False, start = False):
        self.canChange = True
        self.destination = destination
        self.start = start
        self.width = 30
        self.height = self.width
        self.color = (200,250,0) if self.destination else (0,0,0)
        if self.start: self.color = (255,0,0)
        self.x = randint(0,xRange-self.width)
        self.y = randint(0,yRange - self.height)
        self.connections = []

    def addConnection(self,other):
        self.connections.append(other)

    def draw(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height))

    def cost(self,location):
        return math.dist((self.x,self.y),(location.x,location.y))