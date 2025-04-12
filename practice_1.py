from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

angle = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    light_pos = [1, 1, 1, 0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

def draw_polygon(vertices, colors=None):
    glBegin(GL_POLYGON)
    for i, vertex in enumerate(vertices):
        if colors is not None:
            glColor3f(*colors[i])
        # Если вершина задана как (x, y), используем z=0
        if len(vertex) == 2:
            glVertex3f(vertex[0], vertex[1], 0)
        else:
            glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # Камера, расположенная в точке (20, 20, 20), смотрит на центр координат
    gluLookAt(20, 20, 20, 0, 0, 0, 0, 0, 1)
    glRotatef(angle, 0, 1, 1)
    
    # вершины пятиугольника
    vertices = [(0, 0), (3, 3), (0, 3), (0, -3), (3, -3)]
    # цвета для каждой вершины
    colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1)]
    
    draw_polygon(vertices, colors)
    
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / height if height > 0 else 1, 1, 100)
    glMatrixMode(GL_MODELVIEW)

def update(value):
    global angle
    angle = (angle + 1) % 360
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Pentagon")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(16, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
