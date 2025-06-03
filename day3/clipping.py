import matplotlib.pyplot as plt

LEFT, RIGHT, BOTTOM, TOP = 1, 2, 4, 8

def computeCode(x, y, xmin, xmax, ymin, ymax):
    code = 0
    if x < xmin: code |= LEFT
    elif x > xmax: code |= RIGHT
    if y < ymin: code |= BOTTOM
    elif y > ymax: code |= TOP
    return code

def cohenSutherland(x1, y1, x2, y2, xmin, xmax, ymin, ymax):
    code1 = computeCode(x1, y1, xmin, xmax, ymin, ymax)
    code2 = computeCode(x2, y2, xmin, xmax, ymin, ymax)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2:
            break
        else:
            code_out = code1 or code2
            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1, y1 = x, y
                code1 = computeCode(x1, y1, xmin, xmax, ymin, ymax)
            else:
                x2, y2 = x, y
                code2 = computeCode(x2, y2, xmin, xmax, ymin, ymax)

    if accept:
        return (x1, y1, x2, y2)
    else:
        return None

# Drawing
fig, ax = plt.subplots()
xmin, xmax, ymin, ymax = 50, 100, 50, 100
x1, y1, x2, y2 = 30, 70, 120, 110  # line

clipped = cohenSutherland(x1, y1, x2, y2, xmin, xmax, ymin, ymax)

ax.plot([x1, x2], [y1, y2], 'r--', label="Original Line")
ax.plot([xmin, xmax, xmax, xmin, xmin],
        [ymin, ymin, ymax, ymax, ymin], 'k-', label="Clipping Window")

if clipped:
    cx1, cy1, cx2, cy2 = clipped
    ax.plot([cx1, cx2], [cy1, cy2], 'g-', label="Clipped Line")

ax.set_title("Cohen-Sutherland Line Clipping")
ax.set_xlim(0, 150)
ax.set_ylim(0, 150)
ax.legend()
plt.savefig("line_clipping.png")
print("Image saved: line_clipping.png")
