from NormalMonitor import NormalMonitor
from UltrawideMonitor import UltrawideMonitor
from LengthConverter import LengthConverter

def calculateNormal(ultrawide):
  x_result = 27 * ultrawide / 34
  return x_result

def calculateUltrawide(normal):
  y_result = 34 * normal / 27
  return y_result

q = input('Normal Monitor? (Y/N): ')
normal = 27
ultrawide = 34

if q == 'y' or q == 'Y':
  normal = NormalMonitor().inch
  x = input('Size (27)inch: ')
  if len(x) > 0:
    normal = NormalMonitor(inch=x).inch
  ultrawide = calculateUltrawide(normal)
else:
  r = input('Ultrawide Monitor? (Y/N): ')
  if r == 'y' or r == 'Y':
    ultrawide = UltrawideMonitor().inch
    y = input('Size (34)inch: ')
    if len(y) > 0:
      ultrawide = UltrawideMonitor(inch=y).inch
    normal = calculateNormal(ultrawide)
  else:
    pass

def calculateRatio(normal, ultrawide):
  heightNormalMonitor = NormalMonitor(inch=round(normal)).dimensionHeight()
  widthNormalMonitor = NormalMonitor(inch=round(normal)).dimensionWidth()
  heightUltrawideMonitor = UltrawideMonitor(inch=round(ultrawide)).dimensionHeight()
  widthUltrawideMonitor = UltrawideMonitor(inch=round(ultrawide)).dimensionWidth()


  print('==================================================')
  print(f'Normal Monitor = {round(normal)}", Ultrawide Monitor = {round(ultrawide)}"')
  print(f'Normal Monitor: {round(LengthConverter(widthNormalMonitor).inchToCm(),2)}cm width x {round(LengthConverter(heightNormalMonitor).inchToCm(),2)}cm height.')
  print(f'Ultrawide Monitor: {round(LengthConverter(widthUltrawideMonitor).inchToCm(),2)}cm width x {round(LengthConverter(heightUltrawideMonitor).inchToCm(),2)}cm height.')
  print('==================================================')

calculateRatio(normal, ultrawide)