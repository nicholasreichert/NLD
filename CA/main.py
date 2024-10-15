from CAUtils import *
from tkinter import Checkbutton, IntVar, Radiobutton

windows = []
patternGridWidgets = []
gridToCellsize = {
    5: 140,
    6: 116,
    7: 100,
    8: 87,
    9: 78,
    10: 70,
    11: 63,
    12: 58,
    13: 54,
    14: 50,
    15: 47,
    16: 44,
    17: 41,
    18: 39,
    19: 37,
    20: 35,
    21: 33,
    22: 31,
    23: 30,
    24: 29,
    25: 28
}

def updateRulesDisplay(ca, rulesText):
    rulesText.setText(f"OFF to ON: {ca.rule[0]}\nON to ON: {ca.rule[1]}")

def main():
    global totalistic
    totalistic = True

    # main window created with CA2D initialization
    ca = CA(size=140, is_totalistic=totalistic)

    # bottom control panel for buttons  
    bottomCP = DEGraphWin(width=700, height=150, offsets=(300, 700), defCoords=[-10, -10, 10, 10], hasTitlebar=True, hBGColor='#7F7979')
    bottomCP.setBackground('#323031')
    windows.append(bottomCP)
    
    rightCP = DEGraphWin(width=200, height=700, offsets=(1000, 0), defCoords=[-10, -10, 10, 10], hasTitlebar=True, hBGColor='#7F7979')
    rightCP.setBackground('#323031')
    windows.append(rightCP)
    
    botRightSquare = DEGraphWin(width=200, height=150, offsets=(1000, 700), defCoords=[-10, -10, 10, 10], hasTitlebar=False, hBGColor='#7F7979')
    botRightSquare.setBackground('#323031')
    windows.append(botRightSquare)

    btnExit = Button(bottomCP, topLeft=Point(8.5, 8.5), width=1, height=3, 
                     label='X', buttonColors=['#C1BDB3', '#3D3B3C', 'black'], 
                     clickedColors=['#3D3B3C', '#5F5B6B', 'black'])
    btnExit.activate()

    btnClear = Button(bottomCP, topLeft=Point(6.5, 4), width=3, height=3, 
                      label='Clear', buttonColors=['#C1BDB3', '#3D3B3C', 'black'], 
                      clickedColors=['#3D3B3C', '#5F5B6B', 'black'])
    btnClear.activate()

    btnMoore = Button(bottomCP, topLeft=Point(3, 7), width=3, height=3, 
                      label='Moore', buttonColors=['#C1BDB3', '#3D3B3C', 'black'], 
                      clickedColors=['#3D3B3C', '#5F5B6B', 'black'])

    btnNeumann = Button(bottomCP, topLeft=Point(3, 3), width=3, height=3, 
                        label='Neumann', buttonColors=['#C1BDB3', '#3D3B3C', 'black'], 
                        clickedColors=['#3D3B3C', '#5F5B6B', 'black'])
    btnNeumann.activate()

    btnTotalistic = Button(botRightSquare, topLeft=Point(-9.5, 0), width=19, height=3, 
                           label='Change Totalistic', buttonColors=['#C1BDB3', '#3D3B3C', 'black'], 
                           clickedColors=['#3D3B3C', '#5F5B6B', 'black'])
    btnTotalistic.activate()

    ruleOffCheckbox = RuleCheckBox(Point(-5, 3), choices=[str(i) for i in range(9)], label="Rules (OFF)", font=('times new roman', 14), bg='#323031')
    ruleOffCheckbox.draw(rightCP)
    
    ruleOnCheckbox = RuleCheckBox(Point(5, 3), choices=[str(i) for i in range(9)], label="Rules (ON)", font=('times new roman', 14), bg='#323031')
    ruleOnCheckbox.draw(rightCP)

    genNumSlider = Slider(p=Point(-7, 4), length=200, height=10, min=1, max=500, font=('times new roman', 14), 
                          label="Gen #", bg="#7F7979", trColor="#7F7979")
    genNumSlider.draw(bottomCP)

    startingCellSlider = Slider(p=Point(-7, -4), length=200, height=10, min=1, max=ca.totalCells, font=('times new roman', 14), 
                                label="# Cells to Start With", bg="#7F7979", trColor="#7F7979")
    startingCellSlider.draw(bottomCP)

    speedSlider = Slider(p=Point(4, -4), length=200, height=10, min=1, max=10, font=('times new roman', 14), 
                         label="Delay (s)", bg="#7F7979", trColor="#7F7979")
    speedSlider.draw(bottomCP)

    cellSizeDropdown = DropDown(topLeft=Point(-2, 3), choices=['5x5', '6x6', '7x7', '8x8', '9x9', '10x10',
                                                               '11x11', '12x12', '13x13', '14x14', '15x15',
                                                               '16x16', '17x17', '18x18', '19x19', '20x20',
                                                               '21x21', '22x22', '23x23', '24x24', '25x25'], font=('times new roman', 14),
                                 bg='#7F7979')
    cellSizeDropdown.draw(bottomCP)

    runTypeDropdown = DropDown(topLeft=Point(-2, -5), choices=['Automatic', 'Manual'], font=('times new roman', 14),
                               bg='#7F7979')
    runTypeDropdown.draw(bottomCP)

    csText = Text(Point(-1.9, 6), "Set Gridsize: ")
    csText.setFace('times roman')
    csText.setSize(14)
    csText.setTextColor('#C1BDB3')
    csText.draw(bottomCP)

    runTypeText = Text(Point(-1.9, -2), "Set Run Type: ")
    runTypeText.setFace('times roman')
    runTypeText.setSize(14)
    runTypeText.setTextColor('#C1BDB3')
    runTypeText.draw(bottomCP)

    rulesText = Text(Point(0, 8), f"OFF to ON: {sorted(ca.rule[0])}\nON to ON: {sorted(ca.rule[1])}")
    rulesText.setFace('times roman')
    rulesText.setSize(12)
    rulesText.setTextColor('#C1BDB3')
    rulesText.draw(rightCP)

    totalisticText = Text(Point(0, 4), "Totalistic")
    totalisticText.setFace('times roman')
    totalisticText.setSize(16)
    totalisticText.setTextColor('#C1BDB3')
    totalisticText.draw(botRightSquare)

    def addRuleCallback():
        pattern = [patternGridVars[i][j].get() for i in range(3) for j in range(3)]
        state = stateVar.get()
        rule_str = ''.join(str(x) for x in pattern)
        rule_num = int(rule_str, 2)
        if state == 0:
            ca.rule[0].add(rule_num)
        else:
            ca.rule[1].add(rule_num)
        updateRulesDisplay(ca, rulesText)
        print(ca.rule)

    btnAddRule = tk.Button(rightCP, text="Add Rule", command=addRuleCallback, bg='#3D3B3C', fg='#C1BDB3')
    btnAddRule.place(x=70, y=670)  # Adjust x and y values as needed
    
    def toggleRuleCreationUI(enable):
        state = tk.NORMAL if enable else tk.DISABLED
        for widget in patternGridWidgets:
            widget.configure(state=state)
        btnAddRule.configure(state=state)
        state0.configure(state=state)
        state1.configure(state=state)

    def toggleTotalistic():
        global totalistic
        totalistic = not totalistic
        ca.setTotalistic(totalistic)
        totalisticText.setText("Totalistic" if totalistic else "Non-Totalistic")
        toggleRuleCreationUI(not totalistic)

    # Add pattern grid and state selection for non-totalistic rules
    stateVar = IntVar()
    state0 = Radiobutton(rightCP, text="OFF", variable=stateVar, value=0, bg='#323031', fg='#C1BDB3')
    state1 = Radiobutton(rightCP, text="ON", variable=stateVar, value=1, bg='#323031', fg='#C1BDB3')
    state0.place(x=30, y=500)
    state1.place(x=100, y=500)

    patternGridVars = [[IntVar() for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            cb = Checkbutton(rightCP, variable=patternGridVars[i][j], bg='#323031', fg='#C1BDB3')
            cb.place(x=55 + j * 30, y=600 - i * 30)
            patternGridWidgets.append(cb)
            
    toggleRuleCreationUI(not totalistic)

    # Function to handle checkbox changes
    def handleCheckbox(state, rule, var, ca, rulesText):
        if var.get() == 1:
            ca.rule[state].add(rule)
        else:
            ca.rule[state].remove(rule)
        updateRulesDisplay(ca, rulesText)

    def checkbox_callback():
        ca.rule[0] = ruleOffCheckbox.getSelections()
        ca.rule[1] = ruleOnCheckbox.getSelections()
        updateRulesDisplay(ca, rulesText)

    # Set the callback for the checkboxes
    ruleOffCheckbox.setCallback(checkbox_callback)
    ruleOnCheckbox.setCallback(checkbox_callback)

    def setMoore():
        ca.nbrHood = 9
        ca.nearest = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        ca.updateNbrCount()
        updateRulesDisplay(ca, rulesText)

    def setNeumann():
        ca.nbrHood = 5
        ca.nearest = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
        ca.updateNbrCount()
        updateRulesDisplay(ca, rulesText)

    running = True
    while running:
        bottomPt = bottomCP.getMouseAsync()
        mainPt = ca.display.getMouseAsync()
        botSquarePt = botRightSquare.getMouseAsync()
        
        dropVal = cellSizeDropdown.getChoice()
        dropValPart = int(dropVal.split('x')[0])
        gridSize = gridToCellsize.get(dropValPart)

        if ca.size != gridSize:
            ca.setCellSize(gridSize)

        genNumVal = genNumSlider.getValue()
        startingCellNum = startingCellSlider.getValue()

        if bottomPt:
            if btnExit.clicked(bottomPt):
                for win in windows:
                    win.close()
                ca.close()
                running = False
            if btnClear.clicked(bottomPt):
                genNumSlider.setValue(1)
                startingCellSlider.setValue(1)
                dropVal = '5x5'
                ca.setCellSize(140)
                runTypeDropdown.setValue('Automatic')
                cellSizeDropdown.setValue('5x5')
                ruleOffCheckbox.setSelections(ca.rule[0])
                ruleOnCheckbox.setSelections(ca.rule[1])
                updateRulesDisplay(ca, rulesText)  # Update display on clear
            if btnMoore.clicked(bottomPt):
                btnMoore.deactivate()
                btnNeumann.activate()
                setMoore()
            if btnNeumann.clicked(bottomPt):
                btnMoore.activate()
                btnNeumann.deactivate()
                setNeumann()
                
        if botSquarePt:
            if btnTotalistic.clicked(botSquarePt):
                if totalistic == True:
                    totalistic = False
                    totalisticText.setText("Non-Totalistic")
                    ca.setTotalistic(totalistic)
                    toggleRuleCreationUI(True)
                else:
                    totalistic = True
                    totalisticText.setText("Totalistic")
                    ca.setTotalistic(totalistic)
                    toggleRuleCreationUI(False)
                
        if runTypeDropdown.getChoice() == 'Automatic':
            if mainPt:
                ca.toggleCell(startingCellNum)
                ca.run(genNumVal, delay=speedSlider.getValue())
        else:
            for _ in range(genNumVal):
                mainPt = ca.display.getMouse()
                if mainPt:
                    ca.toggleCell(startingCellNum)
                    ca.run(1, delay=speedSlider.getValue())
                    mainPt = None
                    break
        
        bottomPt = None
        mainPt = None
        botSquarePt = None

if __name__ == "__main__":
    main()