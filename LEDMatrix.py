from rgbmatrix import Adafruit_RGBmatrix
import Image
import ImageDraw

# Ease of Use API For Matrix
class LEDMatrix:
	
	def __init__(self, height, chains):
		self.matrix = Adafruit_RGBmatrix(height, chains)
		self.MAX_Y = height
		self.MAX_X = height * chains
		self.obj_list = []

	def setBG(self, hex_color):
		self.BG = hex_color
		self.drawBG()

	def drawBG(self):
		self.matrix.Fill(self.BG)

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

	def refresh(self):
		self.drawBG()

		for obj in self.obj_list:
			obj.draw()

class LEDSquare:
	def __init__(self, x1, y1, x2, y2, rgb, matrix):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.rgb = rgb
		self.matrix = matrix
		self.matrix.obj_list += [self]

	def draw(self):
		self.matrix.fillRect(self.x1, self.y1, self.x2, self.y2, self.rgb)

	def setX(self, x):
		width = self.x2 - self.x1
		self.x1 = x
		self.x2 = x + width

	def setY(self, y):
		height = self.y2 - self.y1
		self.y1 = y
		self.y2 = y + height

	def moveX(self, x):
		self.x1 += x
		self.x2 += x

	def moveY(self, y):
		self.y1 += y
		self.y2 += y

	def setWidth(self, width):
		self.x2 = self.x1 + width

	def setHeight(self, height):
		self.y2 = self.y1 + height

	def setRGB(self, r, g, b):
		self.rgb = (r,g,b)

	def destroy(self):
		self.matrix.obj_list.remove(self)

class LEDPoint:

	def __init__(self, x, y, rgb, matrix):
		self.x = x
		self.y = y
		self.rgb = rgb
		self.matrix = matrix
		self.matrix.obj_list += [self]

	def draw(self):
		self.matrix.setPixel(self.x, self.y, self.rgb)

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y

	def setRGB(self, r, g, b):
		self.rgb = (r,g,b)

	def destroy(self):
		self.matrix.obj_list.remove(self)

class LEDPointList:

	def __init__(self, matrix):
		self.matrix = matrix
		self.matrix.obj_list += [self]
		self.p_list = []

	def draw(self):
		print len(self.p_list) , "IN draw"
		for point in self.p_list:
			point.draw()

	def setRGBAll(self, r, g, b):
		for point in self.p_list:
			point.rgb = (r,g,b)

	def setRGBAt(self, index, r, g, b):
		self.p_list[index].rgb = (r,g,b)

	def add(self, led_point):
		self.p_list += [led_point]
		self.matrix.obj_list.remove(led_point)

	def removePoint(self, led_point):
		self.p_list.remove(led_point)

	def destroy(self):
		self.matrix.obj_list.remove(self)

	def pop(self, index):
		print len(self.p_list)
		self.p_list.pop(index)
		print len(self.p_list)

class LEDLine:

	def __init__(self, x1, y1, x2, y2, rgb, matrix):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.rgb = rgb
		self.matrix = matrix
		self.matrix.obj_list += [self]

	def draw(self):
		slope = (self.y2 - self.y1)/(self.x2 - self.x1)
		# positive slope
		for x in range(self.x1, self.x2 + 1):
			y = slope * (x - self.x1) + self.y1
			self.matrix.setPixel(self.x1 + x, y, self.rgb)
			print x, y
		# negative slope
		for x in range(self.x2, self.x1 + 1):
			y = slope * (x - self.x2) + self.y2
			self.matrix.setPixel(self.x2 + x, y, self.rgb)
			print x, y

	def setRGB(self, r, g, b):
		self.rgb = (r, g, b)


	def destroy(self):
		self.matrix.obj_list.remove(self)





