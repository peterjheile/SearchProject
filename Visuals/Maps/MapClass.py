import pygame 
import sys
import copy
sys.path.append("Generator")
sys.path.append("Location")
from AllLocations.LocationClass import Location
from Generators.GeneratorClass import Generator


class Map:
    def __init__(self,width = 800, height = 650):
        self.width = 3000
        self.height = 2500
        self.x = 0
        self.y = 0
        self.color = (0,100,0)
        self.zoom = 1
        self.allow = True
        self.allLocations = []
        self.startLocation = Location(self.width,self.height,False, True)
        self.destination1,self.destination2 = tuple(Generator.generateAllDestinations(self.width,self.height))
        self.allLocations.append(self.startLocation)
        self.allLocations.append(self.destination1)
        self.allLocations.append(self.destination2)
        self.allLocations += Generator.generateAllLocations(self.width,self.height)
        self.allLocations += Generator.generateAllIntersections(self.width,self.height,self.allLocations)
        Generator.generateAllRoads(self.allLocations)

        self.pathFound = []


    def drawMap(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height))
        for location in self.allLocations:
            location.draw(display)
        self.drawRoads(display)

    def drawRoads(self,display):
        for location in self.allLocations:
            for other in location.connections:
                pygame.draw.line(display,(0,0,0),(location.x,location.y),(other.x,other.y),width = 1)

        for index in range(len(self.pathFound)-1):
            location = self.pathFound[index]
            next = self.pathFound[index+1]
            pygame.draw.line(display,(255,0,0),(location.x,location.y),(next.x,next.y),width = 3)

    def draw(self,display):
        self.drawMap(display)

