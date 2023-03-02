import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    # Czyszczenie buforów koloru i głębokości
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Rysowanie sześcianu
    glutWireCube(2.0)

    # Rotacja sześcianu
    glRotatef(0.5, 1.0, 1.0, 1.0)
    glutSwapBuffers()

def main():
    # Inicjalizacja okna
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Obracający się sześcian")
    glutDisplayFunc(draw)

    # Inicjalizacja ustawień sceny 3D
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, 800.0 / 600.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    # Główna pętla programu
    glutMainLoop()

if __name__ == '__main__':
    main()
