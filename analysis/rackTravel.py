import math

print('Positive angle - steer left, negative angle - steer right')
    
kingpinPoint = (0.0, 600.0)
tieRodOuterPoint = (70.0, 525.0)
tieRodInnerPoint = (70.0, 200.0)
wheelAngleDeg = float(input('Enter wheel steer angle:'))


def rackTravelFromWheelAngle(wheelAngleDeg, kingpinPoint, tieRodOuterPoint, tieRodInnerPoint):
    #Positive is towards the left
    angleRad = math.radians(wheelAngleDeg)
    cosAngle = math.cos(angleRad)
    sinAngle = math.sin(angleRad)

    armX = tieRodOuterPoint[0] - kingpinPoint[0]
    armY = tieRodOuterPoint[1] - kingpinPoint[1]
    outerX = kingpinPoint[0] + armX * cosAngle - armY * sinAngle
    outerY = kingpinPoint[1] + armX * sinAngle + armY * cosAngle

    tieRodLength = math.hypot(
        tieRodInnerPoint[0] - tieRodOuterPoint[0],
        tieRodInnerPoint[1] - tieRodOuterPoint[1],
    )

    offsetX = tieRodInnerPoint[0] - outerX
    reachSquared = tieRodLength ** 2 - offsetX ** 2
    if reachSquared < 0:
        raise ValueError("Invalid hardpoints - the tie cannot reach the rack at this angle")

    sideSign = 1.0 if tieRodInnerPoint[1] >= tieRodOuterPoint[1] else -1.0
    newInnerY = outerY + sideSign * math.sqrt(reachSquared)

    return newInnerY - tieRodInnerPoint[1]


rackTravel = rackTravelFromWheelAngle(wheelAngleDeg, kingpinPoint, tieRodOuterPoint, tieRodInnerPoint)
print(f"Rack travel: {rackTravel:.2f} mm")
