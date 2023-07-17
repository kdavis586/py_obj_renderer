import os
from OpenGL.GL import *
from OpenGL.GLUT import *

class Obj():
    def __init__(self, path: str) -> None:
        self.vertices = []
        self.tex_coords = []
        self.norms = []
        self.faces = []
        self._parse_obj(path)
    
    def _parse_obj(self, path: str) -> None:
        if not isinstance(path, str):
            raise TypeError("The given file path was not a string.")
        if not os.path.exists(path):
            raise FileNotFoundError("The given file path does not exist.")
        if not os.path.isfile(path):
            raise ValueError("The given file path was not for a path. Did you give a path for a directory?")
        
        with open(path) as f:
            for line in f:
                line.strip()
                if not line or line.startswith('#'):
                    continue
                tokens = line.split()
                if not tokens:
                    continue
                prefix = tokens[0]
                data = tokens[1:]
                if not data:
                    continue
                
                match prefix:
                    case 'v':
                        vertex = list(map(float, data))
                        self.vertices.append(vertex)
                    case 'vt':
                        tex_coord = list(map(float, data))
                        self.tex_coords.append(tex_coord)
                    case 'vn':
                        normal = list(map(float, data))
                        self.norms.append(normal)
                    case 'f':
                        face = []
                        for val_string in data:
                            val_list = []
                            vals = val_string.split('/')
                            n = len(vals)
                            match n:
                                case 1:
                                    val_list = [int(vals[0]), -1, -1]
                                case 2:
                                    val_list = list(map(int, vals))
                                    val_list.append(-1)
                                case _:
                                    val_list = list(map(lambda x: int(x) if x else -1, vals))
                            face.append(val_list)
                        self.faces.append(face)
            
    def render(self) -> None:
        glEnable(GL_DEPTH_TEST)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Optionally, set up lighting and materials here

        # Draw the parsed OBJ model
        glBegin(GL_TRIANGLES)
        for face in self.faces:
            for vertexIndex, texCoordIndex, normIndex in face:
                # indices are 1 indexed in .obj
                vertexIndex -= 1
                texCoordIndex -= 1
                normIndex -= 1
                if texCoordIndex >= 0:
                    glTexCoord2fv(self.tex_coords[texCoordIndex])
                if normIndex >= 0:
                    glNormal3fv(self.norms[normIndex])
                glVertex3fv(self.vertices[vertexIndex])
        glEnd()

        glutSwapBuffers()
        
