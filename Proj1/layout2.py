import subprocess
import sys
sys.path.append("../util")
from DEgraphics import *

def main():
    myWindows = []

    winA = DEGraphWin(
        title="winA", defCoords=[-10, -10, 10, 10], margin=[0, 0],
        axisType=0, axisColor='black',
        width=603, height=70,
        offsets=[300, 50], autoflush=False,
        hasTitlebar=False,
        hThickness=0, hBGColor="red",
        borderWidth=0)
    winA.setBackground("red")
    myWindows.append(winA)

    winB = DEGraphWin(title="winB",
                      defCoords=[-10, -10, 10, 10], margin=[0, 0],
                      axisType=0, axisColor='black',
                      width=230, height=427,
                      offsets=[300, 122], autoflush=False,
                      hasTitlebar=False,
                      hThickness=0, hBGColor="blue",
                      borderWidth=0)
    winB.setBackground("blue")
    myWindows.append(winB)

    winC = DEGraphWin(title="winC",
                      defCoords=[-10, -10, 10, 10], margin=[0, 0],
                      axisType=0, axisColor='black',
                      width=250, height=281.82,
                      offsets=[532, 122], autoflush=False,
                      hasTitlebar=False,
                      hThickness=0, hBGColor="green",
                      borderWidth=0)
    winC.setBackground("green")
    myWindows.append(winC)

    winD = DEGraphWin(title="winD",
                      defCoords=[-10, -10, 10, 10], margin=[0, 0],
                      axisType=0, axisColor='black',
                      width=119, height=529,
                      offsets=[784, 123], autoflush=False,
                      hasTitlebar=False,
                      hThickness=0, hBGColor="orange",
                      borderWidth=0)
    winD.setBackground("orange")
    myWindows.append(winD)

    winE = DEGraphWin(title="winE",
                      defCoords=[-10, -10, 10, 10], margin=[0, 0],
                      axisType=0, axisColor='black',
                      width=482, height=100,
                      offsets=[300, 552], autoflush=False,
                      hasTitlebar=False,
                      hThickness=0, hBGColor="yellow",
                      borderWidth=0)
    winE.setBackground("yellow")
    myWindows.append(winE)

    winF = DEGraphWin(title="winF",
                      defCoords=[-10, -10, 10, 10], margin=[0, 0],
                      axisType=0, axisColor='black',
                      width=250, height=143.91,
                      offsets=[532, 406], autoflush=False,
                      hasTitlebar=False,
                      hThickness=0, hBGColor="pink",
                      borderWidth=0)
    winF.setBackground('pink')
    myWindows.append(winF)

    btnExit = Button(winE, topLeft=Point(8.8965, -5.7), width=1, height=4,
                     edgeWidth=2, label='X',
                     buttonColors=['red', 'black', 'black'],
                     clickedColors=['white', 'black', 'black'],
                     font=('courier', 18), timeDelay=0.25)
    btnExit.activate()

    btnColor = Button(winA, topLeft=Point(2.6, 3), width=7, height=8,
                     edgeWidth=2, label='Change Color',
                     buttonColors=['MediumPurple4', 'black', 'black'],
                     clickedColors=['white', 'black', 'black'],
                     font=('times roman', 18), timeDelay=0.25)
    btnColor.activate()
    
    btnMoveR = Button(winE, topLeft=Point(.6, 2), width=9, height=5,
                     edgeWidth=2, label='Move GUI Right',
                     buttonColors=['SpringGreen4', 'black', 'black'],
                     clickedColors=['white', 'red', 'black'],
                     font=('courier', 18), timeDelay=0.25)
    btnMoveR.activate()

    btnMoveL = Button(winE, topLeft=Point(-9.6, 2), width=9, height=5,
                     edgeWidth=2, label='Move GUI Left',
                     buttonColors=['SpringGreen4', 'black', 'black'],
                     clickedColors=['white', 'red', 'black'],
                     font=('courier', 18), timeDelay=0.25)
    btnMoveL.activate()

    btnChangeLayout1 = Button(winB, topLeft=Point(-5, 4), width=14, height=2,
                     edgeWidth=2, label='Change to Layout 1',
                     buttonColors=['medium sea green', 'black', 'black'],
                     clickedColors=['white', 'black', 'black'],
                     font=('times roman', 18), timeDelay=0.25)
    btnChangeLayout1.activate()

    btnChangeLayout3 = Button(winB, topLeft=Point(-5, 0), width=14, height=2,
                     edgeWidth=2, label='Change to Layout 3',
                     buttonColors=['medium sea green', 'black', 'black'],
                     clickedColors=['white', 'black', 'black'],
                     font=('times roman', 18), timeDelay=0.25)
    btnChangeLayout3.activate()

    layoutText = Text(Point(-7.6,-3.7), "Layout 2")
    layoutText.setTextColor('black')
    layoutText.setSize(25)
    layoutText.setFace('times roman')
    layoutText.draw(winA)

    counter = 0
    while True:
        clickPt2 = winA.checkMouse()
        if clickPt2:
            if btnColor.clicked(clickPt2):
                
                if(counter % 2 == 0):
                    winA.setBackground('purple')
                    counter = counter + 1
                elif (counter % 2 != 0):
                    winA.setBackground('red')
                    counter = counter + 1
        clickPt = winE.checkMouse()
        if clickPt:
            if btnExit.clicked(clickPt):
                break
            if btnMoveR.clicked(clickPt):
                for win in myWindows:
                    current_x_offset, current_y_offset = win.master.geometry().split('+')[1:3]
                    new_x_offset = int(current_x_offset) + 10
                    win.setOffsets(new_x_offset, current_y_offset)
            if btnMoveL.clicked(clickPt):
                for win in myWindows:
                    current_x_offset, current_y_offset = win.master.geometry().split('+')[1:3]
                    new_x_offset = int(current_x_offset) - 10
                    win.setOffsets(new_x_offset, current_y_offset)
        clickPt3 = winB.checkMouse()
        if clickPt3:
            if btnChangeLayout1.clicked(clickPt3):
                subprocess.Popen(["python", "layout1.py"])
                exit()
            if btnChangeLayout3.clicked(clickPt3):
                subprocess.Popen(["python", "layout3.py"])
                exit()

                    
                        
            
            

if __name__ == "__main__":
    main()
