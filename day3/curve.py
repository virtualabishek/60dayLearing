import matplotlib.pyplot as plt

def lerp(pointA, pointB, t):
    x = (1 - t) * pointA[0] + t * pointB[0]
    y = (1 - t) * pointA[1] + t * pointB[1]
    return (x, y)

def bezierPoint(controlPoints, t):
    points = controlPoints
    while len(points) > 1:
        points = [lerp(points[i], points[i+1], t) for i in range(len(points)-1)]
    return points[0]

def drawBezier(controlPoints, steps=100):
    curvePoints = [bezierPoint(controlPoints, t/steps) for t in range(steps+1)]
    xs, ys = zip(*curvePoints)

    ctrlX, ctrlY = zip(*controlPoints)

    plt.plot(ctrlX, ctrlY, "ro--", label="Control Points")
    plt.plot(xs, ys, "b-", label="Bezier Curve")
    plt.legend()
    plt.title(f"Bezier Curve with {len(controlPoints)} Control Points")
    plt.savefig("bezier_curve.png")
    print("Bezier curve saved as bezier_curve.png")
    plt.show()

controlPoints = [(0, 0), (1, 2), (3, 3), (4, 0)]

drawBezier(controlPoints)
