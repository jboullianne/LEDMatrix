# LEDMatrix Library Test Script
# Running on a 2 32x32 LED Matrix boards
import time
from LEDMatrix import *

def main():
	print "Starting LEDMatrix Test"

	# Constructing LEDMatrix
	matrix = Matrix(32, 2)

	# Set Background Green
	matrix.setBG(0x00FF00)
	time.sleep(1)

	matrix.setBoard(0, (255, 0, 0))
	matrix.setBoard(1, (0, 0, 255))
	time.sleep(1)

	#matrix.fillRect(0,0,15,15, (0,0,255))
	#time.sleep(1)

	'''
	square = LEDSquare(15,0,30,15, (255,0,0), matrix)
	matrix.refresh()
	time.sleep(1)

	# Moves square's position 3 pixels to the right
	square.moveX(3)
	matrix.refresh()
	time.sleep(2)

	# Sets square's height (based from top left)
	square.setHeight(30)
	matrix.refresh()
	time.sleep(1)

	square.setRGB(0,0,255)
	matrix.refresh()
	time.sleep(1)

	# Shouldn't change when refreshed because it has been destroyed
	square.setRGB(255,0,0)
	square.destroy()
	matrix.refresh();
	time.sleep(1)

	# Construct new LEDSquare
	square2 = LEDSquare(0,0,10,10, (0,0,255), matrix)
	matrix.refresh()
	time.sleep(1)

	# Animate it up/down left/right
	for x in range(0, 15):
		for y in range(0, 15):
			square2.moveY(1)
			matrix.refresh()
			time.sleep(0.01)

		square2.moveX(1)
		square2.setY(0)
		matrix.refresh()
		time.sleep(0.01)

	time.sleep(1)

	# Construct New LEDPoint
	p1 = LEDPoint(0, 0, (255, 0, 0), matrix)
	matrix.refresh()
	time.sleep(1)

	# Animate it up/down left/right
	for x in range(0, 15):
		for y in range(0, 15):
			p1.setY(y)
			matrix.refresh()
			time.sleep(0.01)

		p1.setX(x)
		p1.setY(0)
		matrix.refresh()
		time.sleep(0.01)

	time.sleep(1)
	
	pList = LEDPointList(matrix)
	pList.add(LEDPoint(0,0, (0,0,255), matrix))
	pList.add(LEDPoint(1,0, (255,0,255), matrix))
	pList.add(LEDPoint(2,0, (0,255,255), matrix))
	pList.add(LEDPoint(3,0, (255,255,0), matrix))
	matrix.refresh()
	time.sleep(1)

	pList.setRGBAll(0,0,255)
	matrix.refresh()
	time.sleep(1)

	pList.pop(0)
	pList.pop(1)
	matrix.refresh()
	time.sleep(1)

	matrix.setBG(0xFF0000)
	matrix.refresh()'''

	line = LEDLine(0,0, 15, 15, (0,0,255), matrix)
	line2 = LEDLine(15,0, 0, 15, (0,0,255), matrix)
	matrix.refresh()
	time.sleep(1)
	line.destroy()
	line2.destroy()

	matrix.clear()
	matrix.setBG(0x000000)
	matrix.refresh()

	text1 = LEDText(0,0, (255,255,255), "{ } [ ] | \\ ", matrix)
	text2 = LEDText(0,5, (255,255,255), ": ; \' < > , . ?", matrix)

	matrix.refresh()
	time.sleep(1)

	time.sleep(1)
	# Clears the entire matrix LED board
	matrix.clear()

if __name__ == "__main__":
	main();