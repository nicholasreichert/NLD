#intro to basics in python, much of which
# should be review for students in NLD


# set up the ability to see another folder
import sys


sys.path.append("../util")

from math import sin
from DEgraphics import *

#define a main method
def main():

    #demonstrate us of print statements here
    #print alone its effectively like println in java
    print("Hello, World!")

    print("Whoops! I meant ", end = " ")
    print("Hello, Universe!")

    # create a graphing window
    winPlot = DEGraphWin(title = "My first NLD graphics program",
    	         defCoords=[-8,-6,8,6], margin = [0,0],
                 axisType = 0, axisColor = 'black',
                 width = 800, height = 600,
                 offsets=[0,0], autoflush = False,
                 hasTitlebar = True,
                 hThickness=2, hBGColor="blue",
                 borderWidth=0)
    winPlot.toggleAxes()

    # graph y = sin(x) on winPlot in red
    winPlot.getMouse()
    x = winPlot.currentCoords[0]
    xStep=(winPlot.currentCoords[2]-winPlot.currentCoords[0])/winPlot.width
    yStep=(winPlot.currentCoords[3]-winPlot.currentCoords[1])/winPlot.height
    count = 0
    while x < winPlot.currentCoords[2]:
        y = winPlot.currentCoords[1]
        while y < winPlot.currentCoords[3]:
            winPlot.plot(x, y, 'red')
            y += 2 * yStep
        x += xStep
        winPlot.update()
        # count += 1
        # if count % 1000 == 0:
        #     winPlot.update()

    # wait for a click, then close the window
    winPlot.getMouse()
    winPlot.close()

# if running main, then start main,
# otherwise just import to use methods without
# running main
if __name__ == "__main__":
    main()