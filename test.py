# LEDMatrix Library Test Script
# Running on a 2 32x32 LED Matrix boards
import time
from LEDMatrix import LEDMatrix
from LEDMatrix import LEDSquare

def main():
	print "Starting LEDMatrix Test"

	# Constructing LEDMatrix
	matrix = LEDMatrix(32, 2)

	# Set Background Green
	matrix.setFill(0x00FF00)
	time.sleep(1)

	matrix.fillRect(0,0,15,15, (0,0,255))
	time.sleep(1)

	square = LEDSquare(15,0,30,15, (255,0,0), matrix)
	time.sleep(1)

	# Moves square's position 3 pixels to the right
	square.moveX(3)
	time.sleep(2)

	# Clears the entire matrix LED board
	matrix.clear()

if __name__ == "__main__":
	main();