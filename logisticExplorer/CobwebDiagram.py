# Import necessary libraries and modules
import sys
sys.path.append("../util")  # Add "../util" directory to the system path
from DEgraphics import *    # Import a custom graphics module for visualization
from random import random   # Import random model for generating random numbers

class CobwebDiagram:
    # Class attributes initialization
    model = None
    window = None
    coords = [-.1, -.1, 1.1, 1.1]  # Default coordinate settings for the diagram
    r = None  # R parameter for the logistic map
    x0 = random()  # Initial x value, randomly chosen

    def __init__(self, model=True, r=3.5, 
                 win=DEGraphWin("Cobweb Diagram", width=450, height=450, 
                                autoflush=False, offsets=[540, 450], 
                                hasTitlebar=False, hThickness=1, hBGColor='black')):
        self.model = model
        self.window = win  
        self.r = r  
        self.window.setBackground("#008683")  # Set window background color
        # Use logistic map as the default model if parameter is True
        if model == True:
            def logisticMap(x, r):
                return r * x * (1.0 - x)
            self.model = logisticMap
        
        self.window.setCoords(self.coords[0], self.coords[1], self.coords[2], self.coords[3])

        # Draw axes, labels, and steady-state line
        ax1 = Line(Point(0, 0), Point(1, 0))
        ax1Label = Text(Point(.5, -.05), "Xn")

        ax2 = Line(Point(0, 0), Point(0, 1))
        ax2Label = Text(Point(-.05, .5), "Xn+1")

        steadystate = Line(Point(0, 0), Point(1, 1))

        ax1.draw(self.window)
        ax1Label.draw(self.window)
        ax2.draw(self.window)
        ax2Label.draw(self.window)
        steadystate.draw(self.window)

        # Draw the initial cobweb diagram
        self.drawCobwebDiagram()

    def drawCobwebDiagram(self, r=0.5, x0=2.4, iterates=50, transients=50):
        """Draw the cobweb diagram based on the model."""
        r = self.r
        x0 = self.x0
        self.window.clear()

        # Plot the model curve
        x = 0
        while x <= 1:
            self.window.plot(x, self.model(x, self.r), 'black')
            x += .0005
        self.window.update()

        # Initialize values for drawing the cobweb
        endX = x0
        endY = 0
        moveX = False

        # Handling transients
        for i in range(transients):
            if moveX:
                moveX = False
                width = endY
                endX = width
            else:
                moveX = True
                height = self.model(endX, self.r)
                endY = height

        # Regular iterations
        for i in range(iterates):
            if moveX:
                moveX = False
                width = endY
                # Plot horizontal lines
                if endX < width:
                    while endX < width:
                        self.window.plot(endX, endY, 'white')
                        endX += .001
                else:
                    while endX > width:
                        self.window.plot(endX, endY, 'white')
                        endX -= .001
            else:
                moveX = True
                height = self.model(endX, self.r)
                # Plot vertical lines
                if endY < height:
                    while endY < height:
                        self.window.plot(endX, endY, 'white')
                        endY += .001
                else:
                    while endY > height:
                        self.window.plot(endX, endY, 'white')
                        endY -= .001
        self.window.update()

    # Methods for updating r value, initial x0, and window control
    def setR(self, r):
        self.r = r
        self.drawCobwebDiagram(x0=self.x0)

    def setx0(self, x0):
        self.x0 = x0
        self.drawCobwebDiagram(x0=self.x0)

    def getWindow(self):
        return self.window
    
    def clearDiagram(self):
        self.window.clear()

def main():
    """Main model to run the CobwebDiagram application."""
    g = CobwebDiagram()
    g.drawCobwebDiagram()

# Ensure main() is called only when script is run as the main program
if __name__ == "__main__":
    main()
