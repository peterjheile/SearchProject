from random import randint
import sys
import math
sys.path.append("Map")
sys.path.append("Generators")
from Generators.GeneratorClass import Generator

from Maps.MapClass import Map
import copy


class Interactions:
    @classmethod
    def displaceScreen(Interactions,map,locations,displacement, all, zoom = 0):
        Interactions.zoom(map,zoom)
        map.x += displacement[0]
        map.y += displacement[1]
        for i in locations:
            i.x += displacement[0]
            i.y += displacement[1]

    @classmethod
    def zoom(self,map,zoom = 0):
        if zoom == 1:
            map.width = map.width*1.2
            map.height = map.height*1.2
            map.x = map.x*1.2
            map.y = map.y*1.2
            for i in map.allLocations:
                if i.canChange:
                    i.width = i.width*1.2
                    i.height = i.height*1.2
                i.x = i.x*1.2
                i.y = i.y*1.2

        elif (zoom == -1):
            map.width = map.width/1.2
            map.height = map.height/1.2
            map.x = map.x/1.2
            map.y = map.y/1.2
            for i in map.allLocations:
                if i.canChange:
                    i.width = i.width/1.2
                    i.height = i.height/1.2
                i.x = i.x/1.2
                i.y = i.y/1.2

    @classmethod
    def adjustMovements(self,zoom,map,movement):
        if zoom == 0:
            map.allowed = True
        if map.allowed:
            if zoom == 1:
                # print(zoom)
                map.zoom = map.zoom*1.2
                map.allowed = False
            elif zoom ==-1:
                # print(zoom)
                map.zoom = map.zoom/1.2
                map.allowed = False
        return movement*map.zoom


    @classmethod
    def calculatePath(self, parent, goalOne, goalTwo):
        pass


        


                
            


