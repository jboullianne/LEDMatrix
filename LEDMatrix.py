from rgbmatrix import Adafruit_RGBmatrix
import Image
import ImageDraw

# Ease of Use API For Matrix
class LEDMatrix:
	
	def __init__(self, height, chains):
		self.matrix = Adafruit_RGBmatrix(height, chains)
		self.MAX_Y = height
		self.MAX_X = height * chains

	def setFill(self, hex_color):
		self.matrix.Fill(hex_color)

	def clear(self):
		self.matrix.Clear()

	def setPixel(self, x, y, rgb):
		self.matrix.SetPixel(x, y, *rgb)

	def fillRect(self, x1, y1, x2, y2, rgb):
		for x in range(x1, x2):
			for y in range(y1, y2):
				self.setPixel(x, y, rgb)

	def drawPointList(self, plist, rgb):
		for point in plist:
			self.setPixel(point[0],point[1], rgb)

	def drawImage(self, file_name):
		image = Image.open(file_name)
		raw = image.load()

		for x in range(0,30):
			for y in range(0,63):
				rgb = raw[y, x]
				if rgb == (0,0,0): #If you wanted to make the background another color
					self.setPixel(y,x, (0,0,0))
				else:
					self.setPixel(y, x, (rgb[0], rgb[1], rgb[2]))

class LEDSquare:
	def __init__(self, x1, y1, x2, y2, rgb, matrix):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.rgb = rgb
		self.matrix = matrix
		self.draw()

	def draw(self):
		self.matrix.fillRect(self.x1, self.y1, self.x2, self.y2, self.rgb)

	def moveX(self, x):
		self.x1 += x
		self.x2 += x
		self.draw()
