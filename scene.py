from itertools import chain, combinations
from mesh.edge import Edge

class Scene:
    def __init__(self, name, entities, camera, sheet):
        self.name = name
        self.entities = entities
        self.camera = camera
        self.sheet = sheet

    def render(self):
        faces = list(chain(*[entity.mesh.faces for entity in self.entities]))
        faces = list(filter(lambda face: face.visible, faces))
        faces.sort(key=lambda face: face.distance_to_camera(self.camera), reverse=True)

        vertices = list([face.vertices for face in faces])

        # Create edges from vertices
        for vertex in vertices:
            for edge in combinations(vertex, 2):
                ORANGE = (255, 165, 0)
                Edge(*edge, ORANGE, 10).draw(self.sheet, self.camera)
        

        for face in faces:
            face.draw(self.sheet, self.camera)

    def add_entity(self, entity):
        if entity not in self.entities:
            self.entities.append(entity)