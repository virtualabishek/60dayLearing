import matplotlib.pyplot as plt

def drawLineUsingDDA(startX, startY, endX, endY):
    currentX, currentY = startX, startY
    deltaX, deltaY = endX - startX, endY - startY
    steps = max(abs(deltaX), abs(deltaY))
    xStep = deltaX / steps
    yStep = deltaY / steps

    xPoints, yPoints = [], []
    for _ in range(int(steps) + 1):
        xPoints.append(round(currentX))
        yPoints.append(round(currentY))
        currentX += xStep
        currentY += yStep

    plt.plot(xPoints, yPoints, marker='o', color='blue')
    plt.title(f"DDA Line from ({startX},{startY}) to ({endX},{endY})")
    plt.gca().set_aspect('equal')
    plt.grid(True)

    fileName = "dda_line_output.png"
    plt.savefig(fileName)
    print(f"Line drawn and saved to: {fileName}")

drawLineUsingDDA(2, 3, 15, 10)
