import os
os.environ['PYOPENGL_PLATFORM'] = 'osmesa'

from OpenGL.GL import *
from OpenGL.GLUT import *
import math

angle = 0.0

def draw():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    
    glPushMatrix()
    glRotatef(angle, 0, 0, 1)
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex2f(0, 0.5)
    glColor3f(0, 1, 0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0, 0, 1)
    glVertex2f(0.5, -0.5)
    glEnd()
    glPopMatrix()
    
    glutSwapBuffers()
    angle += 1

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(400, 400)
glutCreateWindow(b"Animation")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glClearColor(0, 0, 0, 1)
glutMainLoop()