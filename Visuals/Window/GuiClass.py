from Window.ButtonClass import AStarSearchButton
from Window.ButtonClass import SaveButton
from Window.ButtonClass import ZoomInButton
from Window.ButtonClass import ZoomOutButton
from Window.ButtonClass import ClearButton
from Window.ButtonClass import greedySearchButton
from Window.ButtonClass import DijkstrasSearchButton

class GUI:
    def __init__(self):
        self.AStarSearchButton = AStarSearchButton("A Star")
        self.saveButton = SaveButton("Save")
        self.ZoomInButton = ZoomInButton("Zoom In")
        self.ZoomOutButton = ZoomOutButton("Zoom out")
        self.clearButton = ClearButton("Clear Search")
        self.greedySearchbutton = greedySearchButton("Greedy Search")
        # self.DijkstrasSearchButton = DijkstrasSearchButton("Djikstas Search")
        self.buttons = [self.clearButton,self.AStarSearchButton,self.saveButton,self.ZoomInButton,self.ZoomOutButton, self.greedySearchbutton]

    def draw(self,display):
        for i in self.buttons:
            i.draw(display)

    def update(self,mousePos,display,window):
        self.clearButton.checkClicked(mousePos,window)
        self.AStarSearchButton.checkClicked(mousePos,window)
        # self.DijkstrasSearchButton.checkClicked(mousePos,window)
        self.greedySearchbutton.checkClicked(mousePos,window)
        self.saveButton.checkClicked(mousePos,window)
        self.ZoomInButton.checkClicked(mousePos,window,display)
        self.ZoomOutButton.checkClicked(mousePos,window,display)

        

    


