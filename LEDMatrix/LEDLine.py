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
		# negative slope
		for x in range(self.x2, self.x1 + 1):
			y = slope * (x - self.x2) + self.y2
			self.matrix.setPixel(self.x2 + x, y, self.rgb)

	def setRGB(self, r, g, b):
		self.rgb = (r, g, b)


	def destroy(self):
		self.matrix.obj_list.remove(self)