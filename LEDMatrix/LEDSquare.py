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