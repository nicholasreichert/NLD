import sys
sys.path.append("../util")
from DEgraphics import *
from BifurcationDiagram import *
from CobwebDiagram import CobwebDiagram
from TimeSeriesDiagram import TimeSeriesDiagram

def main():

    # Initial parameters for the diagrams

    numIters = 100
    numTrans = 5
    cobIters = 100
    x1 = .4
    cobTrans = 1
    R = 0.3
    numTimeIters = 100
    numTimeTrans = 10

    # Creating the control panel window
    winCP = DEGraphWin(title = "Control Panel",
    	         defCoords=[-10,-10,10,10], margin = [0,0],
                 axisType = 0, axisColor = 'black', axisStyle = 'solid',
                 width = 540, height = 900,
                 offsets=[0,0], autoflush = False,
                 hasTitlebar = False,
                 hThickness=1, hBGColor="black",
                 borderWidth=0)
    
    winCP.setBackground("#008683")

    # GUI Elements: Buttons and Fields


    # Exit button
    btnExit = Button(winCP, topLeft = Point(-9,9), width= 4, height =1,
                 edgeWidth = 2, label = 'Exit GUI',
                 buttonColors = ['#0E3B4A','#51FFA6','linen'],
                 clickedColors = ['white','red','black'],
                 font=('times roman', 25), timeDelay = 0.15)
    btnExit.activate()

    # Draw Bifurcation button
    btnDrawBifurcation = Button(winCP, topLeft = Point(-9,4.5), width= 9, height =1,
                 edgeWidth = 2, label = 'Draw Bifurcation Diagram',
                 buttonColors = ['#0E3B4A','#51FFA6','white'],
                 clickedColors = ['white','red','black'],
                 font=('helvetica',18), timeDelay = 0.25)
    btnDrawBifurcation.activate()

    # Draw Time Series button
    btnDrawTimeSeries = Button(winCP, topLeft = Point(-9,5.5), width= 9, height =1,
                 edgeWidth = 2, label = 'Draw Time Series Diagram',
                 buttonColors = ['#0E3B4A','#51FFA6','white'],
                 clickedColors = ['white','red','black'],
                 font=('helvetica',18), timeDelay = 0.25)
    btnDrawTimeSeries.activate()

    # Draw Cobweb button
    btnDrawCobweb = Button(winCP, topLeft = Point(-9,3.5), width= 8, height =1,
                 edgeWidth = 2, label = 'Draw Cobweb Diagram',
                 buttonColors = ['#0E3B4A','#51FFA6','white'],
                 clickedColors = ['white','red','black'],
                 font=('helvetica',18), timeDelay = 0.25)
    btnDrawCobweb.activate()

    # Zoom in button
    btnZoom = Button(winCP, topLeft = Point(-9,2.5), width= 8, height =1,
                 edgeWidth = 2, label = 'Zoom In Bifurcation',
                 buttonColors = ['#0E3B4A','#51FFA6','white'],
                 clickedColors = ['white','red','black'],
                 font=('helvetica',18), timeDelay = 0.25)
    btnZoom.activate()

    btnZoomOut = Button(winCP, topLeft = Point(-9,1.5), width= 8, height =1,
                 edgeWidth = 2, label = 'Zoom Out Bifurcation',
                 buttonColors = ['#0E3B4A','#51FFA6','white'],
                 clickedColors = ['white','red','black'],
                 font=('helvetica',18), timeDelay = 0.25)
    btnZoomOut.activate()

    # Set Bifurcation Iterations button
    BtnSetBifurcationIters = Button(winCP, topLeft = Point(-6.5,-2.78), width= .6, height = .45,
                 edgeWidth = 2, label = '✓',
                 buttonColors = ['#0E3B4A','#51FFA6','white'],
                 clickedColors = ['white','red','black'],
                 font=('helvetica',18), timeDelay = 0.25)
    BtnSetBifurcationIters.activate()

    # Bifurcation Iterations entry field
    SetBifurcationIters = IntEntry(center = Point(-8,-3), width = 7, span = [0,10000],
                       colors = ['#007883','#51FFA6'],
                       errorColors = ['red','white'])
    SetBifurcationIters.draw(winCP)

    # Set Bifurcation Transient button
    BtnSetBifurcationTrans = Button(winCP, topLeft = Point(-6.5,-4.28), width= .6, height = .45,
                 edgeWidth = 2, label = '✓',
                 buttonColors = ['#0E3B4A','#51FFA6','white'],
                 clickedColors = ['white','red','black'],
                 font=('helvetica',18), timeDelay = 0.25)
    BtnSetBifurcationTrans.activate()

    # Bifurcation Transient entry field
    SetBifurcationTrans = IntEntry(center = Point(-8,-4.5), width = 7, span = [0,10000],
                       colors = ['#007883','#51FFA6'],
                       errorColors = ['red','white'])
    SetBifurcationTrans.draw(winCP)

    # Set cobweb x0 value button
    BtnSetCobwebx0 = Button(winCP, topLeft = Point(8.5,-5.78), width= .6, height = .45,
                 edgeWidth = 2, label = '✓',
                 buttonColors = ['#0E3B4A','#51FFA6','white'],
                 clickedColors = ['white','red','black'],
                 font=('helvetica',18), timeDelay = 0.25)
    BtnSetCobwebx0.activate()

    # Cobweb x0 entry field
    SetCobwebx0 = DblEntry(center = Point(7,-6), width = 7, span = [0,1.1],
                       colors = ['#007883','#51FFA6'],
                       errorColors = ['red','white'])
    SetCobwebx0.draw(winCP)

    # Set cobweb R value button
    BtnSetCobwebR = Button(winCP, topLeft = Point(8.5,-7.28), width= .6, height = .45,
                 edgeWidth = 2, label = '✓',
                 buttonColors = ['#0E3B4A','#51FFA6','white'],
                 clickedColors = ['white','red','black'],
                 font=('helvetica',18), timeDelay = 0.25)
    BtnSetCobwebR.activate()

    # Cobweb R value entry field
    SetCobwebR = DblEntry(center = Point(7,-7.5), width = 7, span = [0,4],
                       colors = ['#007883','#51FFA6'],
                       errorColors = ['red','white'])
    SetCobwebR.draw(winCP)

    # Set Cobweb Iterations button
    BtnSetCobwebIters = Button(winCP, topLeft = Point(8.5,-4.28), width= .6, height = .45,
                 edgeWidth = 2, label = '✓',
                 buttonColors = ['#0E3B4A','#51FFA6','white'],
                 clickedColors = ['white','red','black'],
                 font=('helvetica',18), timeDelay = 0.25)
    BtnSetCobwebIters.activate()

    # Cobweb Iteration entry field
    SetCobwebIters = IntEntry(center = Point(7,-4.5), width = 7, span = [0,10000],
                       colors = ['#007883','#51FFA6'],
                       errorColors = ['red','white'])
    SetCobwebIters.draw(winCP)

    # Set Cobweb and Time Series Transient button
    BtnSetCobTimeTrans = Button(winCP, topLeft = Point(8.5,-2.72), width= .6, height = .45,
                 edgeWidth = 2, label = '✓',
                 buttonColors = ['#0E3B4A','#51FFA6','white'],
                 clickedColors = ['white','red','black'],
                 font=('helvetica',18), timeDelay = 0.25)
    BtnSetCobTimeTrans.activate()

    # Cobweb and Time Series Transient entry field
    SetCobTimeTrans = IntEntry(center = Point(7, -3), width = 7, span = [0,1000],
                       colors = ['#007883','#51FFA6'],
                       errorColors = ['red','white'])
    SetCobTimeTrans.draw(winCP)

    # Set Time Series Iterations Button
    BtnSetTimeIters = Button(winCP, topLeft = Point(-6.5,-5.8), width= .6, height =.45,
                 edgeWidth = 2, label = '✓',
                 buttonColors = ['#0E3B4A','#51FFA6','white'],
                 clickedColors = ['white','red','black'],
                 font=('helvetica',18), timeDelay = 0.25)
    BtnSetTimeIters.activate()

    # Set Time SEries R Value Button
    BtnSetTimeR = Button(winCP, topLeft = Point(-6.5,-7.3), width=.6, height =.45,
                 edgeWidth = 2, label = '✓',
                 buttonColors = ['#0E3B4A','#51FFA6','white'],
                 clickedColors = ['white','red','black'],
                 font=('helvetica',18), timeDelay = 0.25)
    BtnSetTimeR.activate()

    # Set Time X Button
    BtnSetTimeX = Button(winCP, topLeft = Point(-6.5,-8.8), width= .6, height =.45,
                 edgeWidth = 2, label = '✓',
                 buttonColors = ['#0E3B4A','#51FFA6','white'],
                 clickedColors = ['white','red','black'],
                 font=('helvetica',18), timeDelay = 0.25)
    BtnSetTimeX.activate()


    # Entry for Time Series Iterations
    SetTimeIters = IntEntry(center = Point(-8,-6), width = 7, span = [0,10000],
                       colors = ['#007883','#51FFA6'],
                       errorColors = ['red','white'])
    
    SetTimeIters.draw(winCP)
    
    # Time Series R entry field
    SetTimeRValue =  DblEntry(center = Point(-8,-7.5), width = 7, span = [0,4],
                       colors = ['#007883','#51FFA6'],
                       errorColors = ['red','white'])
    SetTimeRValue.draw(winCP)

    # Time Series X entry field
    SetTimeXValue = DblEntry(center = Point(-8,-9), width = 7, span = [0,1],
                       colors = ['#007883','#51FFA6'],
                       errorColors = ['red','white'])
    SetTimeXValue.draw(winCP)

    # Text fields to label the buttons

    BifurcationIters = Text(Point(-7, -2.5), "Set Bifurcation Iters")
    BifurcationIters.setTextColor('white')
    BifurcationIters.setSize(15)
    BifurcationIters.draw(winCP)

    BifurcationTrans = Text(Point(-7, -4), "Set Bifurcation Trans")
    BifurcationTrans.setTextColor('white')
    BifurcationTrans.setSize(15)
    BifurcationTrans.draw(winCP)

    Cobwebx0 = Text(Point(7, -5.5), "Set Cobweb x0")
    Cobwebx0.setTextColor('white')
    Cobwebx0.setSize(15)
    Cobwebx0.draw(winCP)

    CobwebR = Text(Point(7,-7), "Set Cobweb R")
    CobwebR.setTextColor('white')
    CobwebR.setSize(15)
    CobwebR.draw(winCP)

    CobwebIters = Text(Point(7,-4), "Set Cobweb Iters")
    CobwebIters.setTextColor('white')
    CobwebIters.setSize(15)
    CobwebIters.draw(winCP)

    GlobalTrans = Text(Point(6,-2.5), "Set Cobweb/Time Series Trans")
    GlobalTrans.setTextColor('white')
    GlobalTrans.setSize(15)
    GlobalTrans.draw(winCP)

    TimeX = Text(Point(-7,-8.5), "Set Time Series X")
    TimeX.setTextColor('white')
    TimeX.setSize(15)
    TimeX.draw(winCP)

    TimeR = Text(Point(-7,-7), "Set Time Series R")
    TimeR.setTextColor('white')
    TimeR.setSize(15)
    TimeR.draw(winCP)

    TimeIters = Text(Point(-7,-5.5), "Set Time Series Iters")
    TimeIters.setTextColor('white')
    TimeIters.setSize(15)
    TimeIters.draw(winCP)


    # While loop to code the logic when a button is clicked

    # Initialize three objects, c, p , and t for the three different diagrams
    c = CobwebDiagram()
    p = BifurcationDiagram()
    t = TimeSeriesDiagram()

    while True:
        clickPt = winCP.checkMouse()
        if clickPt:
            if btnExit.clicked(clickPt):
                break
            elif btnDrawBifurcation.clicked(clickPt):  
                p.drawBifurcationDiagram(numTrans, numIters)
            elif btnDrawCobweb.clicked(clickPt):
                c.drawCobwebDiagram()
            elif btnDrawTimeSeries.clicked(clickPt):
                t.drawTimeSeriesDiagram()
            elif btnZoom.clicked(clickPt):
                p.window.zoom(whichWay = 'in')
                p.drawBifurcationDiagram()
            elif btnZoomOut.clicked(clickPt):
                p.window.zoom(whichWay = 'out')
                p.drawBifurcationDiagram()
            elif BtnSetBifurcationIters.clicked(clickPt):
                x = SetBifurcationIters.getValue()
                p.setIters(x)
                p.drawBifurcationDiagram()
            elif BtnSetBifurcationTrans.clicked(clickPt):
                x = SetBifurcationTrans.getValue()
                p.setTrans(x)
                p.drawBifurcationDiagram()
            elif BtnSetCobwebx0.clicked(clickPt):
                z = SetCobwebx0.getValue()
                c.setx0(z)
            elif BtnSetCobwebR.clicked(clickPt):
                H = SetCobwebR.getValue()
                c.setR(H)
            elif BtnSetCobwebIters.clicked(clickPt):
                cobIters = SetCobwebIters.getValue()
                c.drawCobwebDiagram(x0=x1, r = R, iterates = cobIters, transients = cobTrans)
            elif BtnSetCobTimeTrans.clicked(clickPt):
                cobTrans = SetCobTimeTrans.getValue()
                numTimeTrans = SetCobTimeTrans.getValue()
                c.drawCobwebDiagram(x0=x1, r = R, iterates = cobIters, transients = cobTrans)
                t.drawTimeSeriesDiagram(iterations = numTimeIters, transients = numTimeTrans)
            elif BtnSetTimeIters.clicked(clickPt):
                numTimeIters = SetTimeIters.getValue()
                t.drawTimeSeriesDiagram(iterations = numTimeIters, transients = numTimeTrans)
            elif BtnSetTimeX.clicked(clickPt):
                t.setX(SetTimeXValue.getValue())
                t.drawTimeSeriesDiagram(iterations = numTimeIters, transients = numTimeTrans)
            elif BtnSetTimeR.clicked(clickPt):
                t.setR(SetTimeRValue.getValue())
                t.drawTimeSeriesDiagram(iterations = numTimeIters, transients = numTimeTrans)
                

if __name__ == "__main__":
    main()
    
