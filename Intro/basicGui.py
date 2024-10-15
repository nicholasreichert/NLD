# a basic gui with 3 windows

# set up the ability to see another folder
import sys
sys.path.append("../util")

from DEgraphics import *
import math

def main():
    # custom coordinate settings
    xmin = -12
    xmax = 12
    ymin = -4
    ymax = 4

    # list to contain all windows
    myWindows = []

    winA = DEGraphWin(title = "winA", width = 600, height = 230,
                      defCoords = [xmin,ymin,xmax,ymax],
                      offsets = [200,100], autoflush = False,
                      hasTitlebar = False)
    winA.setBackground("white")
    myWindows.append(winA)
    winA.toggleAxes()

    winCP = DEGraphWin(title = "control panel", width = 200, height = 200,
                       defCoords = [0,0,20,20], offsets = [800,100])
    myWindows.append(winCP)

    winExplanation = DEGraphWin(width = 600, height = 50,
                                offsets = [200,330],
                                hasTitlebar = False)
    winExplanation.setBackground("red")
    myWindows.append(winExplanation)

    winBtmRight = DEGraphWin(width = 200, height = 50,
                                offsets = [800,330],
                                hasTitlebar = False)
    winBtmRight.setBackground("green")
    myWindows.append(winBtmRight)

    btnExit = Button(winCP, topLeft = Point(16,19), width=3, height=3,
                 edgeWidth = 2, label = 'X',
                 buttonColors = ['red','black','black'],
                 clickedColors = ['white','red','black'],
                 font=('courier',18), timeDelay = 0.25)
    btnExit.activate

    btnSine = Button(winCP, topLeft = Point(12,19), width=3, height=3,
                 edgeWidth = 2, label = 'SINE',
                 buttonColors = ['red','black','black'],
                 clickedColors = ['white','red','black'],
                 font=('courier',18), timeDelay = 0.1)
    btnSine.activate

    btnInA = Button(winCP, topLeft = Point(12,14), width=3, height=3,
                 edgeWidth = 2, label = 'Inc Ampl',
                 buttonColors = ['red','black','black'],
                 clickedColors = ['white','red','black'],
                 font=('courier',18), timeDelay = 0.1)
    btnInA.activate

    btnDeA = Button(winCP, topLeft = Point(12,9), width=3, height=3,
                 edgeWidth = 2, label = 'Dec Ampl',
                 buttonColors = ['red','black','black'],
                 clickedColors = ['white','red','black'],
                 font=('courier',18), timeDelay = 0.25)
    btnDeA.activate

    btnCos = Button(winCP, topLeft = Point(8,19), width=3, height=3,
                 edgeWidth = 2, label = 'COS',
                 buttonColors = ['red','black','black'],
                 clickedColors = ['white','red','black'],
                 font=('courier',18), timeDelay = 0.25)
    btnCos.activate

    btnTan = Button(winCP, topLeft = Point(4,19), width=3, height=3,
                 edgeWidth = 2, label = 'TAN',
                 buttonColors = ['red','black','black'],
                 clickedColors = ['white','red','black'],
                 font=('courier',18), timeDelay = 0.25)
    btnTan.activate

    clickPt = winCP.getMouse()
    amplitude = 1
    while True:
        clickPt = winCP.checkMouse()
        if clickPt:
            # exit
            if btnExit.clicked(clickPt):
                break

            # increase amplitude
            if btnInA.clicked(clickPt):
                amplitude += 0.5

            # decrease amplitude
            if btnDeA.clicked(clickPt):
                amplitude -= 0.5

            # graph sin wave
            if btnSine.clicked(clickPt):
                x = -16
                while x < 16:
                    winA.plot(x,(math.sin(x) * amplitude), 'blue')
                    x += 0.01

            # graph cos wave
            if btnCos.clicked(clickPt):
                x = -16
                while x < 16:
                    winA.plot(x,(math.cos(x) * amplitude), 'blue')
                    x += 0.01

            # graph tan wave
            if btnTan.clicked(clickPt):
                x = -16
                while x < 16:
                    winA.plot(x,(math.tan(x) * amplitude), 'blue')
                    x += 0.001

    for window in myWindows:
        window.close()


if __name__ == "__main__":
    main()