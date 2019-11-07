import random, math
from PIL import Image

random.seed()

class X():
   def eval(self, x, y):
      return x
   
   def __str__(self):
      return "x"

class Y():
   def eval(self, x, y):
      return y
   
   def __str__(self):
      return "y"

class SinPi():
   def __init__(self, prob):
      self.arg = buildExpr(prob * prob)
   
   def __str__(self):
      return "sin(pi*" + str(self.arg) + ")"

   def eval(self, x, y):
      return math.sin(math.pi * self.arg.eval(x,y))

class CosPi():
   def __init__(self, prob):
      self.arg = buildExpr(prob * prob)

   def __str__(self):
      return "cos(pi*" + str(self.arg) + ")"

   def eval(self, x, y):
      return math.cos(math.pi * self.arg.eval(x,y))

class TanPi():
   def __init__(self, prob):
      self.arg = buildExpr(prob * prob)

   def __str__(self):
      return "tan(pi*" + str(self.arg) + ")"

   def eval(self, x, y):
      return math.tan(math.pi * self.arg.eval(x,y))

class Times():
   def __init__(self, prob):
      self.lhs = buildExpr(prob * prob)
      self.rhs = buildExpr(prob * prob)

   def __str__(self):
      return str(self.lhs) + "*" + str(self.rhs)

   def eval(self, x, y):
      return self.lhs.eval(x,y) * self.rhs.eval(x,y)

class Plus():
   def __init__(self, prob):
      self.lhs = buildExpr(prob * prob)
      self.rhs = buildExpr(prob * prob)

   def __str__(self):
      return str(self.lhs) + "+" + str(self.rhs)

   def eval(self, x, y):
      return self.lhs.eval(x,y) + self.rhs.eval(x,y)

class Minus():
   def __init__(self, prob):
      self.lhs = buildExpr(prob * prob)
      self.rhs = buildExpr(prob * prob)

   def __str__(self):
      return str(self.lhs) + "-" + str(self.rhs)

   def eval(self, x, y):
      return self.lhs.eval(x,y) - self.rhs.eval(x,y)


def buildExpr(prob = 0.99):
   if random.random() < prob:
       # Randomly choose equation!
      return random.choice([CosPi, SinPi, Times, Minus, Plus])(prob)
   else:
      return random.choice([X, Y])()

def plotIntensity(exp, pixelsPerUnit = 270):
    #Create the new image canvas, define the size
    canvasWidth = 4 * pixelsPerUnit
    canvasHeight = 5 * pixelsPerUnit
    canvas = Image.new("L", (canvasWidth, canvasHeight))

    for py in range(canvasHeight):
        for px in range(canvasWidth):
            # Convert pixel location to [-1,1] coordinates
            x = float(px - pixelsPerUnit) / pixelsPerUnit 
            y = -float(py - pixelsPerUnit) / pixelsPerUnit
            z = exp.eval(x,y)

            # Scale [-1,1] result to [0,255].
            intensity = int(z * 127.5 + 127.5)
            canvas.putpixel((px,py), intensity)

    return canvas

def plotColor(redExp, greenExp, blueExp, pixelsPerUnit = 270):
    redPlane   = plotIntensity(redExp, pixelsPerUnit)
    greenPlane = plotIntensity(greenExp, pixelsPerUnit)
    bluePlane  = plotIntensity(blueExp, pixelsPerUnit)
    #Merge three colour planes into one image (Still not coloured yet!!)
    return Image.merge("RGB", (redPlane, greenPlane, bluePlane))

def makeImage(numPics = 1):
   with open("eqns.txt", 'w') as eqnsFile:
      for i in range(numPics):
          # Create the expressions that will determine the RBG colours
         redExp = buildExpr()
         greenExp = buildExpr()
         blueExp = buildExpr()

        #Write down the equations in a seperate text file
         eqnsFile.write("img" + str(i) + ":\n")
         eqnsFile.write("red = " + str(redExp) + "\n")
         eqnsFile.write("green = " + str(greenExp) + "\n")
         eqnsFile.write("blue = " + str(blueExp) + "\n\n")

         image = plotColor(redExp, greenExp, blueExp)
         image.save("img" + str(i) + ".png", "PNG")

makeImage(1)