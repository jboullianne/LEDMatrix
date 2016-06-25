# LEDMatrix
LEDMAtrix is a Python library used to draw and animate on an RGB LED Matrix Board.

## Creator

**LEDMatrix** was created by and is maintained by **Jean-Marc Boullianne**, Undergraduate Student at the [University of Rochester](https://www.cs.rochester.edu/).

**LEDMatrix** is based on the [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) library created by [Henner Zeller](mailto:h.zeller@acm.org).

## Copyright and License

[GNU General Public License Version 2.0](http://www.gnu.org/licenses/gpl-2.0.txt)

### API

#### Constructor

```python
# Constructor for LEDMatrix
matrix = LEDMatrix(32, 2) # 32x32 pixels...2 chained together
```

#### Functions
###### Not all functions listed.

```python

# Color/Fill Entire Matrix
matrix.setBG(#F17417)

# Color/Fill Rectangle on Matrix: x1, y1, x2, y2, color
matrix.fillRect(0, 0, 15, 15, #0000FF)

# Set Pixel (x,y), x=0, y=0, GREEN
matrix.setPixel(0,0, #00FF00)

```
