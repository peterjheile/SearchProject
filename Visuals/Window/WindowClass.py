import sys
import pygame
sys.path.append("Map")
from Maps.MapClass import Map
from Window.GuiClass import GUI
from Window.InteractionsClass import Interactions

class Window:
    #generates a window
    def __init__ (self):
        self.length = 1200
        self.width = 700
        self.color = (255,0,0)
        self.createMap()
        self.createGUI()
        self.information = ["Calculation time: None","Path distance: None"]

#creates a map and everything that is desplayed on the screen
#that the user cannot itnerract with
    def createMap(self):
        self.map = Map()

#creates an interface with buttons and user interactions
    def createGUI(self):
        self.gui = GUI()

    def updateDisplay(self,displacement,display,all=True,zoom=0):
        #this updates the psoitions of everything on the screen
        Interactions.displaceScreen(self.map,self.map.allLocations,displacement,all,zoom)

        #draws everything to the sceen
        display.fill((255,0,0))
        self.map.draw(display)
        self.gui.draw(display)
        self.drawInformation(display)
        pygame.display.update()
    
    def drawInformation(self, display):
        depth = 0
        for info in self.information:
            font = pygame.font.SysFont(None, 25)
            img = font.render(info, True, (255,255,255))
            display.blit(img, (self.length-250,50 + depth))
            depth += 25



