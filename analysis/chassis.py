class Chassis:
    """
    Chassis long side aligned along x-axis, all points relative to center
    """
    def __init__(self, hardpoints, tireWidth, cg):
        self.hardpoints = []
        self.tireWidth = tireWidth
        self.cg = cg #center of gravity (x, y, z)
    def addComponent(self, jointName, x, y, z):
        self.hardpoints.append({jointName: [x, y, z]})
    def getComponent(self, jointName):
        return self.hardpoints[self.hardpoints.index(jointName)]
    def assignWheelCenters(self, frontLeftCoord, frontRightCoord, backLeftCoord, backRightCoord):
        self.hardpoints.append({"FRONT_TIRE_LEFT" : frontLeftCoord})
        self.hardpoints.append({"BACK_TIRE_LEFT": backLeftCoord})
        self.hardpoints.append({"FRONT_TIRE_RIGHT": frontRightCoord})
        self.hardpoints.append({"BACK_TIRE_RIGHT": backRightCoord})
        return
    def _wheelbase(self):
        try: 
            Y_FRONT = (self.hardpoints['FRONT_TIRE_RIGHT'][1] + self.hardpoints['FRONT_TIRE_LEFT'][1]) / 2
            Y_BACK = (self.hardpoints['BACK_TIRE_RIGHT'][1] + self.hardpoints['BACK_TIRE_LEFT'][1]) / 2
            return Y_FRONT - Y_BACK
        except:
            raise ValueError("Tire center positions not specified, use assignWheelCenters")
    def _frontTrackWidth(self):
        try:
            return self.hardpoints['FRONT_TIRE_RIGHT'][1] - self.hardpoints['FRONT_TIRE_LEFT'][1]
        except:
            raise ValueError("Tire center positions not specified, use assignWheelCenters")
    def _backTrackWidth(self):
        try:
            return self.hardpoints['BACK_TIRE_RIGHT'][1] - self.hardpoints['BACK_TIRE_LEFT'][1]
        except:
            raise ValueError("Tire center positions not specified, use assignWheelCenters")
    def _frontAxleCenter(self):
        return [
            (self.hardpoints["FRONT_TIRE_LEFT"][0] + self.hardpoints["FRONT_TIRE_RIGHT"][0]) / 2,
            (self.hardpoints["FRONT_TIRE_LEFT"][1] + self.hardpoints["FRONT_TIRE_RIGHT"][1]) / 2,
            (self.hardpoints["FRONT_TIRE_LEFT"][2] + self.hardpoints["FRONT_TIRE_RIGHT"][2]) / 2,
        ]
    def _backAxleCenter(self):
        return [
            (self.hardpoints["BACK_TIRE_LEFT"][0] + self.hardpoints["BACK_TIRE_RIGHT"][0]) / 2,
            (self.hardpoints["BACK_TIRE_LEFT"][1] + self.hardpoints["BACK_TIRE_RIGHT"][1]) / 2,
            (self.hardpoints["BACK_TIRE_LEFT"][2] + self.hardpoints["BACK_TIRE_RIGHT"][2]) / 2
        ]

    

























