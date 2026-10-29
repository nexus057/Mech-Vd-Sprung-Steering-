class Trajectory:
    def __init__(self, points, dt):
        self.points = points #(x, y, z, t)
        self.dt = 0.05 #sec
    def _getv(self, n):
        vx = (self.points[n*self.dt][0] - self.points[n*self.dt - 1][0]) / self.dt
        vy = (self.points[n*self.dt][1] - self.points[n*self.dt - 1][1]) / self.dt
        vz = (self.points[n*self.dt][2] - self.points[n*self.dt - 1][2]) / self.dt
        speed = (vx**2 + vy**2 + vz**2) ** (1/2)
        return [vz, vy, vx, speed]
    def _geta(self, n):
        return (self._getv(n) - self._get_v(n-1))/ self.dt
    def _getYawRate(self, n):
        vx = self._getv(n)[0]
        vy = self._getv(n)[1]
        ax = self._geta(n)[0]
        ay = self._geta(n)[1]
        phiDot = (vx*ay - vy*ax)/(vx**2 + vy**2)
        return phiDot



