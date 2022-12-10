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

    def heuristic1(point_s,point_g):
        # a basic heuristic that uses euclidean distance, returns a float
        return math.dist((point_s-point_g)**2 + (point_s-point_g)**2)
    #--------------------------------

    def heuristic2(a,b):
        # Manhattan distance on a square grid
        return abs(a.x - b.x) + abs(a.y - b.y)

    #-----------------------------------------
    def f_value(point_s,nextPoint,destination1,destination2):
        return point_s.cost(nextPoint)+Algorithms.hueristic(nextPoint,destination1,destination2)
    #--------------------------------
    @classmethod
    def AStarSearch(self, point, destination1, destination2, maxDepth= 10):
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
    def greedySearch(self, point, destination1, destination2, depth = 0, maxDepth = 30):
        destination1Found = False
        destination2Found = False

        def findClosest(point, fringe,path):
            lowest = fringe[0]
            for node in fringe[1:]:
                if lowest.cost(node) < point.cost(lowest) and (lowest not in path):
                    lowest = node
            print(lowest)
            return fringe.index(lowest)

        fringe = [point]
        path = []
        while fringe and depth < maxDepth:
            print("calculating")

            if not(path):
                node = fringe.pop(findClosest(point,fringe,path))
            else: 
                node = fringe.pop(findClosest(path[len(path)-1],fringe,path))
            path.append(node)
            if node == destination1:
                destination1Found == True
            elif node == destination2:
                destination2Found == True

            print(fringe,destination1Found,destination2Found)
            if destination1 and destination2:
                return path
            fringe = fringe + node.connections
            depth += 1
            print(len(fringe))

        return "No Path Found"



    #--------------------------------
    #--------------------------------
    @classmethod
    def MarkovSearch(self, point, destination1, destination2):
        pass

    #--------------------------------
    #--------------------------------
    @classmethod
    def DijkstrasSearch(self, spoint, destination1, destination2):
        
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = dict()
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = 0

        # while not frontier.empty():
        #     current = frontier.get()
            
        #     if current == goal:
        #         break
            
        #     for next in graph.neighbors(current):
        #         new_cost = cost_so_far[current] + graph.cost(current, next)
        #         if next not in cost_so_far or new_cost < cost_so_far[next]:
        #             cost_so_far[next] = new_cost
        #             priority = new_cost
        #             frontier.put(next, priority)
        #             came_from[next] = current

    
        

    #work code: kind of like greedy search where it choses the shortest path given. If a previous point is found and there is a path which is 'cheaper',
        #use that to get the path
    
    

    """
    function Dijkstra(Graph, source):
        for each vertex v in Graph:	// Initialization
            dist[v] := infinity	// initial distance from source to vertex v is set to infinite
          	previous[v] := undefined	// Previous node in optimal path from source
	    dist[source] := 0	// Distance from source to source
	    Q := the set of all nodes in Graph	// all nodes in the graph are unoptimized - thus are in Q
	    while Q is not empty:	// main loop
	        u := node in Q with smallest dist[ ]
	        remove u from Q
	        for each neighbor v of u:	// where v has not yet been removed from Q.
	            alt := dist[u] + dist_between(u, v)
	            if alt < dist[v]	// Relax (u,v)
                    dist[v] := alt
	                previous[v] := u
	    return previous[ ]
    """