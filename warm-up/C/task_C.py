import math


def alg(xA, yA, xB, yB):
    if xA == xB and yA == yB:
        track = 0
    elif (xA == 0 and yA == 0) or (xB == 0 and yB == 0):
        track = math.sqrt(xA * xA + yA * yA + xB * xB + yB * yB)
    else:
        rA = math.sqrt(xA * xA + yA * yA)
        rB = math.sqrt(xB * xB + yB * yB)
        rMin = min(rA, rB)
        rDelta = max(rA, rB) - rMin

        angleA = math.atan2(yA, xA)
        angleB = math.atan2(yB, xB)
        angleDelta = max(angleA, angleB) - min(angleA, angleB)
        if angleDelta > math.pi:
            angleDelta = 2 * math.pi - angleDelta

        track = rDelta + min(2, angleDelta) * rMin
    return "{:.12f}".format(track)

xA, yA, xB, yB = map(int, input().split())

print(alg(xA, yA, xB, yB))