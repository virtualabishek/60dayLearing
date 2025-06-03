import matplotlib.pyplot as plt
import numpy as np

width, height = 30, 30
canvas = np.zeros((height, width))

# Triangle for simplicity
polygon = [(5, 5), (25, 10), (15, 25)]

def drawPolygon(polygon):
    for i in range(len(polygon)):
        x0, y0 = polygon[i]
        x1, y1 = polygon[(i + 1) % len(polygon)]
        drawLine(x0, y0, x1, y1)

def drawLine(x0, y0, x1, y1):
    dx, dy = x1 - x0, y1 - y0
    steps = max(abs(dx), abs(dy))
    for i in range(steps + 1):
        x = round(x0 + i * dx / steps)
        y = round(y0 + i * dy / steps)
        canvas[y, x] = 1

def scanlineFill(polygon):
    ymin = min(y for _, y in polygon)
    ymax = max(y for _, y in polygon)

    for y in range(ymin, ymax + 1):
        intersections = []
        for i in range(len(polygon)):
            (x0, y0), (x1, y1) = polygon[i], polygon[(i + 1) % len(polygon)]
            if y0 == y1:
                continue
            if (y >= min(y0, y1)) and (y < max(y0, y1)):
                x = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
                intersections.append(x)
        intersections.sort()
        for i in range(0, len(intersections), 2):
            x_start = round(intersections[i])
            x_end = round(intersections[i + 1])
            canvas[y, x_start:x_end] = 1

drawPolygon(polygon)
scanlineFill(polygon)

plt.imshow(canvas, cmap='gray_r')
plt.title("Scanline Polygon Fill")
plt.axis('off')
plt.savefig("scanline_polygon_fill.png")
print("Image saved: scanline_polygon_fill.png")
