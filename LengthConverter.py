
class LengthConverter:
  def __init__(self, inch = 1):
    self.inch = inch
  
  def inchToCm(self):
    cm = self.inch * 2.54
    return round(cm,3)
