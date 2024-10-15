# Import necessary libraries and modules
import sys
sys.path.append("../util")  # Add "../util" directory to the system path

from DEgraphics import *  # Import graphics module (presumably for visualization)
from math import *  # Import all math functions
from random import random  # Import random function for generating random numbers

class BifurcationDiagram:
    # Class attributes initialization
    model = None
    window = None
    coords = None
    numTrans = None
    numIters = None

    def __init__ (self, model=True, 
                  window=DEGraphWin("Bifurcation Diagram", width=900, height=450, 
                                    axisType = 1, autoflush=False, defCoords = [0.75,0,4,1], 
                                    offsets = [540, 0], hasTitlebar = False, 
                                    hThickness = 1, hBGColor = 'black'), 
                  coords = [0.75,0,4,1], numTrans = 100, numIters = 100):
        self.model = model
        self.numTrans = numTrans
        self.numIters = numIters
        self.window = window
        self.window.setBackground("#008683")  # Set window background color
        self.coords = coords
        self.current_r = None
        # Use logistic map as the default model if model parameter is True
        if model == True:
            def logisticMap(x,r):
                return r * x * (1.0 - x)
            self.model = logisticMap
        # Draw the initial bifurcation diagram
        self.drawBifurcationDiagram()


    def drawBifurcationDiagram(self, numTransients = 100, numIterates = 100):
        """Draw the bifurcation diagram based on model behavior."""
        numTransients = self.numTrans
        numIterates = self.numIters

        # Clear any existing graphics on the window
        self.window.clear()

        # Initialize r value and its step size
        r = self.coords[0]
        rstep = (self.coords[2] - self.coords[0])/self.window.width

        # Iterate over r values and plot behavior
        while r < self.coords[2]:
            self.current_r = r
            x0 = random()  # Random initial condition

            # Allow system to settle (transients)
            for i in range(numTransients):
                x0 = self.model(x0,r)

            # Plot system behavior for numIterates iterations
            for i in range(numIterates):
                x0 = self.model(x0,r)
                self.window.plot(r, x0, 'white')
            r += rstep

        # Update the window with the new graphics
        self.window.update()


    def setTrans(self, newNum):
        """Set the number of transients for the bifurcation diagram."""
        self.numTrans = newNum
    
    def setIters(self, newNum):
        """Set the number of iterations for the bifurcation diagram."""
        self.numIters = newNum


    

def main():
    """Main function to run the BifurcationDiagram application."""
    # Create a BifurcationDiagram instance
    g = BifurcationDiagram()

    # Continuously allow user to zoom into the diagram with mouse clicks
    while True:
        g.twoClickZoom()

    # Close the window when done
    g.window.getMouse()
    g.window.close()

# Ensure main() is called only when script is run as the main program
if __name__ == "__main__":
    main()
