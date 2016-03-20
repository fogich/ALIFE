import math
import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# program modifiers
branchThreshold = 4
width, height = 900, 900

# global variables
window, mouseX, mouseY = 0, 0, 0
theta = 0.0

def drawLine(x1, y1, x2, y2):
    """Draw a line by providing two points"""
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def refresh2d(width, height):
    """Refresh the viewport"""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def branchLeg(th, h): 
    """Perform tree branching and draw the result"""
    glPushMatrix()
    glRotatef(math.degrees(th), 0, 0, -1)
    drawLine(0, 0, 0, h)
    glTranslatef(0, h, 0)
    branch(h)
    glPopMatrix()

def branch(h):
    """Check and performs branching"""
    h *= 0.52+(0.17*((height-mouseY) / height))
    if (h > branchThreshold):
       branchLeg(theta, h)
       branchLeg(-theta, h)

def draw():
    """Our draw function. This is our logic loop""" 
    global sizeX, sizeY, theta
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2d(width, height)

    glColor3f(1.0, 1.0, 1.0)
    theta = math.radians((mouseX / width) * 90)
    th = 100+(math.fabs(900-mouseY))/4
    
    glTranslatef(width/2, 0, 0)
    drawLine(0, 0, 0, th)
    glTranslatef(0, th, 0)
    branch(th)    

    glutSwapBuffers()
   
def mouseMotion(x:int, y:int):
    """MouseMotion event callback"""
    global mouseX, mouseY
    mouseX = x
    mouseY = y

def viewportChanged(w:int, h:int):
    """Viewport change even callback"""
    global width, height
    width = w
    height = h

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutInitWindowPosition(0, 0)
window = glutCreateWindow(b"Interactive Tree")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutPassiveMotionFunc(mouseMotion)
glutReshapeFunc(viewportChanged)
glutMainLoop()     