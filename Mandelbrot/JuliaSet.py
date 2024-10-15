from DEgraphics import *
import numpy as np
from random import random

class JuliaSet:
    def __init__ (self, pixelWidth, pixelHeight):
        self.window = DEGraphWin(title = "Julia Set", width = pixelWidth, height = pixelHeight, defCoords = [-2,-2,2,2], hasTitlebar = False, offsets = [150, 100], hBGColor = '#212529')
        self.window.setBackground('#343A40')
        self.maxIterates = 250
    
    def setMaxIterates(self, iterates):
        self.maxIterates = iterates

    def regPlotSet(self, const = .365 - 0.37j):
        y, x = np.ogrid[self.window.currentCoords[1]:self.window.currentCoords[3]:self.window.height*1j, self.window.currentCoords[0]:self.window.currentCoords[2]:self.window.width*1j]
        c = x + y*1j
        z = c
        divergeIter = self.maxIterates + np.zeros(z.shape, dtype=int)

        for i in range(self.maxIterates):
            z = z**2 + const
            diverge = abs(z) >= 2
            divergingNow = diverge & (divergeIter == self.maxIterates)
            divergeIter[divergingNow] = i
            z[diverge] = 2

        for i in range(len(c)):
            for ii in range(len(c[i])):
                it = divergeIter[i][ii]
                if it != self.maxIterates:
                    z = c[i][ii]
                    color = it * 2
                    if color > 255:
                        color = 255
                    self.window.plot(z.real, z.imag, color_rgb(color, color, color))
        self.window.update()
        
    def inversePlotSet(self, const = .365 - 0.37j):
        def g(z, c = const):
            i = 1
            if random() < .5:
                i = -1
            return i * (z-c) ** 0.5
        
        z = complex(-3+ 3 *random(), -3+ 3*random())

        for i in range (10000):
            z = g(z)

        for i in range(10000):
            z = g(z)
            self.window.plot(z.real, z.imag, 'black')

    def zoom(self, inout="in", constan = .365 - 0.37j, algType = 'Regular'):
        self.window.zoom(inout)
        if(algType == 'Regular'):
             self.regPlotSet(const = constan)
        elif(algType == 'Inverse'):
            self.inversePlotSet(const = constan)

if __name__ == '__main__':
    m = JuliaSet(800, 800)
    m.inversePlotSet()

#0
#1j
#-1j
#-0.123 + 0.745j
#-0.77 + 0.22j
#.365 - 0.37j
#-0.8+0.156j
#-0.835-0.2321j
#-0.4+0.6j
#0.279