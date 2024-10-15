
import sys
import os
import webbrowser
from MandelbrotSet import *
from JuliaSet import *

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path)


def main():
    global constant
    constant = complex(.365, -.37)
    
    windows = []

    # Window creation

    winTitle = DEGraphWin(title = "Title Bar", height = 100, width = 1200 , hasTitlebar = False, offsets = [150, 0], hBGColor = '#212529')
    winTitle.setBackground('#343A40')
    windows.append(winTitle)

    winBigCP = DEGraphWin(title = "Big CP", height = 200, width = 1200 , hasTitlebar = True, offsets = [150, 700], hBGColor = '#212529')
    winBigCP.setBackground('#343A40')
    windows.append(winBigCP)

    # Button Creation

    btnExit = Button(winBigCP, topLeft = Point(9, 9), width = 0.5, height=1.5, label = 'X')
    btnExit.activate()
    
    btnZoomInJulia = Button(winBigCP, topLeft = Point(-9.5, 8), width = 4, height=3, label = 'Zoom In')
    btnZoomInJulia.activate()
    
    btnZoomOutJulia = Button(winBigCP, topLeft = Point(-9.5, 3), width = 4, height=3, label = 'Zoom Out')
    btnZoomOutJulia.activate()
    
    btnClearJulia = Button(winBigCP, topLeft = Point(-4.5, 8), width = 3.5, height=3, label = 'Clear')
    btnClearJulia.activate()
    
    btnZoomInMandelbrot = Button(winBigCP, topLeft = Point(1, 7), width = 4, height=3, label = 'Zoom In')
    btnZoomInMandelbrot.activate()
    
    btnZoomOutMandelbrot = Button(winBigCP, topLeft = Point(1, 3), width = 4, height= 3, label = 'Zoom Out')
    btnZoomOutMandelbrot.activate()
    
    btnClearMandelbrot = Button(winBigCP, topLeft = Point(8, 7), width =1.5, height=2, label = 'Clear')
    btnClearMandelbrot.activate()
    
    btnChooseC = Button(winBigCP, topLeft = Point(-4.5, 4), width =2.5, height=2, label = 'Choose C')
    btnChooseC.activate()
    
    btnDrawMandelbrot = Button(winBigCP, topLeft = Point(8, 4), width =1.5, height=2, label = 'Draw')
    btnDrawMandelbrot.activate()

    btnDrawJulia = Button(winBigCP, topLeft = Point(-4.5, -3), width = 1.5, height = 2, label = 'Draw')
    btnDrawJulia.activate()

    btnHelp = Button(winBigCP, topLeft = Point(9.5, -6), width =0.2, height=1.5, label = '?')
    btnHelp.activate()

    btnEnterC = Button(winBigCP, topLeft = Point(-1.6, 0.8), width = 1, height = 2, label = 'Go')
    btnEnterC.activate()
    
    # Dropdown
    
    algChange = DropDown(Point(3.18, -3), ['Exterior', 'Interior'])
    algChange.draw(winBigCP)   
    
    algChangeJulia = DropDown(Point(-8.5, -2.5), ['Regular', 'Inverse'])
    algChangeJulia.draw(winBigCP)
    
    # Line
    dividerLine = Line(Point(0, -10), Point(0, 10))
    dividerLine.draw(winBigCP)
    
    # Entry
    
    escIters = IntEntry(Point(4, -7), 8, [0, 1000])
    escIters.draw(winBigCP)
    
    cValue = Entry(Point(-2.3, 0), 8)
    cValue.draw(winBigCP)
    
    setIters = IntEntry(Point(-7, -6), 8, [0, 1000])
    setIters.draw(winBigCP)
    
    # Text Creation
    
    escItersText = Text(Point(2.25, -7), "Set Escape Iters:")
    escItersText.setTextColor('black')
    escItersText.setFace('times roman')
    escItersText.setSize(20)
    escItersText.draw(winBigCP)

    setItersJulia = Text(Point(-8.5, -6), "Set Julia Iters:")
    setItersJulia.setTextColor('black')
    setItersJulia.setFace('times roman')
    setItersJulia.setSize(16)
    setItersJulia.draw(winBigCP)
    
    JuliaText = Text(Point(-5, 0), "Julia Set")
    JuliaText.setTextColor('black')
    JuliaText.setFace('times roman')
    JuliaText.setSize(30)
    JuliaText.draw(winTitle)

    MandelbrotText = Text(Point(5, 0), "Mandelbrot Set")
    MandelbrotText.setTextColor('black')
    MandelbrotText.setFace('times roman')
    MandelbrotText.setSize(30)
    MandelbrotText.draw(winTitle)
    
    currentCText = Text(Point(-2, -7), "C Value: ")
    currentCText.setTextColor('black')
    currentCText.setFace('times roman')
    currentCText.setSize(16)
    currentCText.draw(winBigCP)
    
    enterCText = Text(Point(-3.75, 0), "Enter C Value:")
    enterCText.setTextColor('black')
    enterCText.setFace('times roman')
    enterCText.setSize(16)
    enterCText.draw(winBigCP)


    running = True
    mandelbrot = MandelbrotSet(600,600)
    julia = JuliaSet(600,600)
    mandelbrot.exteriorAlg()
    mandelbrot.window.update()
    julia.inversePlotSet(const = constant)
    julia.window.clear()
    julia.regPlotSet(const = constant)
    julia.window.update()
    currentCText.setText("C Value: " + str(constant))
    
    windows.append(mandelbrot.window)
    windows.append(julia.window)

    def choosePoint(algType = 'Regular', iterations = 50):
        julia.setMaxIterates(iterations)
        point = mandelbrot.window.getMouse()
        constant = complex(point.x, point.y)
        julia. window.clear()
        if algType == 'Regular':
            julia.regPlotSet(const = constant)
        elif algType == 'Inverse':
            julia.inversePlotSet(const = constant) 
        currentCText.setText("C value: " + str(constant)) 
        
    def open_link():
        webbrowser.open("https://drive.google.com/file/d/1lW83xbytAjCRGrr3kuuoHoOGIqOvIJHV/view?usp=sharing")
        
    while running:
        clickPt = winBigCP.checkMouse()
        if clickPt:
            if btnExit.clicked(clickPt):
                for win in windows:
                    win.close()
                running = False
                
            elif btnZoomInJulia.clicked(clickPt):
                algTypeJulia = algChangeJulia.getChoice()
                julia.setMaxIterates(setIters.getValue())
                julia.zoom(constan = constant, algType = algTypeJulia)
                
            elif btnZoomOutJulia.clicked(clickPt):
                algTypeJulia = algChangeJulia.getChoice()
                julia.setMaxIterates(setIters.getValue())
                julia.zoom(inout = "out", constan = constant, algType = algTypeJulia)
                
            elif btnZoomInMandelbrot.clicked(clickPt):
                mandelbrot.setMaxIterates(escIters.getValue())
                algType = algChange.getChoice()
                mandelbrot.zoom(algType = algType)
                
            elif btnZoomOutMandelbrot.clicked(clickPt):
                mandelbrot.setMaxIterates(escIters.getValue())
                algType = algChange.getChoice()
                mandelbrot.zoom(inout = "out", algType = algType)
                
            elif btnClearJulia.clicked(clickPt):
                julia.window.clear()
                
            elif btnClearMandelbrot.clicked(clickPt):
                mandelbrot.window.clear()
                
            elif btnChooseC.clicked(clickPt):
                julia.setMaxIterates(setIters.getValue())
                algTypeJulia = algChangeJulia.getChoice()
                choosePoint(algType = algTypeJulia)
                
            elif btnDrawMandelbrot.clicked(clickPt):
                mandelbrot.setMaxIterates(escIters.getValue())
                algType = algChange.getChoice()
                if(algType == 'Exterior'):
                    mandelbrot.exteriorAlg()
                if(algType == 'Interior'):
                    mandelbrot.interiorAlg()
                    
            elif btnDrawJulia.clicked(clickPt):
                julia.setMaxIterates(setIters.getValue())
                algTypeJulia = algChangeJulia.getChoice()
                if(algTypeJulia == 'Regular'):
                    julia.regPlotSet(const = constant)
                if(algTypeJulia == 'Inverse'):
                    julia.inversePlotSet(const = constant)
                    
            elif btnHelp.clicked(clickPt):
                open_link()
                
            elif btnEnterC.clicked(clickPt):
                constant = eval(cValue.getText())
                algTypeJulia = algChangeJulia.getChoice()
                if(algTypeJulia == 'Regular'):
                    julia.regPlotSet(const = constant)
                elif algTypeJulia == 'Inverse':
                    julia.inversePlotSet(const = constant)
    

if __name__ == '__main__':
    main()