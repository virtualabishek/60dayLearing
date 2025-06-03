import os
os.environ['PYOPENGL_PLATFORM'] = 'osmesa'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = 0

def draw_cube():
    glBegin(GL_LINES)
    # Bottom face
    glVertex3f(-1,-1,-1); glVertex3f(1,-1,-1)
    glVertex3f(1,-1,-1);  glVertex3f(1,1,-1)
    glVertex3f(1,1,-1);   glVertex3f(-1,1,-1)
    glVertex3f(-1,1,-1);  glVertex3f(-1,-1,-1)
    # Top face
    glVertex3f(-1,-1,1);  glVertex3f(1,-1,1)
    glVertex3f(1,-1,1);   glVertex3f(1,1,1)
    glVertex3f(1,1,1);    glVertex3f(-1,1,1)
    glVertex3f(-1,1,1);   glVertex3f(-1,-1,1)
    # Vertical edges
    glVertex3f(-1,-1,-1); glVertex3f(-1,-1,1)
    glVertex3f(1,-1,-1);  glVertex3f(1,-1,1)
    glVertex3f(1,1,-1);   glVertex3f(1,1,1)
    glVertex3f(-1,1,-1);  glVertex3f(-1,1,1)
    glEnd()

def draw():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Original cube (blue)
    glColor3f(0, 0, 1)
    draw_cube()
    
    # Transformed cube (red)
    glPushMatrix()
    glTranslatef(3, 0, 0)      # Translate
    glScalef(1.5, 1.5, 1.5)    # Scale
    glRotatef(angle, 0, 1, 0)  # Rotate Y
    glColor3f(1, 0, 0)
    draw_cube()
    glPopMatrix()
    
    glutSwapBuffers()
    angle += 1

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 400)
glutCreateWindow(b"3D Cube Transform")
glutDisplayFunc(draw)
glutIdleFunc(draw)

glEnable(GL_DEPTH_TEST)
glClearColor(0, 0, 0, 1)

# Setup 3D perspective
glMatrixMode(GL_PROJECTION)
gluPerspective(45, 1.5, 1, 50)
glMatrixMode(GL_MODELVIEW)
gluLookAt(8, 4, 8, 0, 0, 0, 0, 1, 0)

glutMainLoop()