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
        return outerY + sideSign * math.sqrt(reachSquared)



    

            
