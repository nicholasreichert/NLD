import numpy as np
import time
from DEgraphics import *

class CA:
    def __init__(self, size=100, colors=['black', 'white'], is_totalistic=True):
        self.size = size
        self.is_totalistic = is_totalistic
        self.display = DEGraphWin(title="CA2D", width=700, height=700,
                                  defCoords=[0, 0, 700, 700], offsets=[300, 0],
                                  autoflush=False, hasTitlebar=False)
        self.numRows = self.display.height // self.size
        self.numCols = self.display.width // self.size
        self.display.grid(self.size, self.size)
        self.liveCells = []
        self.nbrHood = 9  # Moore neighborhood, 5 for von Neumann
        self.nbrCount = np.zeros((self.numRows, self.numCols)).astype(int)
        self.stateSpace = np.zeros((self.numRows, self.numCols)).astype(int)
        self.nearest = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        self.totalCells = self.numRows * self.numCols
        self.toggledCells = []  # Keep track of which cells are on
        self.rule = {0: [3], 1: [2, 3]} if is_totalistic else {0: set(), 1: set()}  # Initialize rules
        self.colorOn = colors[0]
        self.colorOff = colors[1]

    def setTotalistic(self, is_totalistic):
        self.is_totalistic = is_totalistic
        if self.is_totalistic:
            self.rule = {0: [3], 1: [2, 3]}  # Default totalistic rules
        else:
            self.rule = {0: set(), 1: set()}  # Clear non-totalistic rules

    def toggleCell(self, cellNum=1):
        while len(self.toggledCells) < cellNum:
            pt = self.display.getMouse()
            col = int(pt.getX() // self.size)
            row = int(pt.getY() // self.size)

            if 0 <= row < self.numRows and 0 <= col < self.numCols:
                if (row, col) in self.toggledCells:
                    self.toggledCells.remove((row, col))
                    self.stateSpace[row, col] = 0  # Set cell to OFF
                    self.updateNbrCount()
                    self.updateDisplay()
                else:
                    if len(self.toggledCells) < cellNum:
                        self.toggledCells.append((row, col))
                        self.stateSpace[row, col] = 1  # Set cell to ON
                        self.updateNbrCount()
                        self.updateDisplay()
                    else:
                        last_row, last_col = self.toggledCells[-1]
                        self.stateSpace[last_row, last_col] = 1  # Ensure the last cell is ON
                        self.updateNbrCount()
                        self.updateDisplay()
                        break
            else:
                print("Clicked outside grid boundaries.")

    def updateNbrCount(self):
        for row in range(self.numRows):
            for col in range(self.numCols):
                self.__updateLiveNbrCount(row, col)

    def setCellSize(self, size):
        if size < 5:
            size = 5


        self.size = size
        self.numRows = self.display.height // self.size
        self.numCols = self.display.width // self.size
        self.stateSpace = np.zeros((self.numRows, self.numCols)).astype(int)
        self.nbrCount = np.zeros((self.numRows, self.numCols)).astype(int)

        self.display.clear()
        self.display.grid(self.size, self.size)
        self.updateDisplay()

    def __updateLiveNbrCount(self, row, col):
        self.nbrCount[row, col] = 0

        if self.nbrHood == 9:
            nbrOffsets = self.nearest
        elif self.nbrHood == 5:
            nbrOffsets = self.nearest[:5]

        for changeRowVal, changeColVal in nbrOffsets:
            if changeRowVal == 0 and changeColVal == 0:
                continue
            
            n_row = (row + changeRowVal) % self.numRows
            n_col = (col + changeColVal) % self.numCols
            
            if n_row < 0:
                n_row = self.numRows - 1
            if n_col < 0:
                n_col = self.numCols - 1
            
            self.nbrCount[row, col] += self.stateSpace[n_row, n_col]

    def updateDisplay(self):
        for cell in self.liveCells:
            cell.undraw()
        self.liveCells = []

        for r in range(self.numRows):
            for c in range(self.numCols):
                topLeft = Point(c * self.size, r * self.size)
                bottomRight = Point((c + 1) * self.size, (r + 1) * self.size)

                cell = Rectangle(topLeft, bottomRight)
                if self.stateSpace[r, c] == 1:
                    cell.setFill(self.colorOn)
                else:
                    cell.setFill(self.colorOff)

                cell.draw(self.display)
                self.liveCells.append(cell)

    def advance(self):
        newSpace = np.copy(self.stateSpace)
        for row in range(self.numRows):
            for col in range(self.numCols):
                state = self.stateSpace[row, col]
                if self.is_totalistic:
                    nbrs = self.nbrCount[row, col]
                    if nbrs in self.rule[state]:
                        newSpace[row, col] = 1
                    else:
                        newSpace[row, col] = 0
                else:
                    neighbors = self.getNeighborsBinary(row, col)
                    if (state, neighbors) in self.rule[state]:
                        newSpace[row, col] = 1
                    else:
                        newSpace[row, col] = 0
        self.stateSpace = newSpace
        self.updateNbrCount()
        self.updateDisplay()

    def getNeighbors(self, row, col):
        if self.is_totalistic:
            return self.nbrCount[row, col]
        else:
            return self.getNeighborsBinary(row, col)

    def getNeighborsBinary(self, row, col):
        binary = 0
        for i, (changeRowVal, changeColVal) in enumerate(self.nearest):
            if changeRowVal == 0 and changeColVal == 0:
                continue
            n_row = (row + changeRowVal) % self.numRows
            n_col = (col + changeColVal) % self.numCols
            if n_row < 0:
                n_row = self.numRows - 1
            if n_col < 0:
                n_col = self.numCols - 1
            if self.stateSpace[n_row, n_col] == 1:
                binary |= (1 << i)
        return binary

    def run(self, numSteps=1, delay=0.1):
        for n in range(numSteps):
            self.advance()
            self.display.update()  # Ensure the display updates with each step
            time.sleep(delay)  # Introduce the delay between generations
        self.display.update()  # Update the display for the final generation
        time.sleep(delay*3)

    def getMouse(self):
        return self.display.getMouse()

    def pause(self, seconds=0.1):
        self.display.checkMouse(seconds)

    def close(self):
        if not self.display.isClosed():
            self.display.close()

    def updateRule(self, state, newRuleSet):
        self.rule[state] = newRuleSet

    def getRule(self, state):
        return self.rule[state]

    def addRule(self, state, pattern):
        self.rule[state].add(pattern)

    def removeRule(self, state, pattern):
        self.rule[state].remove(pattern)
