import math
import pygame
import numpy as np

class Vertex:
    def __init__(self, x, y, z, coordinate_system="global") -> None:
        self.coordinate_system = coordinate_system
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self) -> str:
        return f"Vertex({self.x}, {self.y}, {self.z})"
    
    def __repr__(self) -> str:
        return self.__str__()

    def _pos_on_screen(self, camera, w, h):
        # Translate vertex relative to camera position
        rel_x = self.x - camera.position.x
        rel_y = self.y - camera.position.y
        rel_z = self.z - camera.position.z
        
        # Rotate around X-axis
        temp_y = rel_y * np.cos(camera.rotation.x) - rel_z * np.sin(camera.rotation.x)
        temp_z = rel_y * np.sin(camera.rotation.x) + rel_z * np.cos(camera.rotation.x)
        rel_y, rel_z = temp_y, temp_z
        
        # Rotate around Y-axis
        temp_x = rel_x * np.cos(camera.rotation.y) + rel_z * np.sin(camera.rotation.y)
        temp_z = -rel_x * np.sin(camera.rotation.y) + rel_z * np.cos(camera.rotation.y)
        rel_x, rel_z = temp_x, temp_z
        
        # Rotate around Z-axis
        temp_x = rel_x * np.cos(camera.rotation.z) - rel_y * np.sin(camera.rotation.z)
        temp_y = rel_x * np.sin(camera.rotation.z) + rel_y * np.cos(camera.rotation.z)
        rel_x, rel_y = temp_x, temp_y
        
        # Avoid division by zero (if vertex is behind camera)
        if rel_z <= 0:
            return None  # Vertex is behind the camera
        
        # Perspective projection
        fov_factor = math.tan(math.radians(camera.fov) / 2)
        screen_x = (rel_x / (rel_z * fov_factor)) * (w / 2) + (w / 2)
        screen_y = (rel_y / (rel_z * fov_factor)) * (h / 2) + (h / 2)
        
        return screen_x, screen_y
    
    def distance_to_camera(self, camera):
        dx = self.x - camera.position.x
        dy = self.y - camera.position.y
        dz = self.z - camera.position.z

        return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

    def draw(self, sheet, camera):
        screen_pos = self._pos_on_screen(camera, sheet.get_width(), sheet.get_height())
        if screen_pos:
            pygame.draw.circle(sheet, (255, 255, 255), (int(screen_pos[0]), int(screen_pos[1])), 2)