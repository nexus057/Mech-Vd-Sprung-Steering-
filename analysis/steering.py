import math
from chassis import Chassis
class Steering(Chassis):
    def __init__(self, hardpoints, tireWidth):
        super().__init__(hardpoints, tireWidth)
    def getFrontWheelAngles(self, targetTurnRadius):
        T = self._frontTrackWidth
        L = self._wheelbase()
        # Inner wheel steering angle
        delta_i = math.atan(L / (targetTurnRadius - T / 2))

        # Outer wheel steering angle
        delta_o = math.atan(L / (targetTurnRadius + T / 2))

        # Convert radians to degrees
        delta_i_deg = math.degrees(delta_i)
        delta_o_deg = math.degrees(delta_o)
        return {"INNER WHEEL ANGLE": delta_i_deg, "OUTER WHEEL ANGLE": delta_o_deg}
    
    def getRackTravel(self, wheel_angle):
        "Positive angle: left steer, negative angle: right steer"
        upper = self.hardpoints["FL_UPPER_BALL_JOINT"]
        lower = self.hardpoints["FL_LOWER_BALL_JOINT"]
        outer = self.hardpoints["FL_TIE_OUTER"]
        t = (outer[2] - lower[2]) / (upper[2] - lower[2])
        kpX = lower[0] + t * (upper[0] - lower[0])
        kpY = lower[1] + t * (upper[1] - lower[1])
        kP = (kpX, kpY)
        TPO = self.hardpoints["FL_TIE_OUTER"]
        TPI = self.hardpoints["FL_TIE_INNER"]
        tieRodOuterPoint = (TPO[0], TPO[1])
        tieRodInnerPoint = (TPI[0], TPI[1])
        angleRad = math.radians(wheel_angle)
        cosAngle = math.cos(angleRad)
        sinAngle = math.sin(angleRad)

        armX = tieRodOuterPoint[0] - kP[0]
        armY = tieRodOuterPoint[1] - kP[1]
        outerX = kP[0] + armX * cosAngle - armY * sinAngle
        outerY = kP[1] + armX * sinAngle + armY * cosAngle

        tieRodLength = math.hypot(
            tieRodInnerPoint[0] - tieRodOuterPoint[0],
            tieRodInnerPoint[1] - tieRodOuterPoint[1],
        )

        offsetX = tieRodInnerPoint[0] - outerX
        reachSquared = tieRodLength ** 2 - offsetX ** 2
        if reachSquared < 0:
            raise ValueError("Invalid hardpoints - the tie cannot reach the rack at this angle")
        sideSign = 1.0 if tieRodInnerPoint[1] >= tieRodOuterPoint[1] else -1.0
        newRackY = outerY + sideSign * math.sqrt(reachSquared)
        return newRackY
    def getWheelAngleFromRackTravel(self, rackTravel, minAngle, maxAngle):

        def error(angle):
            return self.getRackTravel(angle) - rackTravel
        low = minAngle
        high = maxAngle
        f_low = error(low)
        f_high = error(high)
        if f_low * f_high > 0:
            raise ValueError("Rack travel outside of range")
        for _ in range(len(self.hardpoints)):
            mid = (low + high) / 2
            f_mid = error(mid)
            if abs(f_mid) < 1e-8:
                return mid
            if f_low * f_mid <= 0:
                high = mid
            else:
                low = mid
                f_low = f_mid

        return (low + high) / 2
    
    def getAckermannPercentages(self, innerAngle, outerAngle):
        inner = math.radians(abs(innerAngle))
        outer = math.radians(abs(outerAngle))

        if math.isclose(math.tan(inner), 0) or math.isclose(math.tan(outer), 0):
            raise ValueError("Nonzero wheel angles needed")
        T = self._frontAxleCenter
        L = self._wheelbase
        actual = 1 / math.tan(outer) - 1/ math.tan(inner)
        ideal = T / L
        return ideal / actual * 100
    




    

            
