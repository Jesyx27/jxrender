from object import Object
import numpy as np

class Camera(Object):
    def __init__(self, position, rotation, fov, near=0.1, far=1000):
        #super().__init__("camera", position, rotation)
        self.name = "camera"
        self.position = position
        self.rotation = rotation
        print(self.rotation)
        self.fov = fov
        self.near = near
        self.far = far

    def walk(self, direction, speed=0.5):
        """ Moves the camera in the given direction relative to its rotation. """
        yaw_rad = self.rotation.y  # Yaw (horizontal rotation)

        if direction == 'left':
            move_vector = np.array([np.cos(yaw_rad), np.sin(yaw_rad), 0])
        elif direction == 'right':
            move_vector = -np.array([np.cos(yaw_rad), np.sin(yaw_rad), 0])
        elif direction == 'forward':
            move_vector = -np.array([np.sin(yaw_rad), -np.cos(yaw_rad), 0])
        elif direction == 'backward':
            move_vector = np.array([np.sin(yaw_rad), -np.cos(yaw_rad), 0])
        elif direction == 'up':
            move_vector = np.array([0, 0, 1])
        elif direction == 'down':
            move_vector = -np.array([0, 0, 1])
        else:
            raise ValueError("Invalid movement direction")

        # Update position
        self.position.x += move_vector[0] * speed
        self.position.y += move_vector[1] * speed
        self.position.z += move_vector[2] * speed
