import sys
sys.path.append("../util")

from DEgraphics import *
import math
import numpy as np

roots = []
function = [1,0,0,0,-1]
windows = []
dimension_horizontal = 0
dimension_vertical = 0
numIters = 100
res_horizontal = 0
res_vertical = 0
colors = ["#264653", "#e76f51", "#E9C46A", "#F4A261", "#386641", "#f2e8cf", "#bc4749", "#d4a373", "#bb9457"]

def function_values(case):
     global function
     if case == 'z^5 - 1':
          function = [1,0,0,0,0,-1]
     elif case == 'z^4 - 1':
          function = [1,0,0,0,-1]
     elif case == 'z^3 - 1':
          function = [1,0,0,-1]
     elif case == 'z^2 - 1':
          function = [1,0,-1]
     
def f(z, function):
        result = 0
        for i, coeff in enumerate(function[::-1]):
            result += coeff * z**i
        return result

def df(z, function):
        result = 0
        for i, coeff in enumerate(function[:-1][::-1]):
            result += (i + 1) * coeff * z**i
        return result

def newtons(z, function):
        f_value = f(z, function)
        df_value = df(z, function)
        
        # Set a threshold for magnitude to avoid division by zero
        threshold = 1e-10
        
        if abs(df_value) < threshold:
            # If magnitude is below the threshold, use a small value instead
            adjusted_df = threshold
        else:
            # Otherwise, use the original derivative
            adjusted_df = df_value
        
        return z - (f_value / adjusted_df)

def iterate(z0, function, n):
        for i in range(n):
            z0 = newtons(z0, function)
        return z0

def getColor(z):
    # Calculate the distances from z to each root
    distances = [abs(z - root) for root in roots]
    
    # Get the index of the root with the smallest distance
    closest_root_index = distances.index(min(distances))
    
    # Return the color corresponding to the closest root
    return colors[closest_root_index]

def iterateAll(win, resVert = res_vertical, resHorz = res_horizontal, iters=numIters):
    # Creates the roots
    global roots
    global function
    for window in windows:
         window.clear()
    roots = np.roots(function)
    real = win.currentCoords[0]
    while real < win.currentCoords[2]:
        imag = win.currentCoords[1]
        while imag < win.currentCoords[3]:
            z = complex(real, imag)
            z = iterate(z, function, iters)
            win.plot(real, imag, getColor(z))
            imag += res_vertical
        real += res_horizontal
    win.update()

def setQuality(quality):
     global dimension_horizontal
     global dimension_vertical
     global res_horizontal
     global res_vertical
     if(quality == 'Ultra High'):
          res_horizontal = dimension_horizontal * .8
          res_vertical = dimension_vertical * .8
     if(quality == 'High'):
          res_horizontal = 1.1* dimension_horizontal
          res_vertical = 1.1* dimension_vertical
     if(quality == 'Medium'):
          res_horizontal = 2.3 * dimension_horizontal
          res_vertical = 2.3 * dimension_vertical
     if(quality == 'Low'):
          res_horizontal = 2.7 * dimension_horizontal
          res_vertical = 2.7 * dimension_vertical

     
def getFunctionRoots():
     global roots
     return roots

