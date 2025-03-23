import math
import pygame
import numpy as np

def euler_to_rotation_matrix(pitch, yaw, roll):
    """
    Convert Euler angles (pitch, yaw, roll) into a 3x3 rotation matrix.
    Angles should be given in **radians**.
    """
    # Rotation around X-axis (Pitch)
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(pitch), -np.sin(pitch)],
        [0, np.sin(pitch), np.cos(pitch)]
    ])
    
    # Rotation around Y-axis (Yaw)
    Ry = np.array([
        [np.cos(yaw), 0, np.sin(yaw)],
        [0, 1, 0],
        [-np.sin(yaw), 0, np.cos(yaw)]
    ])
    
    # Rotation around Z-axis (Roll)
    Rz = np.array([
        [np.cos(roll), -np.sin(roll), 0],
        [np.sin(roll), np.cos(roll), 0],
        [0, 0, 1]
    ])

    # Combine rotations: R = Rz * Ry * Rx (applied in ZYX order)
    return Rz @ Ry @ Rx


class Vertex:
    def __init__(self, position, coordinate_system="global") -> None:
        self.coordinate_system = coordinate_system
        self.position = position
    
    def __str__(self) -> str:
        return f"Vertex({self.position.x}, {self.position.y}, {self.position.z})"
    
    def __repr__(self) -> str:
        return self.__str__()

    def _pos_on_screen(self, camera, w, h):
        aspect_ratio = w / h
        near = camera.near
        far = camera.far
        f = 1 / np.tan(np.radians(camera.fov) / 2)

        # Projection matrix (Perspective Projection)
        projection_matrix = np.array([
            [f / aspect_ratio, 0, 0, 0],
            [0, f, 0, 0],
            [0, 0, (far + near) / (near - far), (2 * far * near) / (near - far)],
            [0, 0, -1, 0]
        ])

        # Convert point to numpy array
        point = np.array([self.position.x, self.position.y, self.position.z])

        # Transform point to camera space
        relative_pos = point - np.array([camera.position.x, camera.position.y, camera.position.z])

        # Convert Euler angles to rotation matrix
        rotation_matrix = camera.rotation.get_rotation_matrix()

        # Rotate into camera space
        camera_space_point = rotation_matrix @ relative_pos

        # Convert to homogeneous coordinates (4D)
        x, y, z = camera_space_point
        if z <= 0:  # Ignore points behind the camera
            return None  

        homogeneous_point = np.array([x, y, z, 1])
        projected = projection_matrix @ homogeneous_point

        # Normalize by w
        if projected[3] == 0:
            return None  

        ndc_x = projected[0] / projected[3]
        ndc_y = projected[1] / projected[3]

        # Convert to screen space
        screen_x = (ndc_x + 1) * 0.5 * w
        screen_y = (1 - ndc_y) * 0.5 * h

        return screen_x, screen_y


    def draw(self, sheet, camera):
        """ Draws the vertex as a small circle on the screen if it's visible. """
        screen_pos = self._pos_on_screen(camera, sheet.get_width(), sheet.get_height())
        if screen_pos:
            pygame.draw.circle(sheet, (255, 255, 255), (int(screen_pos[0]), int(screen_pos[1])), 2)


class Normal:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z