import os
os.environ['PYOPENGL_PLATFORM'] = 'osmesa'

from OpenGL.GL import *
from OpenGL.GLUT import *
import math

mode = 0

def draw_triangle(x, y, size, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y + size)
    glVertex2f(x - size, y - size)
    glVertex2f(x + size, y - size)
    glEnd()

def draw():
    global mode
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Original
    draw_triangle(0, 0, 0.2, (0, 0, 1))
    
    # Transformed
    if mode == 0:    # Translate
        draw_triangle(0.5, 0.3, 0.2, (1, 0, 0))
    elif mode == 1:  # Scale
        draw_triangle(0, 0, 0.4, (1, 0, 0))
    elif mode == 2:  # Rotate
        glPushMatrix()
        glRotatef(45, 0, 0, 1)
        draw_triangle(0, 0, 0.2, (1, 0, 0))
        glPopMatrix()
    
    glutSwapBuffers()
    mode = (mode + 1) % 3

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(1000, timer, 0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(400, 400)
glutCreateWindow(b"Transformations")
glutDisplayFunc(draw)
glutTimerFunc(1000, timer, 0)
glClearColor(0, 0, 0, 1)
glutMainLoop()