class LEDEffect:

	def __init__(self, effect, matrix):
		self.effect = effect
		self.matrix = matrix
		self.matrix.obj_list += [self]

	def draw(self):
		print "LEDEffect Drawing"

	def destroy(self):
		self.matrix.obj_list.remove(self)