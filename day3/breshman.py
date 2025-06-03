import matplotlib.pyplot as plt

def drawLineUsingBresenham(startX, startY, endX, endY):
    xPoints, yPoints = [], []

    x, y = startX, startY
    dx, dy = abs(endX - startX), abs(endY - startY)
    sx = 1 if endX > startX else -1
    sy = 1 if endY > startY else -1
    swapped = False

    if dy > dx:
        dx, dy = dy, dx
        swapped = True

    decisionParam = 2 * dy - dx

    for _ in range(dx + 1):
        xPoints.append(x)
        yPoints.append(y)

        if decisionParam >= 0:
            if swapped:
                x += sx
            else:
                y += sy
            decisionParam -= 2 * dx
        if swapped:
            y += sy
        else:
            x += sx
        decisionParam += 2 * dy

    plt.plot(xPoints, yPoints, marker='o', color='green')
    plt.title(f"Bresenham Line from ({startX},{startY}) to ({endX},{endY})")
    plt.gca().set_aspect('equal')
    plt.grid(True)

    fileName = "bresenham_line_output.png"
    plt.savefig(fileName)
    print(f" Line drawn and saved to: {fileName}")

drawLineUsingBresenham(2, 3, 15, 10)
