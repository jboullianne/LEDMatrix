# led-matrix-api
Python API for drawing on a RGB LED Matrix display

### API

#### Constructor

```python
# Constructor for LEDMatrix
matrix = LEDMatrix(32, 2) // 32x32 pixels...2 chained together
```

#### Functions

```python

# Color/Fill Entire Matrix
matrix.setBG(#F17417)

# Color/Fill Rectangle on Matrix: x1, y1, x2, y2, color
matrix.fillRect(0, 0, 15, 15, #0000FF)

# Set Pixel (x,y), x=0, y=0, GREEN
matrix.setPixel(0,0, #00FF00)

```
