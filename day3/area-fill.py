import os
os.environ['PYOPENGL_PLATFORM'] = 'osmesa'

from OpenGL.GL import *
from OpenGL.GLUT import *

grid = [[0]*20 for _ in range(20)]
mode = 0

def draw_grid():
    glClear(GL_COLOR_BUFFER_BIT)
    for y in range(20):
        for x in range(20):
            if grid[y][x] == 1:      # Boundary
                glColor3f(1, 1, 1)
            elif grid[y][x] == 2:    # Fill
                glColor3f(1, 0, 0)
            else:                    # Empty
                glColor3f(0, 0, 0)
            
            glBegin(GL_QUADS)
            glVertex2f(x*0.1-1, y*0.1-1)
            glVertex2f((x+1)*0.1-1, y*0.1-1)
            glVertex2f((x+1)*0.1-1, (y+1)*0.1-1)
            glVertex2f(x*0.1-1, (y+1)*0.1-1)
            glEnd()
    
    glutSwapBuffers()

def flood_fill(x, y, old, new):
    if x<0 or x>=20 or y<0 or y>=20 or grid[y][x] != old:
        return
    grid[y][x] = new
    flood_fill(x+1, y, old, new)
    flood_fill(x-1, y, old, new)
    flood_fill(x, y+1, old, new)
    flood_fill(x, y-1, old, new)

def setup():
    global grid
    # Draw rectangle boundary
    for i in range(5, 15):
        grid[5][i] = grid[14][i] = 1
        grid[i][5] = grid[i][14] = 1
    
    if mode == 1:  # Fill
        flood_fill(10, 10, 0, 2)

def timer(v):
    global mode
    mode = 1 - mode
    setup()
    glutPostRedisplay()
    glutTimerFunc(2000, timer, 0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(400, 400)
glutCreateWindow(b"Fill Algorithm")
glutDisplayFunc(draw_grid)
glutTimerFunc(2000, timer, 0)
setup()
glutMainLoop()