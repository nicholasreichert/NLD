from DEgraphics import *
import numpy as np

class MandelbrotSet:

    def __init__ (self, pixelWidth, pixelHeight):
        self.window = DEGraphWin(title = "Mandelbrot Set", width = pixelWidth, height = pixelHeight, defCoords = [-2.1,-1.4,.8,1.4], hasTitlebar = False, offsets = [750, 100], hBGColor = '#212529')
        self.window.setBackground('black')
        self.maxIters = 50
    
    def setMaxIterates(self, iterates):
        self.maxIters = iterates

    def exteriorAlg(self):
        y, x = np.ogrid[self.window.currentCoords[1]:self.window.currentCoords[3]:self.window.height*1j, self.window.currentCoords[0]:self.window.currentCoords[2]:self.window.width*1j]
        c = x + y*1j
        z = c
        divergeIter = self.maxIters + np.zeros(z.shape, dtype=int)

        for i in range(self.maxIters):
            z = z**2 + c
            diverge = abs(z) >= 2
            divergingNow = diverge & (divergeIter == self.maxIters)
            divergeIter[divergingNow] = i
            z[diverge] = 2

        for i in range(len(c)):
            for ii in range(len(c[i])):
                it = divergeIter[i][ii]
                if it != self.maxIters:
                    z = c[i][ii]
                    if it <= 40:
                        color = it * 6 + 50
                        if color > 255:
                            color = 255
                        self.window.plot(z.real, z.imag, color_rgb(0, 0, color))
                    else:
                        color = 255 - it * 3
                        if color < 0:
                            color = 1
                        self.window.plot(z.real, z.imag, color_rgb(color, color * 1, 0))
        self.window.update()

    def interiorAlg(self):
        self.window.setCoords(-2, -3, 4.5, 3)
        y, x = np.ogrid[self.window.currentCoords[1]:self.window.currentCoords[3]:self.window.height*1j, self.window.currentCoords[0]:self.window.currentCoords[2]:self.window.width*1j]
        c = x + y*1j
        z = c
        divergeIter = self.maxIters + np.zeros(z.shape, dtype=int)

        for i in range(self.maxIters):
            z = z**2 + c
            diverge = abs(z) >= 2
            divergingNow = diverge & (divergeIter == self.maxIters)
            divergeIter[divergingNow] = i
            z[diverge] = 2

        for i in range(len(c)):
            for ii in range(len(c[i])):
                it = divergeIter[i][ii]
                if it == self.maxIters:
                    z = c[i][ii]
                    if it <= 40:
                        color = it * 6 + 50
                        if color > 255:
                            color = 255
                        self.window.plot(z.real, z.imag, color_rgb(0, 0, color))
                    else:
                        color = 255 - it * 3
                        if color < 0:
                            color = 1
                        self.window.plot(z.real, z.imag, color_rgb(color, color * 1, 0))
        self.window.update()
        
    
    def zoom(self, inout="in", algType = "Exterior"):
        self.window.zoom(inout)
        if(algType == 'Exterior'):
            self.exteriorAlg()
        if(algType == 'Interior'):
            self.interiorAlg()


if __name__ == "__main__":
    m = MandelbrotSet(800, 800)
    m.regPlotSet()
    m.zoom()
    m.zoom()

    m.window.getMouse()
    m.window.close()