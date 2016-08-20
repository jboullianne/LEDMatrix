from rgbmatrix import Adafruit_RGBmatrix
import Image
import ImageDraw

# Ease of Use API For Matrix
class Matrix:
	
	def __init__(self, height, chains):
		self.matrix = Adafruit_RGBmatrix(height, chains)
		self.MAX_Y = height
		self.MAX_X = height * chains
		self.obj_list = []
		self.setBG(0x000000)

	def setBG(self, hex_color):
		self.BG = hex_color
		self.drawBG()

	def setBoard(self, board_num, rgb):
		self.fillRect(board_num*self.MAX_Y, 0, board_num*self.MAX_Y + self.MAX_Y, self.MAX_Y, rgb)

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

	def getMatrix(self):
		return self.matrix