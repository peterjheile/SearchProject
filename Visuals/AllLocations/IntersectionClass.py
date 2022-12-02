import pygame
from random import randint
import math

class Intersection:
    #this creates an intersection in the roads
    def __init__(self,xRange,yRange,destination = False,setx = None, sety = None):
        self.canChange = False
        self.destination = destination
        self.width = 5
        self.height = 5
        self.color = (0,0,255)
        self.x = randint(0,xRange-self.width) if setx == None else setx
        self.y = randint(0,yRange - self.height) if sety == None else sety
        self.connections = []

    def addConnection(self,other):
        self.connections.append(other)

    def draw(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height))

    def cost(self,location):
        return math.dist((self.x,self.y),(location.x,location.y))