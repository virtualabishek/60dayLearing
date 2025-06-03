import matplotlib.pyplot as plt

def plotEllipsePoints(centerX, centerY, offsetX, offsetY, points):
    points.extend([
        (centerX + offsetX, centerY + offsetY),
        (centerX - offsetX, centerY + offsetY),
        (centerX + offsetX, centerY - offsetY),
        (centerX - offsetX, centerY - offsetY),
    ])

def midpointEllipse(centerX, centerY, radiusX, radiusY):
    points = []
    x, y = 0, radiusY
    radiusXSquare = radiusX * radiusX
    radiusYSquare = radiusY * radiusY
    deltaX = 2 * radiusYSquare * x
    deltaY = 2 * radiusXSquare * y

    decision1 = radiusYSquare - (radiusXSquare * radiusY) + (0.25 * radiusXSquare)
    while deltaX < deltaY:
        plotEllipsePoints(centerX, centerY, x, y, points)
        if decision1 < 0:
            x += 1
            deltaX += 2 * radiusYSquare
            decision1 += deltaX + radiusYSquare
        else:
            x += 1
            y -= 1
            deltaX += 2 * radiusYSquare
            deltaY -= 2 * radiusXSquare
            decision1 += deltaX - deltaY + radiusYSquare

    decision2 = (radiusYSquare) * (x + 0.5)**2 + (radiusXSquare) * (y - 1)**2 - (radiusXSquare * radiusYSquare)
    while y >= 0:
        plotEllipsePoints(centerX, centerY, x, y, points)
        if decision2 > 0:
            y -= 1
            deltaY -= 2 * radiusXSquare
            decision2 += radiusXSquare - deltaY
        else:
            y -= 1
            x += 1
            deltaX += 2 * radiusYSquare
            deltaY -= 2 * radiusXSquare
            decision2 += deltaX - deltaY + radiusXSquare
    return points

centerX, centerY = 100, 100
radiusX, radiusY = 80, 40
ellipsePoints = midpointEllipse(centerX, centerY, radiusX, radiusY)
xPoints, yPoints = zip(*ellipsePoints)

plt.scatter(xPoints, yPoints, color='blue')
plt.gca().set_aspect('equal')
plt.title("Midpoint Ellipse Drawing")
plt.savefig("midpoint_ellipse_output.png")
print("Ellipse drawn and saved as: midpoint_ellipse_output.png")
