# Import necessary libraries and modules
import sys
sys.path.append("../util")  # Add "../util" directory to the system path
from DEgraphics import *    # Import a custom graphics module for visualization
from random import random   # Import random function for generating random numbers

class TimeSeriesDiagram:
    # Class attributes initialization
    function = None
    window = None
    coords = [-0.1, -0.1, 1.1, 1.1]  # Default coordinate settings for the diagram
    lines = []  # List to store lines drawn in the diagram
    r = 3.1  # Default r value for logistic map
    x0 = random()  # Initial x value, randomly chosen
    numIters = 100  # Default number of iterations

    def __init__(self, function=True,
                 window=DEGraphWin("Timeseries Diagram", width=450, height=450, 
                                autoflush=False, offsets=[990, 450], 
                                hasTitlebar=False, hBGColor="black")):
        self.function = function
        self.numIters = 100  # Set the number of iterations
        self.window = window  # Set the window for the diagram
        # Use logistic map as the default function if parameter is True
        if function:
            def logisticMap(x, r):
                return r * x * (1.0 - x)
            self.function = logisticMap


        self.window.setCoords(self.coords[0], self.coords[1], self.coords[2], self.coords[3])

        self.window.setBackground("#008683")  # Set window background color

        # Draw axes and labels
        ax1 = Line(Point(0, 0), Point(30, 0))
        ax1Label = Text(Point(.5, -.05), "t")
        ax1Label.setSize(20)

        ax2 = Line(Point(0, 0), Point(0, 10))
        ax2Label = Text(Point(-.05, .5), "X")
        ax2Label.setSize(20)

        ax1.draw(self.window)
        ax1Label.draw(self.window)
        ax2.draw(self.window)
        ax2Label.draw(self.window)

        # Draw the initial time series diagram
        self.drawTimeSeriesDiagram()

    def drawTimeSeriesDiagram(self, x=20, iterations=20, transients=1):
        """Draw the time series diagram based on the function."""
        self.clearDiagram()  # Clear any existing lines
        x = self.x0  # Set the initial x value

        # Iterate and draw lines for each step
        i = 0
        for t in range(transients):
            x = self.function(x, self.r)

        for j in range(iterations):
            # Draw a line from (i, x) to (i + 1/iterations, f(x))
            line = Line(Point(i, x), Point(i + 1 / iterations, self.function(x, self.r)), style='solid')
            line.setFill("white")
            line.draw(self.window)

            # Store the line in lines list
            self.lines.append(line)
            x = self.function(x, self.r)
            i += 1 / iterations

    def clearDiagram(self):
        """Clear the diagram by removing all drawn lines."""
        for _ in range(10):
            for line in self.lines:
                line.undraw()
            self.lines.clear()
            self.window.clear()

    def getWindow(self):
        """Return the window instance."""
        return self.window
    
    def setIters(self, iters):
        """Set the number of iterations and redraw the diagram."""
        self.numIters = iters
        self.drawTimeSeriesDiagram()

    def setR(self, r):
        """Set the r value for the logistic map and redraw the diagram."""
        self.r = r
        self.drawTimeSeriesDiagram()

    def setX(self, x):
        """Set the initial x value and redraw the diagram."""
        self.x0 = x
        self.drawTimeSeriesDiagram()
