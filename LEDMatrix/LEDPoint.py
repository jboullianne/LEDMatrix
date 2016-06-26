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