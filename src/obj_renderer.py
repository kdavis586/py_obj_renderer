import sys
from Obj import Obj
from OpenGL.GL import *
from OpenGL.GLUT import *

def main(argv) -> None:
    inputs = argv[1:]
    if not inputs or len(inputs) > 1:
        raise Exception("Invalid number of inputs." + \
                            "\npython obj_renderer.py <path_to_obj>")
    obj_path = argv[1]
    model = Obj(obj_path)

    if 'DISPLAY' in os.environ:
        del os.environ['DISPLAY']
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(200, 200)
    window = glutCreateWindow("Simple PyOpenGL Window")
    
    # Set the draw function
    glutDisplayFunc(model.render)

    glutMainLoop()
    

if __name__ == '__main__':
    main(sys.argv)