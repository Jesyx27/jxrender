import warnings
import pygame
from mesh.vertex import Vertex, Normal
from position import Position
import numpy as np

class Face:
    def __init__(self, vertices, color):
        self.child_faces = []
        self.visible = True

        if len(vertices) != 3:
            warnings.warn("Face has more than 3 vertices. This may cause unexpected behavior.", Warning)
            if len(vertices) < 3:
                raise ValueError("Face must have at least 3 vertices")
            if len(vertices) > 4:
                raise ValueError("Face must have at most 4 vertices")
            
            # Disconnect two faces
            #self.child_faces = [Face(vertices[:3], color), Face(vertices[1:], color)]
            #self.visible = False

        self.vertices = vertices
        self.color = color
        self.normal = self.calculate_normal()
        brightness = (self.normal.y * 255/2 + 255/2) * 0.2 + (self.normal.x * 255/2 + 255/2) * 0.8
        self.color = [brightness , brightness, brightness]

    def distance_to_camera(self, camera):
        x = sum([v.position.x for v in self.vertices]) / len(self.vertices)
        y = sum([v.position.y for v in self.vertices]) / len(self.vertices)
        z = sum([v.position.z for v in self.vertices]) / len(self.vertices)

        center = Position(x, y, z)
        distance = center.distance_to_camera(camera)
        return distance

    def draw(self, sheet, camera):
        if self.visible:
            screen_positions = [v._pos_on_screen(camera, sheet.get_width(), sheet.get_height()) for v in self.vertices]
            if all(screen_positions):
                color = self.color
                pygame.draw.polygon(sheet, color, screen_positions)
    
    def calculate_normal(self):
        """ Calculate the normal of the face. """
        # Get vectors from the first vertex to the other two
        v1 = (self.vertices[1].position - self.vertices[0].position).to_vector()
        v2 = (self.vertices[2].position - self.vertices[0].position).to_vector()

        # Calculate the cross product using numpy
        cross_product = np.cross(v1, v2)

        # Normalize the resulting vector
        norm = np.linalg.norm(cross_product)
        if norm != 0:
            cross_product = cross_product.astype(float) / norm

        return Normal(*cross_product)