import os
os.environ['PYOPENGL_PLATFORM'] = 'osmesa'

from OpenGL.GL import *
from OpenGL.GLUT import *
import math

# Smiley positions and velocities
smiley1_x, smiley1_y = -0.8, 0.0
smiley2_x, smiley2_y = 0.8, 0.5
vel1_x, vel1_y = 0.01, 0.008
vel2_x, vel2_y = -0.012, -0.006

def draw_circle(x, y, radius, segments=20):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(segments + 1):
        angle = 2.0 * math.pi * i / segments
        glVertex2f(x + math.cos(angle) * radius, y + math.sin(angle) * radius)
    glEnd()

def draw_smiley(x, y, size=0.15):
    # Face (yellow circle)
    glColor3f(1.0, 1.0, 0.0)
    draw_circle(x, y, size)
    
    # Eyes (black circles)
    glColor3f(0.0, 0.0, 0.0)
    draw_circle(x - size*0.3, y + size*0.3, size*0.15)
    draw_circle(x + size*0.3, y + size*0.3, size*0.15)
    
    # Mouth (arc)
    glBegin(GL_LINE_STRIP)
    for i in range(10):
        angle = math.pi + i * math.pi / 9
        mx = x + math.cos(angle) * size * 0.6
        my = y + math.sin(angle) * size * 0.4 - size*0.1
        glVertex2f(mx, my)
    glEnd()

def draw():
    global smiley1_x, smiley1_y, smiley2_x, smiley2_y
    global vel1_x, vel1_y, vel2_x, vel2_y
    
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Draw smileys
    draw_smiley(smiley1_x, smiley1_y)
    draw_smiley(smiley2_x, smiley2_y, 0.12)
    
    # Update positions
    smiley1_x += vel1_x
    smiley1_y += vel1_y
    smiley2_x += vel2_x
    smiley2_y += vel2_y
    
    # Bounce off walls
    if smiley1_x > 0.85 or smiley1_x < -0.85:
        vel1_x = -vel1_x
    if smiley1_y > 0.85 or smiley1_y < -0.85:
        vel1_y = -vel1_y
        
    if smiley2_x > 0.88 or smiley2_x < -0.88:
        vel2_x = -vel2_x
    if smiley2_y > 0.88 or smiley2_y < -0.88:
        vel2_y = -vel2_y
    
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Moving Smileys")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glClearColor(0.2, 0.3, 0.4, 1.0)
glutMainLoop()