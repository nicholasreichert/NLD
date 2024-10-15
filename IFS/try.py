from DEgraphics import *
import sys
from transform import *
from random import random as rnd
from random import randrange
sys.path.append("../util")

IFS = []

def main():
    win = DEGraphWin(width = 700, height = 700, offsets = (375, 0), defCoords = [-0.1, -0.1, 1.1, 1.1], hasTitlebar = False)
    
    IFS.append(IFS_Transform([0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 4, 'green']))
    IFS.append(IFS_Transform([0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 4, 'blue']))
    IFS.append(IFS_Transform([0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 4, 'yellow']))
    
    print(IFS)
    pt = (rnd(), rnd())
    numTransients = 10000
    numIterations = 1000
    print(pt)
    print(range(numIterations))
    # transient loop (plots)
    
    # something is wrong with the pt variable, keeps going to (0.0, 0.0) when using transfomrPoint
    # potentially wrong IFS values for pascal's triangle
    # maybe something is wrong with the assigning of variables within the for loops
    for n in range(numTransients):
        # randomly choose a transform
        t = IFS[randrange(len(IFS))]
        print(pt)
        pt = t.transformPoint(pt[0], pt[1])
    print(pt)
    for _ in range(numIterations):
        p = IFS[randrange(len(IFS))]
        pt = p.transformPoint(pt[0], pt[1])
        win.plot(pt[0], pt[1], t.getColor())
    print(pt)
    
    win.getMouse()
    win.close()
    

main()