def main():
    win = DEGraphWin(width = 800, height = 800, offsets = [400, 100], autoflush = False, hasTitlebar = False, hThickness = 1, hBGColor = '#4A2545')
    windows.append(win)
    winCP = DEGraphWin(width = 200, height = 800, offsets = [200, 100], hasTitlebar = True, hThickness = 1, hBGColor = '#4A2545')
    windows.append(winCP)
    winCP.setBackground('#2A9D8F')
    win.setBackground('white')
    winHeader = DEGraphWin(width = 1000, height = 100, offsets = [200, 0], hasTitlebar = False, hThickness = 1, hBGColor = '#4A2545')
    windows.append(winHeader)
    winHeader.setBackground('#264653')

    global dimension_horizontal
    global dimension_vertical
    dimension_horizontal = (win.currentCoords[2]-win.currentCoords[0]) / win.width
    dimension_vertical = (win.currentCoords[3] - win.currentCoords[1]) / win.height

    dropFunc = DropDown(topLeft = Point(0,-4), choices = ['z^5 - 1', 'z^4 - 1', 'z^3 - 1', 'z^2 - 1'], bg = '#E76F51')
    dropFunc.setFill('#E76F51')
    dropFunc.setTextColor('#E9C46A')
    dropFunc.draw(winCP)

    dropRes = DropDown(topLeft = Point(0, -9), choices = ['Ultra High', 'High', 'Medium', 'Low'], bg = '#E76F51')
    dropRes.setFill('#E76F51')
    dropRes.setTextColor('#E9C46A')
    dropRes.draw(winCP)

    # Creating the functionality buttons

    btnDraw = Button(win = winCP, topLeft = Point(-5,7), width = 9, height = 0.5, label = 'Draw', buttonColors = ['#E76F51', '#4a2545', 'black'])
    btnDraw.activate()

    btnExit = Button(win = winCP, topLeft = Point(7, 9.5), width = 2, height =0.5, label = 'X', buttonColors = ['red', '#4a2545', 'black'])
    btnExit.activate()

    btnZoomIn = Button(win = winCP, topLeft = Point(-5, 5.5), width = 9, height =0.5, label = 'Zoom In', buttonColors = ['#E76F51', '#4a2545', 'black'])
    btnZoomIn.activate()

    btnZoomOut = Button(win = winCP, topLeft = Point(-5, 4.5), width = 9, height =0.5, label = 'Zoom Out', buttonColors = ['#E76F51', '#4a2545', 'black'])
    btnZoomOut.activate()

    ownFuncEnter = Button(win = winCP, topLeft = Point(6.4, -6.25), width = 1.5, height = 0.5, label = 'X', buttonColors = ['#E76F51', '#4a2545', 'black'])
    ownFuncEnter.activate()

    dropDownEnter = Button(win = winCP, topLeft = Point(6.4, -3.75), width = 1.5, height = 0.5, label = 'X', buttonColors = ['#E76F51', '#4a2545', 'black'])
    dropDownEnter.activate()

    setItersEnter = Button(win= winCP, topLeft = Point(6.4, -7.75), width = 1.5, height = 0.5, label = 'X', buttonColors = ['#E76F51', '#4a2545', 'black'])
    setItersEnter.activate()

    getRoots = Button(win = winCP, topLeft = Point(-5.5, 3), width = 10, height = 0.5, label = 'Get Roots', buttonColors = ['#E76F51', '#4a2545', 'black'])
    getRoots.activate()

    setIters = IntEntry(center = Point(0,-8), span = [0, 1000], width = 15, colors = ['#E76F51', '#4a2545'])
    setIters.draw(winCP)
    
    ownFunction = Entry(center = Point(0, -6.5), width = 15)
    ownFunction.setFill('#E76F51')
    ownFunction.setTextColor('#4a2545')
    ownFunction.draw(winCP)

    ownFuncLabel = Text(p = Point(0, -5.5), text = "Enter the coefficients for a function")
    ownFuncLabel.draw(winCP)
    ownFuncLabel2 = Text(p = Point(0, -6), text = "i.e. 1,0,0,-1 is z^3 - 1")
    ownFuncLabel2.draw(winCP)

    setItersLabel = Text(p = Point(0,-7.5), text = "Set the iterations")
    setItersLabel.draw(winCP)

    headerLabel = Text(p = Point(0,0), text = "Newton's Method Explorer")
    headerLabel.setSize(36)
    headerLabel.setStyle('bold')
    headerLabel.setFace('times roman')
    headerLabel.setTextColor('#E9C46A')
    headerLabel.draw(winHeader)



    # While loop for the logic behind the buttons

    while(True):
        global function
        global numIters
        clickPt = winCP.getMouse()

        if(clickPt):
          if btnDraw.clicked(clickPt):
               setQuality(dropRes.getChoice())
               iterateAll(win = win, iters = numIters)

          elif btnZoomIn.clicked(clickPt):
               win.zoom()
               dimension_horizontal = (win.currentCoords[2]-win.currentCoords[0]) / win.width
               dimension_vertical = (win.currentCoords[3] - win.currentCoords[1]) / win.height
               setQuality(dropRes.getChoice())
               iterateAll(win = win, iters = numIters)

          elif btnZoomOut.clicked(clickPt):
               win.zoom(whichWay = 'out')
               iterateAll(win = win, iters = numIters)
        
          elif ownFuncEnter.clicked(clickPt):
               value = ownFunction.getText()
               function  = [int(i.strip()) for i in value.split(',')]
          
          elif dropDownEnter.clicked(clickPt):
               values = dropFunc.getChoice()
               function_values(values)
          
          elif setItersEnter.clicked(clickPt):
               numIters = setIters.getValue()

          elif getRoots.clicked(clickPt):
               roots = getFunctionRoots()
               a = Text(p = Point(0,0), text = "\n".join(f"{root:.2f}" for root in roots))
               a.setSize(12)
               a.draw(winCP)
          

        
        # Exit functionality
          elif btnExit.clicked(clickPt):
               for win in windows:
                    win.close()
               break
        


if __name__ == "__main__":
     main()