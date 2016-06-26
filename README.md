# LEDMatrix
LEDMAtrix is a Python library used to draw and animate on an RGB LED Matrix Board.

## Creator

**LEDMatrix** was created by and is maintained by **Jean-Marc Boullianne**, Undergraduate Student at the [University of Rochester](https://www.cs.rochester.edu/).

**LEDMatrix** is based on the [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) library created by [Henner Zeller](mailto:h.zeller@acm.org).

## Copyright and License

[GNU General Public License Version 2.0](http://www.gnu.org/licenses/gpl-2.0.txt)

### Example

```python

# LEDMatrix Library Test Script
# Running on a 2 32x32 LED Matrix boards
import time
from LEDMatrix import *

def main():
	print "Starting LEDMatrix Test"

	# Constructing LEDMatrix
	matrix = LEDMatrix(32, 2)

	# Set Background Green
	matrix.setBG(0x00FF00)
	time.sleep(1)

	#matrix.fillRect(0,0,15,15, (0,0,255))
	#time.sleep(1)

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

	# Clears the entire matrix LED board
	matrix.clear()

if __name__ == "__main__":
	main();

```
