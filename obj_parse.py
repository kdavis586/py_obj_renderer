class Obj():
    def __init__(self, filename: str) -> None:
        self.vertices = []
        self.tex_coord = []
        self.norms = []
        self.faces = []
        self._parse_obj(filename)
    
    def _parse_obj(filename: str) -> None:
        if not isinstance(filename, str):
            raise TypeError()
        
