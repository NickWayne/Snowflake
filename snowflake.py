import pygame
from pygame import draw
from helperFunctions import isPointInTriangle, rotate, translate, mirror

class Snowflake(object):

    def __init__(self):
        self.baseShape = [(20, 240), (200, 20), (20, 20)]
        self.points = self.baseShape[:]
        self.line = []
        self.snowflakeCenter = (700, 300)

    def render(self, surface, mousePos):
        pygame.draw.polygon(surface, (10, 200, 150), self.points)
        for point in self.points:
            pygame.draw.circle(surface, (255, 255, 255), point, 2)
        self.renderLine(surface, mousePos)

    def renderLine(self, surface, mousePos):
        if (len(self.line) >= 1):
            
            for i in range(len(self.line) - 1):
                pygame.draw.aaline(surface, (200, 100, 100), self.line[i], self.line[i + 1])
                pygame.draw.circle(surface, (255, 255, 255), self.line[i], 2)
                pygame.draw.circle(surface, (255, 255, 255), self.line[i + 1], 2)

            pygame.draw.aaline(surface, (200, 100, 100), self.line[-1], mousePos)
            pygame.draw.circle(surface, (255, 255, 255), mousePos, 2)
            pygame.draw.circle(surface, (255, 255, 255), self.line[0], 2)
        self.renderSnowflake(surface)


    def renderSnowflake(self, surface):
        offset = (self.snowflakeCenter[0] - self.baseShape[0][0], self.snowflakeCenter[1] - self.baseShape[0][1])

        pygame.draw.circle(surface, (200, 100, 100), self.snowflakeCenter, 100)

    def calculatePointsLocation(self, surface, original, offset, rotation, mirrorX, mirrorY):
        point = translate(original, offset)
        point = rotate(self.snowflakeCenter, point, rotation)
        point = mirror(self.snowflakeCenter, point, mirrorX, mirrorY)
        return point

    def addPoint(self, point):
        self.line.append(point)
        if (len(self.line) >= 2 and not isPointInTriangle(point, *self.baseShape)):
            self.points.extend(self.line)
            self.makeSlice(self.line[0], self.line[1])
            self.line = []

    def makeSlice(self, point1, point2):
        if (isPointInTriangle(point1, *self.baseShape)):
            print("Point1 in the triangle")
        
        if (isPointInTriangle(point2, *self.baseShape)):
            print("Point2 in the triangle")
