class LEDPointList:

	def __init__(self, matrix):
		self.matrix = matrix
		self.matrix.obj_list += [self]
		self.p_list = []

	def draw(self):
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