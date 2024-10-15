from math import radians, cos, sin

class IFS_Transform:

    def __init__(self, parameters):
        # Assume parameters is a list: [r, s, theta, phi, h, k, p, c]
        if len(parameters) != 8:
            raise ValueError("Parameters list must contain 8 elements.")
        self.r = parameters[0]  # xScale
        self.s = parameters[1]  # yScale
        self.theta = parameters[2]  # theta
        self.phi = parameters[3]  # phi
        self.e = parameters[4]  # h
        self.f = parameters[5]  # k
        self.prob = parameters[6]  # p
        self.color = parameters[7]  # c

        # Convert angles from degrees to radians for internal calculations
        self.thetaRadians = radians(self.theta)
        self.phiRadians = radians(self.phi)

    def setR(self, xScale):
        self.r = xScale

    def setS(self, yScale):
        self.s = yScale

    def setTheta(self, angle):
        self.theta = angle
        self.thetaRadians = radians(self.theta)

    def setPhi(self, angle):
        self.phi = angle
        self.phiRadians = radians(self.phi)

    def setHshift(self, shift):
        self.e = shift

    def setVshift(self, shift):
        self.f = shift

    def setProb(self, prob):
        self.prob = prob

    def setColor(self, myColor):
        self.color = myColor

    def getR(self):
        return self.r

    def getS(self):
        return self.s

    def getTheta(self):
        return self.theta

    def getPhi(self):
        return self.phi

    def getE(self):
        return self.e

    def getF(self):
        return self.f

    def getProb(self):
        return self.prob

    def getColor(self):
        return self.color

    def transformPoint(self, x, y):
        newX = x * self.r * cos(self.thetaRadians) - y * self.s * sin(self.phiRadians) + self.e
        newY = x * self.r * sin(self.thetaRadians) + y * self.s * cos(self.phiRadians) + self.f
        return newX, newY

    def __str__(self):
        # toString method remains unchanged
        result = '[scale(' + str(self.r) + ',' + str(self.s) + '), '
        result += 'rot(' + str(self.theta) + ',' + str(self.phi) + '), '
        result += 'trans(' + str(self.e) + ',' + str(self.f) + '), '
        result += 'prob(' + str(self.prob) + '), '
        result += 'col(' + str(self.color) + ')]'
        return result
