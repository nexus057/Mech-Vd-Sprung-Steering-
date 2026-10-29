import math
from chassis import Chassis
from trajectory import Trajectory
class DynamicModel(Chassis):
    """This uses the dynamic bicycle model"""
    def __init__(self, hardpoints, tireWidth, steerAngle, trajectory:Trajectory):
        super().__init__(hardpoints, tireWidth)
        self.steerAngle = steerAngle
        self.trajectory = trajectory
    def frontSlipAngle(self, t):
        vx = self.trajectory._getv(t)[0]
        vy = self.trajectory._getv(t)[1]
        r = self.trajectory._getYawRate()
        a = self._frontAxleCenter - self.cg
        return self.steerAngle - math.atan2(vy+a*r, vx)
    def rearSlipAngle(self, t):
        b = self.cg - self._backAxleCenter
        vx = self.trajectory._getv(t)[0]
        vy = self.trajectory._getv(t)[1]
        r = self.trajectory._getYawRate()
        return -1 * math.atan2(vy - b*r, vx)
