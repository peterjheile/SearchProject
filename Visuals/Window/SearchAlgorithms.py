##Here we will ahve each search algorithm that can be used code will be written in each
#function that is representative of what the search does 

# Note: each search function takes an input of only the starting point
# Location is given by x and y coordinated and can be obtained by point.x and point.y

# (x,y)

#THE LOCATIONS THAT A LOCATION IS CONNECTED TO CAN BE ACCESSED USING point.connections
#USING point.connections will return a list of other points that the location is connected to

#--------------------------------
import math
from queue import PriorityQueue
class Algorithms:

    def heuristic1(point_s,destination1,destination2):
        #this is a hueristic for the shortest distance ot the points, regardless of paths. This is also known as
        # "as the crow flies"
        if math.dist((point_s.x,point_s.y),(destination1.x,destination1.y))<math.dist((point_s.x,point_s.y),(destination2.x,destination2.y)):
            dist1 = math.dist((point_s.x,point_s.y),(destination1.x,destination1.y))
        else:
            dist1 = math.dist((point_s.x,point_s.y),(destination2.x,destination2.y))
        dist2 = math.dist((destination2.x,destination2.y),(destination1.x,destination1.y))
        return dist1+dist2
    #--------------------------------

    def heuristic2(a,b):
        # Manhattan distance on a square grid
        return abs(a.x - b.x) + abs(a.y - b.y)

    #--------------------------------
    @classmethod
    def AStarSearch(self, point, destination1, destination2):
        fringe = [point]










        frontier = PriorityQueue()
        x = point.x
        y = point.y
        start = (x,y)
        frontier.put(start, 0)
        came_from = dict()
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = 0
        goal = destination1

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break
            for next in point.connections:
                new_cost = cost_so_far[current] + next.cost(next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + Algorithms.heuristic1(goal.cost(goal),next.cost(next))
                    frontier.put(next, priority)
                    came_from[next] = current
            

    #--------------------------------
    #--------------------------------
    @classmethod
    def greedySearch(self, point, destination1, destination2):
        x = point.x
        y = point.y
        start = (x,y)
        goal = destination1
        
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = dict()
        came_from[start] = None

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break
            
            for next in graph.neighbors(current):
                if next not in came_from:
                    priority = Algorithms.heuristic1(goal.cost(), next.cost())
                    frontier.put(next, priority)
                    came_from[next] = current

    #--------------------------------
    #--------------------------------
    @classmethod
    def MarkovSearch(self, point, destination1, destination2):
        pass

    #--------------------------------
    #--------------------------------
    @classmethod
    def DijkstrasSearch(self, spoint, destination1, destination2):
        x = point.x
        y = point.y
        start = (x,y)
        goal = destination1
        
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = dict()
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()
            
            if current == goal:
                break
            
            for next in graph.neighbors(current):
                new_cost = cost_so_far[current] + graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    frontier.put(next, priority)
                    came_from[next] = current