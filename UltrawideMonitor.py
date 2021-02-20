import math

class UltrawideMonitor:
  def __init__(self, inch = 34):
    self.inch = float(inch)
    self.width = 2560
    self.height = 1080
    self.widthRatio = 21
    self.heightRatio = 9
    self.diagonalRatio = math.sqrt(self.widthRatio**2 + self.heightRatio**2)
  def dimensionHeight(self):
    return (self.heightRatio * self.inch) / self.diagonalRatio
  def dimensionWidth(self):
    return (self.widthRatio * self.inch) / self.diagonalRatio