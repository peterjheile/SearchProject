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
import copy
class Algorithms:

    def heuristic1(point_s, dest1, dest2, dest1Found, dest2Found):
        # a basic heuristic that uses euclidean distance, returns a float
        if dest1Found:
            closest = math.dist((point_s.x,point_s.y),(dest2.x,dest2.y))
        elif dest2Found:
            closest = math.dist((point_s.x,point_s.y),(dest1.x,dest1.y))
        else: 
            closest = math.dist((point_s.x,point_s.y),(dest1.x,dest1.y)) if math.dist((point_s.x,point_s.y),(dest1.x,dest1.y)) < math.dist((point_s.x,point_s.y),(dest2.x,dest2.y)) else math.dist((point_s.x,point_s.y),(dest2.x,dest2.y))
        return closest

    #--------------------------------

    def heuristic2(point_s, dest1,dest2, path):
        # Manhattan distance on a square grid
        return 0

    #-----------------------------------------
    def f_value(point_s,nextPoint,destination1,destination2,dest1Found,dest2Found):
        return point_s.cost(nextPoint)+ Algorithms.heuristic1(nextPoint,destination1,destination2,dest1Found,dest2Found)
    #--------------------------------
    @classmethod
    def AStarSearch(self, start, destination1, destination2, dest1Found = False, dest2Found = False, depth = 0, path = [], maxDepth = 50):
        def lowestChildren(children,path):
            lowest = []
            lowCount = math.inf
            for child in children:
                if path.count(child)<lowCount:
                    lowCount = path.count(child)
            for child in children:
                if path.count(child) <= lowCount:
                    lowest.append(child)
            return lowest
        
        def calcBestF(parent, dest1,dest2,dest1Found,dest2Found,path):
            children = parent.connections.copy()
            if not(dest1Found) and not(dest2Found):
                children = lowestChildren(children,path)
            elif dest1Found:
                children = lowestChildren(children,path[path.index(destination1):])
            else:
                children = lowestChildren(children,path[path.index(destination2):])
            lowest,lNode = self.f_value(parent,children[0],dest1,dest2,dest1Found,dest2Found),children[0]
            for child in children[1:]:
                f = self.f_value(parent,child,dest1,dest2,dest1Found,dest2Found)
                #to-do: make sure the algorithm does not keep repeating
                if f < lowest:
                    lowest,lNode = f,child
            return lNode
        # if not(path):
        #     path = path.append(start)
        nextNode = calcBestF(start, destination1,destination2,dest1Found,dest2Found,path)
        if depth>=maxDepth:

            return ["No path Found"]
        if (dest1Found and nextNode == destination2) or (dest2Found and nextNode == destination1):
            return [nextNode]
        if start == destination1:
            dest1Found = True
        elif start == destination2:
            dest2Found = True
        depth = depth+1
        path = path+[nextNode]
        return [nextNode] + Algorithms.AStarSearch(nextNode,destination1,destination2,dest1Found,dest2Found,depth,path)
            

    #--------------------------------
    #--------------------------------
    @classmethod
    def greedySearch(self, start, destination1, destination2, maxDepth = 1000, depth = 0):
        def findClosestLeastNode(fringe,path,destination1,destination2):
            if destination1 in fringe and destination1 not in path:
                return destination1
            elif destination2 in fringe and destination2 not in path:
                return destination2
            leastNodes = []
            leastCount = math.inf
            for node in fringe:
                count = path.count(node)
                if count < leastCount:
                    leastCount = count
            for node in fringe:
                if path.count(node) <= count:
                    leastNodes.append(node)
            
            if len(leastNodes) == 1:
                return leastNodes[0]
            else:
                closest = leastNodes[0]
                for node in leastNodes[1:]:
                    if path.count(node)<path.count(closest):
                        closest = node
                return closest

        destination1Found = False
        destination2Found = False

        path = [start]
        fringe = start.connections.copy()

        while depth < maxDepth:
            nextNode = findClosestLeastNode(fringe, path,destination1,destination2)
            path.append(nextNode)
            # if nextNode == destination1 or nextNode == destination2:
            #     print("found destination")
            if nextNode == destination1:
                destination1Found = True
            if nextNode == destination2:
                destination2Found = True

            if destination1Found and destination2Found:
                return path

            fringe = nextNode.connections.copy()
            depth += 1
        return "none"


    #--------------------------------
    @classmethod
    def DijkstrasSearch(self, spoint, destination1, destination2):
        pass
        # frontier = PriorityQueue()
        # frontier.put(start, 0)
        # came_from = dict()
        # cost_so_far = dict()
        # came_from[start] = None
        # cost_so_far[start] = 0

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