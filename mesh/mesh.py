class Mesh:
    def __init__(self, faces=[], lines=[], verteces=[]):
        self.faces = faces
        self.lines = lines
        self.vertices = verteces

        for face in faces:
            if len(face.child_faces) > 0:
                self.faces.extend(face.child_faces)

    def draw(self, sheet, camera):
        for face in sorted(self.faces, key=lambda face: face.distance_to_camera(camera), reverse=True):
            face.draw(sheet, camera)
        for line in self.lines:
            line.draw(sheet, camera)
        for vertex in self.vertices:
            vertex.draw(sheet, camera)