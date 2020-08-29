from pygame import *

class Snowflake(object):

    def __init__(self):
        self.baseShape = [(20, 20), (40, 100), (60, 20)]
        self.points = self.baseShape.copy()
        self.location = ()

    def render(self, surface):
        for point in self.baseShape:
            pygame.draw.circle(surface, (200, 200, 50), point, 3)
        pygame.draw.polygon(surface, (10, 200, 150), self.points)

    def makeSlice(self, point1, point2):


    def isPoint
