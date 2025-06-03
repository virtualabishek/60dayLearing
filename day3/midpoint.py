import matplotlib.pyplot as plt

def plotCirclePoints(centerX, centerY, x, y, points):
    points.append((centerX + x, centerY + y))
    points.append((centerX - x, centerY + y))
    points.append((centerX + x, centerY - y))
    points.append((centerX - x, centerY - y))
    points.append((centerX + y, centerY + x))
    points.append((centerX - y, centerY + x))
    points.append((centerX + y, centerY - x))
    points.append((centerX - y, centerY - x))

def midpointCircleDraw(centerX, centerY, radius):
    points = []
    x = 0
    y = radius
    decision = 1 - radius

    plotCirclePoints(centerX, centerY, x, y, points)

    while x < y:
        x += 1
        if decision < 0:
            decision += 2 * x + 1
        else:
            y -= 1
            decision += 2 * (x - y) + 1
        plotCirclePoints(centerX, centerY, x, y, points)
    return points

def drawCircle():
    centerX, centerY = 100, 100
    radius = 60
    circlePoints = midpointCircleDraw(centerX, centerY, radius)
    
    xs, ys = zip(*circlePoints)
    plt.scatter(xs, ys, color='blue')
    plt.gca().set_aspect('equal')
    plt.savefig("midpoint_circle.png")
    print("Circle image saved as midpoint_circle.png")


drawCircle()
