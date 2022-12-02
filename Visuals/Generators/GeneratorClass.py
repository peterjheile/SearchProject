from random import randint
import math
import sys 
sys.path.append("Intersection")
from AllLocations.IntersectionClass import Intersection
from AllLocations.LocationClass import Location


class Generator:
    
    @classmethod
    def generateAllIntersections(self,xRange,yRange,allLocations,bottom = 10, top = 20):
        allIntersections = []
        for _ in range(randint(bottom,top)):
            randomPoints = (allLocations[randint(0,len(allLocations)-1)],allLocations[randint(0,len(allLocations)-1)],allLocations[randint(0,len(allLocations)-1)])
            intersectionCoords = (sum([point.x for point in randomPoints])/3,sum([point.y for point in randomPoints])/3)     
            allIntersections.append(Intersection(xRange, yRange, False,intersectionCoords[0],intersectionCoords[1])) 
        return allIntersections   

    @classmethod
    def generateAllDestinations(self,xRange,yRange):
        return [Location(xRange,yRange,True) for _ in range(2)]

    @classmethod
    def generateAllLocations(self,xRange,yRange,bottom = 20, top = 30):
        return [Location(xRange,yRange) for _ in range(randint(bottom,top))]

    @classmethod
    def generateAllRoads(self,allLocations):
        def findClosestLocations(location,count,allLocations):
            allClosest = []
            index = 0
            while index < count:
                closest = allLocations[0] if allLocations[0] != location else allLocations[1]
                distance = math.dist((closest.x,closest.y),(location.x,location.y))

                #gets the closest location
                for loc in allLocations:
                    # print(type(loc))
                    if math.dist((location.x,location.y),(loc.x,loc.y))<distance and location!=loc and loc not in allClosest and loc not in location.connections:
                        closest = loc
                        distance = math.dist((location.x,location.y),(loc.x,loc.y))

                allClosest.append(closest)
                index+=1
            return allClosest

        for location in allLocations:
            closest = findClosestLocations(location,randint(2,3)-len(location.connections),allLocations)
            for each in closest:
                if each not in location.connections:
                    location.connections.append(each)
                    each.connections.append(location)
