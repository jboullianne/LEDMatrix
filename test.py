# LEDMatrix Library Test Script
# Running on a 2 32x32 LED Matrix boards
import time
from LEDMatrix import LEDMatrix

def main():
	print "Starting LEDMatrix Test"

	#Constructing LEDMatrix
	matrix = LEDMatrix(32, 2)
	matrix.setFill(0x00FF00)
	time.sleep(2)
	matrix.clear()

if __name__ == "__main__":
	main();