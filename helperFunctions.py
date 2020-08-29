import math

def triangleArea(x1, y1, x2, y2, x3, y3):

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

def translate(original, offset):
    return (original[0] + offset[0], original[1] + offset[1])

def mirror(origin, point, xFlip, yFlip):
    newPointX = point[0]
    newPointY = point[1]
    if (xFlip):
        newPointX = origin[0] + (origin[0] - point[0])
    if (yFlip):
        newPointY = origin[1] + (origin[1] - point[1])
        
    return (newPointX, newPointY)

def isPointInTriangle(targetPoint, trainglePoint1, trainglePoint2, trainglePoint3):
    a = triangleArea(
        trainglePoint1[0], trainglePoint1[1], trainglePoint2[0], trainglePoint2[1], trainglePoint3[0], trainglePoint3[1])
    a1 = triangleArea(
        targetPoint[0], targetPoint[1], trainglePoint2[0], trainglePoint2[1], trainglePoint3[0], trainglePoint3[1])
    a2 = triangleArea(
        trainglePoint1[0], trainglePoint1[1], targetPoint[0], targetPoint[1], trainglePoint3[0], trainglePoint3[1])
    a3 = triangleArea(
        trainglePoint1[0], trainglePoint1[1], trainglePoint2[0], trainglePoint2[1], targetPoint[0], targetPoint[1])
    if (a == a1 + a2 + a3):
        return True
    else:
        return False
