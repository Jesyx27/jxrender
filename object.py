class Object:
    def __init__(self, name, position, rotation=[], mesh=None, visible=True):
        self.name = name
        self.position = position
        self.mesh = mesh
        self.rotation = rotation
        self.visible = True

    def rotate(self, rotation):
        # Update mesh to reflect new rotation
        self.rotation = rotation

        for vertex in self.mesh.vertices:
            vertex.rotate(rotation)

    def walk(self, position):
        self.position = position

    def draw(self, screen, camera):
        if self.mesh:
            self.mesh.draw(screen, camera)