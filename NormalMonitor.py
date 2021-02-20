import math

class NormalMonitor:
  def __init__(self, inch = 27):
    self.inch = float(inch)
    self.width = 1920
    self.height = 1080
    self.widthRatio = 16
    self.heightRatio = 9
    self.diagonalRatio = math.sqrt(self.widthRatio**2 + self.heightRatio**2)
  def dimensionHeight(self):
    return (self.heightRatio * self.inch) / self.diagonalRatio
  def dimensionWidth(self):
    return (self.widthRatio * self.inch) / self.diagonalRatio