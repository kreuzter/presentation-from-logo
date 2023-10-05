from extcolors import extract_from_path
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i")
parser.add_argument("-l")
parser.add_argument("-d")

args = parser.parse_args()
if args.i == None:
  args.i = "imgs/logo.png"

if args.l == None: 
  args.l = [255,255,255]
else: args.l = [int(item) for item in (args.l).split(',')]

if args.d == None: 
  args.d = [0,0,0]
else: args.d = [int(item) for item in (args.d).split(',')]

class Color:
  def __init__(self, RGB):
    self.R = RGB[0]; self.G = RGB[1]; self.B = RGB[2]
  
  def __str__(self):
    return "{" + str(int(self.R)) + ","  + str(int(self.G))+ ","  + str(int(self.B)) + "}" 
  
  def blend(self, color2, alpha):

    R = self.R*alpha + color2.R*(1-alpha)
    G = self.G*alpha + color2.G*(1-alpha)
    B = self.B*alpha + color2.B*(1-alpha)
    
    blend = Color([R, G, B])
    return blend

colors = extract_from_path(args.i)

i = 0
while colors[0][i][0] == (255, 255, 255) \
   or colors[0][i][0] == (0,0,0)         \
   or colors[0][i][0] == tuple(args.l)   \
   or colors[0][i][0] == tuple(args.d) :
  i = i+1

mainColor          = Color(colors[0][i][0])
lightBlendingColor = Color(args.l)
darkBlendingColor  = Color(args.d)

numColors = 4

factors = np.linspace(0, 0.5, numColors)

with open( 'orig_main.tex', 'r' ) as file :
  origFile = file.read()
  origFile = origFile.replace('PLACEHOLDER_PATH_TO_LOGO', args.i)
  origFile = origFile.replace('PLACEHOLDER_COLOR_0' , (mainColor.blend(darkBlendingColor, 0.4).__str__()))
  for i in range(1,numColors):
    origFile = origFile.replace(f'PLACEHOLDER_COLOR_{i}' , (mainColor.blend(lightBlendingColor, factors[i]).__str__()))

with open( 'main.tex', 'w' ) as file: file.write( origFile )
