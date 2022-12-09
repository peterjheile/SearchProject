import pygame
import sys
import pickle
from Window.SearchAlgorithms import Algorithms
import math
import time


class Button:
    def __init__(self, text = ""):
        self.width = 200
        self.height = 50
        self.color = (221,160,221)
        self.text = text

    def draw(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height))
        self.showText(display)

    def showText(self,display):
        font = pygame.font.SysFont(None, 25)
        img = font.render(self.text, True, (0,0,255))
        display.blit(img, (self.x+10,self.y+30))

    def checkClicked(self, clickPos):
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            return True
        return False

    def updateDisplayInformation(self,window,pathFound,time):
        distance = 0
        for index in range(1,len(pathFound)):
            distance += math.dist((pathFound[index].x,pathFound[index].y),(pathFound[index-1].x,pathFound[index-1].y))
        window.information = ["Calculation time:"+str(time),"Path distance:"+str(round(distance,2))]


class AStarSearchButton(Button):
    def __init__(self,text):
        super().__init__(text)
        self.x = 5
        self.y = 225

    def checkClicked(self, clickPos, window):
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            self.findPath(window)

    def findPath(self,window):
        t0 = time.time()
        pathFound = Algorithms.AStarSearch(window.map.startLocation,window.map.destination1,window.map.destination2)
        t1 = time.time()
        print(t0,t1)
        window.map.pathFound = pathFound
        self.updateDisplayInformation(window,pathFound,t1-t0)


class greedySearchButton(Button):
    def __init__(self,text):
        super().__init__(text)
        self.x = 5
        self.y = 280

    def checkClicked(self, clickPos, window):
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            self.findPath(window)

    def findPath(self,window):
        t0 = time.time()
        pathFound = Algorithms.greedySearch(window.map.startLocation,window.map.destination1,window.map.destination2)
        t1 = time.time()
        print(t0,t1)
        window.map.pathFound = pathFound
        self.updateDisplayInformation(window,pathFound,t1-t0)

class DijkstrasSearchButton(Button):
    def __init__(self,text):
        super().__init__(text)
        self.x = 5
        self.y = 335

    def checkClicked(self, clickPos, window):
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            self.findPath(window)

    def findPath(self,window):
        t0 = time.time()
        pathFound = Algorithms.DijkstrasSearch(window.map.startLocation,window.map.destination1,window.map.destination2)
        t1 = time.time()
        print(t0,t1)
        window.map.pathFound = pathFound
        self.updateDisplayInformation(window,pathFound,t1-t0)


class ClearButton(Button):
    def __init__(self,text):
        super().__init__(text)
        self.x = 5
        self.y = 170

    def checkClicked(self, clickPos, window):
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            self.clear(window)

    def clear(self,window):
        window.map.pathFound = []

        
# class PauseButton(Button):
#     def __init__(self, text):
#         super().__init__(text)
#         self.x = 5
#         self.y = 105

#     def checkClicked(self,clickPos,buttons,display,window, parent = False):
#         if parent:
#             return super().checkClicked(clickPos)
#         else: 
#             if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
#                 self.pause(buttons,display,window)
                    
#     def pause(self,buttons,display,window):
#         clock = pygame.time.Clock()
#         continues = True
#         while continues:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 if event.type == pygame.MOUSEBUTTONUP:
#                     if buttons[0].checkClicked(pygame.mouse.get_pos()):
#                         continues = False
#                     buttons[2].checkClicked(pygame.mouse.get_pos(),window)
#                     buttons[3].checkClicked(pygame.mouse.get_pos(),window,display)
#                     buttons[4].checkClicked(pygame.mouse.get_pos(),window,display)
#                     buttons[5].checkClicked(pygame.mouse.get_pos(),window,display)


#             keys = pygame.key.get_pressed()
#             movement = [0,0]
#             if keys[pygame.K_a]:
#                 movement[0] +=5
#             if keys[pygame.K_d]:
#                 movement[0] -=5
#             if keys[pygame.K_w]:
#                 movement[1] +=5
#             if keys[pygame.K_s]:
#                 movement[1] -=5
#             window.updateDisplay(movement,display,False)
#             clock.tick(60)

class SaveButton(Button):
    def __init__(self,text):
        super().__init__(text)
        self.x = 5
        self.y = 5

    def checkClicked(self,clickPos,window, parent = False):
        if parent:
            return super().checkClicked(clickPos)
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            self.save(window)

    def save(self,window):
        with open("EcoOutputData","wb") as file:
            pickle.dump(window,file)

class ZoomOutButton(Button):
    def __init__(self,text):
        super().__init__(text)
        self.x = 5
        self.y = 115
        
    def checkClicked(self,clickPos,window,display, parent = False):
        if parent:
            return super().checkClicked(clickPos)
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            self.zoomOut(window,display)

    def zoomOut(self,window,display):
        window.updateDisplay([0,0],display,True,-1)

class ZoomInButton(Button):
    def __init__(self,text):
        super().__init__(text)
        self.x = 5
        self.y = 60
        
    def checkClicked(self,clickPos,window,display, parent = False):
        if parent:
            return super().checkClicked(clickPos)
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            self.zoomIn(window,display)

    def zoomIn(self,window,display):
        window.updateDisplay([0,0],display,True,1)

    

    



    