import sys
sys.path.append("../util")

from DEgraphics import *
from DEgraphics import change_color
from random import random as rnd
from random import randrange
from transform import *
from tkinter.colorchooser import askcolor
import webbrowser

# to-do
# fix scaling for right control panel value texts
# fix scaling values check button error
# work on new transformation, compelete transformation, and view transformation functionality
# work on draw image functionality
# work on two-tone and multi-color buttons
# work in a way for user to enter iterations and (maybe) transients
# work on user manual document
# comment code
# color scheme for GUI

windows = []
leftButtons = []
bottomButtons = []
bottomText = []
bottomEntry = []
IFS = []
values = []
val = 0


def main():
    # Window creation
    imageWin = DEGraphWin(width = 700, height = 700, offsets = (375, 0), defCoords = [-0.1, -0.1, 1.1, 1.1], hasTitlebar = False)
    windows.append(imageWin)
    leftCP = DEGraphWin(width = 250, height = 700, offsets = (125, 0), defCoords = [-10, -10, 10, 10], hasTitlebar = False)
    windows.append(leftCP)
    rightCP = DEGraphWin(width = 250, height = 700, offsets = (1075, 0), defCoords = [-10, -10, 10, 10], hasTitlebar = False)
    windows.append(rightCP)
    bottomCP = DEGraphWin(width = 1200, height = 200, offsets = (125, 700), defCoords = [-10, -10, 10, 10], hasTitlebar = True)
    windows.append(bottomCP)
    
    # Buttons for the left control panel
    
    btnExit = Button(leftCP, topLeft = Point(-9, 9.3), width = 2, height=1, label = 'X')
    btnExit.activate()

    btnNewTransformation = Button(leftCP, topLeft = Point(-8.95, 8), width = 18, height=1.5, label = 'New Transformation')
    btnNewTransformation.activate()

    leftButtons.append(btnNewTransformation)
    btnCompleteTransformation = Button(leftCP, topLeft = Point(-8.95, 6), width = 18, height=1.5, label = 'Complete Trans')
    leftButtons.append(btnCompleteTransformation)
    btnScalingValues = Button(leftCP, topLeft = Point(-8.95, 4), width = 18, height=1.5, label = 'Scaling Values')
    leftButtons.append(btnScalingValues)
    btnRotationValues = Button(leftCP, topLeft = Point(-8.95, 2), width = 18, height=1.5, label = 'Rotation Values')
    leftButtons.append(btnRotationValues)
    btnTranslationValues = Button(leftCP, topLeft = Point(-8.95, 0), width = 18, height=1.5, label = 'Translation Values')
    leftButtons.append(btnTranslationValues)
    btnProbability = Button(leftCP, topLeft = Point(-8.95, -2), width = 18, height=1.5, label = 'Probability Values')
    leftButtons.append(btnProbability)
    btnDrawImage = Button(leftCP, topLeft = Point(-8.95, -4), width = 18, height=1.5, label = 'Draw Image')
    leftButtons.append(btnDrawImage)
    btnDrawImage.activate()
    btnViewTransformations = Button(leftCP, topLeft = Point(-8.95, -6), width = 18, height=1.5, label = 'View Transformations')
    btnViewTransformations.activate()
    btnUserManual = Button(leftCP, topLeft = Point(-8.95, -8), width = 1.2, height=0.7, label = '?')
    btnUserManual.activate()
    
    # Buttons for view transformation pop-up window

    
    # Buttons for right control panel

    btnTwoTone = Button(rightCP, topLeft = Point(-8, -6), width = 16, height=1.5, label = 'Two Tone')
    btnTwoTone.activate()

    btnMultiColor = Button(rightCP, topLeft = Point(-8, -8), width = 16, height=1.5, label = 'Multi-Color')
    btnMultiColor.activate()
    
    # Text for right control panel

    currentR = Text(Point(-5, 8), "Current R: ")
    currentR.setTextColor('black')
    currentR.setFace('times roman')
    currentR.setSize(20)
    currentR.draw(rightCP)
    values.append(currentR)
    currentS = Text(Point(-5.1, 6.5), "Current S: ")
    currentS.setTextColor('black')
    currentS.setFace('times roman')
    currentS.setSize(20)
    currentS.draw(rightCP)
    values.append(currentS)
    currentTheta = Text(Point(-3.8, 5), "Current Theta: ")
    currentTheta.setTextColor('black')
    currentTheta.setFace('times roman')
    currentTheta.setSize(20)
    currentTheta.draw(rightCP)
    values.append(currentTheta)
    currentPhi = Text(Point(-4.5, 3.5), "Current Phi: ")
    currentPhi.setTextColor('black')
    currentPhi.setFace('times roman')
    currentPhi.setSize(20)
    currentPhi.draw(rightCP)
    values.append(currentPhi)
    currentH = Text(Point(-5, 2), "Current H: ")
    currentH.setTextColor('black')
    currentH.setFace('times roman')
    currentH.setSize(20)
    currentH.draw(rightCP)
    values.append(currentH)
    currentK = Text(Point(-5, 0.5), "Current K: ")
    currentK.setTextColor('black')
    currentK.setFace('times roman')
    currentK.setSize(20)
    currentK.draw(rightCP)
    values.append(currentK)
    currentP = Text(Point(-5.1, -1.5), "Current P: ")
    currentP.setTextColor('black')
    currentP.setFace('times roman')
    currentP.setSize(20)
    currentP.draw(rightCP)
    values.append(currentP)
    currentC = Text(Point(-5, -3), "Current C: ")
    currentC.setTextColor('black')
    currentC.setFace('times roman')
    currentC.setSize(20)
    currentC.draw(rightCP)
    values.append(currentC)
    # Bottom Text Objects and Whatnto
    

    entrySText = Text(Point(2, 0), "Enter S Value: ")
    entrySText.setTextColor('black')
    entrySText.setFace('times roman')
    entrySText.setSize(18)
    
    bottomText.append(entrySText)
    
    entryRText = Text(Point(-5.5, 0), "Enter R Value: ")
    entryRText.setTextColor('black')
    entryRText.setFace('times roman')
    entryRText.setSize(18)
    
    bottomText.append(entryRText)
    
    enterREntry = DblEntry(center = Point(-4,0), width = 6)
    btnEnterR = Button(bottomCP, topLeft = Point(-3.5, 0.8), width = .5, height = 2, label = '✓')
    btnEnterR.undraw()
    enterSEntry = DblEntry(center = Point(3.5,0), width = 6)
    btnEnterS = Button(bottomCP, topLeft = Point(4, 0.8), width = .5, height = 2, label = '✓')
    btnEnterS.undraw()
    
    bottomEntry.append(enterREntry)
    bottomEntry.append(enterSEntry)
    bottomText.append(btnEnterR)
    bottomText.append(btnEnterS)
    
    entryThetaText = Text(Point(2, 0), "Enter Theta Value: ")
    entryThetaText.setTextColor('black')
    entryThetaText.setFace('times roman')
    entryThetaText.setSize(18)
    
    bottomText.append(entryThetaText)
    
    entryPhiText = Text(Point(-5.5, 0), "Enter Phi Value: ")
    entryPhiText.setTextColor('black')
    entryPhiText.setFace('times roman')
    entryPhiText.setSize(18)

    bottomText.append(entryPhiText)
    
    enterThetaEntry = DblEntry(center = Point(-4,0), width = 6, span = [0, 360])
    btnEnterTheta = Button(bottomCP, topLeft = Point(-3.5, 0.8), width = .5, height = 2, label = '✓')
    btnEnterTheta.undraw()
    enterPhiEntry = DblEntry(center = Point(3.5,0), width = 6, span = [0, 360])
    btnEnterPhi = Button(bottomCP, topLeft = Point(4, 0.8), width = .5, height = 2, label = '✓')
    btnEnterPhi.undraw()
    
    bottomEntry.append(enterThetaEntry)
    bottomEntry.append(enterPhiEntry)
    bottomButtons.append(btnEnterTheta)
    bottomButtons.append(btnEnterPhi)

    entryHText = Text(Point(2, 0), "Enter H Value: ")
    entryHText.setTextColor('black')
    entryHText.setFace('times roman')
    entryHText.setSize(18)
    
    bottomText.append(entryHText)
    
    entryKText = Text(Point(-5.5, 0), "Enter K Value: ")
    entryKText.setTextColor('black')
    entryKText.setFace('times roman')
    entryKText.setSize(18)
    
    bottomText.append(entryKText)
    
    enterHEntry = DblEntry(center = Point(-4,0), width = 6, span = [0, 1000])
    btnEnterH = Button(bottomCP, topLeft = Point(-3.5, 0.8), width = .5, height = 2, label = '✓')
    btnEnterH.undraw()
    enterKEntry = DblEntry(center = Point(3.5,0), width = 6, span = [0, 1000])
    btnEnterK = Button(bottomCP, topLeft = Point(4, 0.8), width = .5, height = 2, label = '✓')
    btnEnterK.undraw()
    
    bottomEntry.append(enterHEntry)
    bottomEntry.append(enterKEntry)
    bottomButtons.append(btnEnterH)
    bottomButtons.append(btnEnterK)

    entryPText = Text(Point(-5.5, 0), "Enter P Value: ")
    entryPText.setTextColor('black')
    entryPText.setFace('times roman')
    entryPText.setSize(18)
    
    bottomText.append(entryPText)
    
    enterPEntry = IntEntry(center = Point(-4,0), width = 6, span = [0, 100])
    btnEnterP = Button(bottomCP, topLeft = Point(-3.5, 0.8), width = .5, height = 2, label = '✓')
    btnEnterP.undraw()
    
    bottomEntry.append(enterPEntry)
    bottomButtons.append(btnEnterP)
    
    btnZoomIn = Button(bottomCP, topLeft = Point(6, 6), width = 3, height = 3, label = 'Zoom In')
    btnZoomIn.undraw()

    btnZoomOut = Button(bottomCP, topLeft = Point(6, 3), width = 3, height = 3, label = 'Zoom Out')
    btnZoomOut.undraw()

    btnClear = Button(bottomCP, topLeft = Point(6, 0), width = 3,  height = 3, label = 'Clear')
    btnClear.undraw()
    
    bottomButtons.append(btnZoomIn)
    bottomButtons.append(btnZoomOut)
    bottomButtons.append(btnClear)
    
    # Right control panel text
    rValue = Text(Point(-.7, 8), '0.5')
    rValue.setTextColor('black')
    rValue.setFace('times roman')
    rValue.setSize(20)

    sValue = Text(Point(-.8, 6.5), '0.5')
    sValue.setTextColor('black')
    sValue.setFace('times roman')
    sValue.setSize(20)

    thetaValue = Text(Point(1.9, 5), '0.0')
    thetaValue.setTextColor('black')
    thetaValue.setFace('times roman')
    thetaValue.setSize(20)

    phiValue = Text(Point(.5, 3.5), '0.0')
    phiValue.setTextColor('black')
    phiValue.setFace('times roman')
    phiValue.setSize(20)

    hValue = Text(Point(-.3, 2), '0.0')
    hValue.setTextColor('black')
    hValue.setFace('times roman')
    hValue.setSize(20)

    kValue = Text(Point(-.3, 0.5), '0.0')
    kValue.setTextColor('black')
    kValue.setFace('times roman')
    kValue.setSize(20)

    pValue = Text(Point(-.6, -1.5), '1')
    pValue.setTextColor('black')
    pValue.setFace('times roman')
    pValue.setSize(20)
    
    cValue = Text(Point(-.6, -3), 'green')
    cValue.setTextColor('black')
    cValue.setFace('times roman')
    cValue.setSize(20)
    
    def openLink():
        webbrowser.open("https://docs.google.com/document/d/1ahDtVTu9AKk_O2xYiGHnbwD0EDPCAkx8xgp7qEVHdHQ/edit?usp=sharing")
    
    def drawImage():
                pt = (100*rnd(), 100*rnd())
                numTransients = 10000
                numIterations = 100000
                # transient loop (plots)
                for n in range(numTransients):
                # randomly choose a transform
                    t = IFS[randrange(len(IFS))]
                    pt = t.transformPoint(pt[0], pt[1])
        
                for n in range(numIterations):
                    t = IFS[randrange(len(IFS))]
                    pt = t.transformPoint(pt[0], pt[1])
                    imageWin.plot(pt[0], pt[1], t.getColor())
    
    running = True
    edit = False
    while running:
        if edit == False:
            args = [0.5, 0.5, 360, 360, 0.25, 0.5, 1, 'green']
            if len(IFS) > 0:
                val = len(IFS)-1
            elif len(IFS) == 0:
                val = 0
        rightPt = rightCP.getMouseAsync()
        leftPt = leftCP.getMouseAsync()
        bottomPt = bottomCP.getMouseAsync()
        counter2 = 0
        
        if leftPt:
            bottomPt = bottomCP.getMouseAsync()
            if btnExit.clicked(leftPt):
                for win in windows:
                    win.close()
                running = False
            elif btnNewTransformation.clicked(leftPt):
                counter2 += 1
                args = [0.5, 0.5, 360, 360, 0.25, 0.5, 1, 'green']
                for btn in leftButtons:
                    if btn.isDrawn():
                        btn.deactivate()
                btnScalingValues.activate()
                btnRotationValues.activate()
                btnTranslationValues.activate()
                btnProbability.activate()
                btnCompleteTransformation.activate()
                for text in values:
                    if text.isDrawn() == False:
                        text.draw()
                
            elif btnCompleteTransformation.clicked(leftPt):
                if edit == True:
                    edit = False
                
                btnScalingValues.deactivate()
                btnRotationValues.deactivate()
                btnTranslationValues.deactivate()
                btnProbability.deactivate()
                btnCompleteTransformation.deactivate()
                IFS.insert(val, IFS_Transform(args))
                for btn in bottomButtons:
                    if btn.isDrawn():
                        btn.undraw()
                        btn.deactivate()
                for text in bottomText:
                    if text.isDrawn():
                        text.undraw()
                for entry in bottomEntry:
                    if entry.isDrawn():
                        entry.undraw()
                args = [0.5, 0.5, 360, 360, 0.25, 0.5, 1, 'green']
                btnNewTransformation.activate()
                btnDrawImage.activate()
            elif btnScalingValues.clicked(leftPt):
                for btn in bottomButtons:
                    if btn.isDrawn():
                        btn.undraw()
                        btn.deactivate()
                for text in bottomText:
                    if text.isDrawn():
                        text.undraw()
                for entry in bottomEntry:
                    if entry.isDrawn():
                        entry.undraw()
                entryRText.draw(bottomCP)
                enterREntry.draw(bottomCP)
                btnEnterR.draw(bottomCP)
                btnEnterR.activate()
                entrySText.draw(bottomCP)
                enterSEntry.draw(bottomCP)
                btnEnterS.draw(bottomCP)
                btnEnterS.activate()
        
            elif btnRotationValues.clicked(leftPt):
                for btn in bottomButtons:
                    if btn.isDrawn():
                        btn.undraw()
                        btn.deactivate()
                for text in bottomText:
                    if text.isDrawn():
                        text.undraw()
                for entry in bottomEntry:
                    if entry.isDrawn():
                        entry.undraw()
                entryThetaText.draw(bottomCP)
                enterThetaEntry.draw(bottomCP)
                btnEnterTheta.draw(bottomCP)
                btnEnterTheta.activate()
                entryPhiText.draw(bottomCP)
                enterPhiEntry.draw(bottomCP)
                btnEnterPhi.draw(bottomCP)
                btnEnterPhi.activate()
                
            elif btnTranslationValues.clicked(leftPt):
                for btn in bottomButtons:
                    if btn.isDrawn():
                        btn.undraw()
                        btn.deactivate()
                for text in bottomText:
                    if text.isDrawn():
                        text.undraw()
                for entry in bottomEntry:
                    if entry.isDrawn():
                        entry.undraw()
                entryHText.draw(bottomCP)
                enterHEntry.draw(bottomCP)
                btnEnterH.draw(bottomCP)
                btnEnterH.activate()
                entryKText.draw(bottomCP)
                enterKEntry.draw(bottomCP)
                btnEnterK.draw(bottomCP)
                btnEnterK.activate()
                
            elif btnProbability.clicked(leftPt):
                for btn in bottomButtons:
                    if btn.isDrawn():
                        btn.undraw()
                        btn.deactivate()
                for text in bottomText:
                    if text.isDrawn():
                        text.undraw()
                for entry in bottomEntry:
                    if entry.isDrawn():
                        entry.undraw()
                entryPText.draw(bottomCP)
                enterPEntry.draw(bottomCP)
                btnEnterP.draw(bottomCP)
                btnEnterP.activate()
                
            elif btnDrawImage.clicked(leftPt):
                for btn in bottomButtons:
                    if btn.isDrawn():
                        btn.undraw()
                        btn.deactivate()
                for text in bottomText:
                    if text.isDrawn():
                        text.undraw()
                for entry in bottomEntry:
                    if entry.isDrawn():
                        entry.undraw()
                IFS.append(IFS_Transform([0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 4, 'green']))
                IFS.append(IFS_Transform([0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 4, 'blue']))
                IFS.append(IFS_Transform([0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 4, 'yellow']))
                btnZoomIn.draw(bottomCP)
                btnZoomIn.activate()
                btnZoomOut.draw(bottomCP)
                btnZoomOut.activate()
                btnClear.draw(bottomCP)
                btnClear.activate()
                
                drawImage()

                
            elif btnViewTransformations.clicked(leftPt):
                viewWin = DEGraphWin(width = 700, height = 600, offsets = (375, 300), defCoords = [-10, -10, 10, 10], hasTitlebar = False)
                btnExitView = Button(viewWin, topLeft = Point(8.3, 9), width = 1, height=1, label = 'X')
                btnExitView.activate()
                btnEditOrDelete = Button(viewWin, topLeft = Point(-2, 9), width = 4, height=1, label = 'Edit/Delete')
                btnEditOrDelete.activate()
                IFS.append(IFS_Transform([0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 4, 'black']))
                IFS.append(IFS_Transform([0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 4, 'black']))
                IFS.append(IFS_Transform([0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 4, 'black']))
                transformationList = Text(Point(-1.5, -3), '')
                transformationList.setTextColor('black')
                transformationList.setFace('times roman')
                transformationList.setSize(16)
                counter = 1
                for ifs in IFS:
                    transformationList.setText(transformationList.getText() + "Transformation " +  str(counter) + ":" "  R: " + str(ifs.getR()) + "  S: " + str(ifs.getS()) + "  Theta: " + str(ifs.getTheta()) + "  Phi:  " + str(ifs.getPhi()) + "  H: " + str(ifs.getE()) + "  K: " + str(ifs.getF()) + "  P: " + str(ifs.getProb()) + "  C: " + str(ifs.getColor())  + '\n' + '\n')
                    counter += 1
                transformationList.draw(viewWin)
                status = True
                while status:
                    viewPt = viewWin.getMouse()
                    if btnExitView.clicked(viewPt):
                        viewWin.close()
                        status = False
                    if btnEditOrDelete.clicked(viewPt):
                        editWin = DEGraphWin(width = 300, height = 300, offsets = (600, 100), defCoords = [-10, -10, 10, 10], hasTitlebar = False)
                        btnEdit = Button(editWin, topLeft = Point(-8, 8), width = 5, height=1.5, label = 'Edit')
                        btnEdit.activate()
                        btnDelete = Button(editWin, topLeft = Point(-8, 5.5), width = 5, height=1.5, label = 'Delete')
                        btnDelete.activate()
                        btnExitEdit = Button(editWin, topLeft = Point(8.3, 9), width = 1, height=1, label = 'X')
                        btnExitEdit.activate()
                        status2 = True
                        while status2:
                            editPt = editWin.getMouse()
                            if btnExitEdit.clicked(editPt):
                                editWin.close()
                                status2 = False
                            if btnEdit.clicked(editPt):
                                chooseEditWin = DEGraphWin(width = 300, height = 300, offsets = (600, 100), defCoords = [-10, -10, 10, 10], hasTitlebar = False)
                                enterTValue = IntEntry(center = Point(0, 0), width = 6, span = [1, 20])
                                enterTValue.draw(chooseEditWin)
                                btnEditT = Button(chooseEditWin, topLeft = Point(3.3, 0.7), width = 2, height=1.5, label = '✓')
                                btnEditT.activate()
                                status3 = True
                                while status3:
                                    editPt = chooseEditWin.getMouse()
                                    if btnEditT.clicked(editPt):
                                        args = [IFS[enterTValue.getValue() - 1].getR(), IFS[enterTValue.getValue() - 1].getS(), IFS[enterTValue.getValue() - 1].getTheta(), IFS[enterTValue.getValue() - 1].getPhi(), IFS[enterTValue.getValue() - 1].getE(), IFS[enterTValue.getValue() - 1].getF(), IFS[enterTValue.getValue() - 1].getProb(), IFS[enterTValue.getValue() - 1].getColor()]
                                        rValue.setText(str(args[0]))
                                        sValue.setText(str(args[1]))
                                        thetaValue.setText(str(args[2]))
                                        phiValue.setText(str(args[3]))
                                        hValue.setText(str(args[4]))
                                        kValue.setText(str(args[5]))
                                        pValue.setText(str(args[6]))
                                        color = args[7]
                                        IFS.pop(enterTValue.getValue() - 1)
                                        val = enterTValue.getValue()-1
                                        edit = True
                                        chooseEditWin.close()
                                        editWin.close()
                                        viewWin.close()
                                        status = False
                                        status2 = False
                                        status3 = False
                            if btnDelete.clicked(editPt):
                                chooseDeleteWin = DEGraphWin(width = 300, height = 300, offsets = (600, 100), defCoords = [-10, -10, 10, 10], hasTitlebar = False)
                                enterTValue = IntEntry(center = Point(0, 0), width = 6, span = [1, 20])
                                enterTValue.draw(chooseDeleteWin)
                                btnDeleteT = Button(chooseDeleteWin, topLeft = Point(3.3, 0.7), width = 2, height=1.5, label = '✓')
                                btnDeleteT.activate()
                                status4 = True
                                while status4:
                                    deletePt = chooseDeleteWin.getMouse()
                                    if btnDeleteT.clicked(deletePt):
                                        IFS.pop(enterTValue.getValue() - 1)
                                        status = False
                                        status2 = False
                                        status3 = False
                                        status4 = False
                                        chooseDeleteWin.close()
                                        editWin.close()
                                        viewWin.close()
                    

            elif btnUserManual.clicked(leftPt):
                openLink()
        
        if rightPt:
            if btnTwoTone.clicked(rightPt):
                background = askcolor(title = "Choose a background color")
                imageWin.setBackground(background[1])
                IFSColor = askcolor(title = "Choose a color for the IFS Scheme")
                for ifs in IFS:
                    ifs.setColor(IFSColor[1])
                
            elif btnMultiColor.clicked(rightPt):
                print(range(len(IFS)))
                for ifs in IFS:
                    ifs.setColor(askcolor(title = "Choose a color for the IFS Scheme")[1])
        
        if bottomPt:
            if btnEnterR.clicked(bottomPt):
                args[0] = enterREntry.getValue()
                rValue.setText(str(args[0]))
            elif btnEnterS.clicked(bottomPt):
                args[1] = enterSEntry.getValue()
                sValue.setText(str(args[1]))
            elif btnEnterTheta.clicked(bottomPt):
                args[2] = enterThetaEntry.getValue()
                thetaValue.setText(str(args[2]))
            elif btnEnterPhi.clicked(bottomPt):
                args[3] = enterPhiEntry.getValue()
                phiValue.setText(str(args[3]))
            elif btnEnterH.clicked(bottomPt):
                args[4] = enterHEntry.getValue()
                hValue.setText(str(args[4]))
            elif btnEnterK.clicked(bottomPt):
                args[5] = enterKEntry.getValue()
                kValue.setText(str(args[5]))
            elif btnEnterP.clicked(bottomPt):
                args[6] = enterPEntry.getValue()
                pValue.setText(str(args[6]))
            elif btnZoomIn.clicked(bottomPt):
                imageWin.zoom()
                drawImage()
            elif btnZoomOut.clicked(bottomPt):
                imageWin.zoom('out')
                drawImage()
            elif btnClear.clicked(bottomPt):
                imageWin.clear()
            
            
        rightPt = None
        leftPt = None
        bottomPt = None
    

    
main()