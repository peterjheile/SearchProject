OVERVIEW:
Our program creates a map that generates Locations, intersections, a starting point, and Locations that
mimicks what a real map looks like. Once creates, the user can interact with the map, clikcing buttons.
The main purpose of this project is to allow the user to use search algorithms to find an optimal path from their destination
to two different locations. Below is important information on how to run and use the program and information on what everything is.

TO RUN THE PROGRAM:
1. Run the intitializer.py file. Runnign this file calls methods and classes so that the user does not need to 
    navigate throguh the file. They can simply run it inly from this.
    - Upon running, the suer can enter a 0 to crate a new map, or a 1 to load a past saved map
2. use the W,S,A,D keys to move the screen to where you want to looks
3. Click on the On-screen buttons to use each Once
     - Save button - Saves the map in real time. There is a max of 1 save so upon click, the past save will be overridden
     - Zoom in Button - Zoom in on the map
     - Zoom out button - Zoom out on the map
     - A* button - uses the A* Search algorithm to generate and add a path to your destinations on the screen
     - Greedy Button - uses the Greedy Search algorithm to generate and add a path to your destinations on the screen


MAP KEY:
 - Red Dot - Starting locations
 - Yellow Dot - both destinations
 - Black Dot - random locations (think taco bell or walmart)
 - Blue Dot - intersections in the road, but are not destinations you can travel. 
 - black line - roads from one location to anther
 - yellow line - path to the first destination. Appear when a search has been clicked and there is a path to Both destinations
 - red line - path to the second destination. Appear when a search has been clicked and there is a path to Both destinations
 - Top Right Information - calculation time of the seach algorithm and distance to reach both destination with the path found


WORKINGS:
- the initializer  - creates a window that acts as a container for all information that is held on the screen. It also
                    starts running the code allowing all in one spot. it also keeps track of a times, and if the user has hit any buttons
- window class - container that stores the information to generate a pygame window. Also creates the map class, which hold everything portrayed on
                  the map. It furthermore creates the GUI class which hold everything portrayed on the GUI
 - GUI Class - contains draw functions and containers that hold a list of all the Buttons on the screen
 - Map Class - contains draw function and containers that hold the starting point, locations, and destintions. It also
                contains a function that draw the roads to the screen
 - Button classes - each button is the same except for one unique function that gives it its unique ability.
                    some of the chage map dimention, such as length and widht to zoom in and out, some call a different seach algorithm
 - Algorithms - class that constains our two search algorithms and all of their implementation. It is a serpeate class so it can all be easily seen 
                and held in one spot
 - Locations, destinations, etc - hold coordinates that are location on the map. The are points that can be traveled to.


Imports:
pygame
Pickle
math


 NOTE: 
 The computation time is often zero because neither algorithm has a large time complexity and are nearly
 instantaneous. Because of this, the time calculation only is shows as a figure other then zero sometimes. If there
 were more locations and intersections, and the time is actually noticebale, then the compuation time will apear learger than
 zero
