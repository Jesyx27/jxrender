from object import Object
from util import epsilon
import numpy as np

class Camera(Object):
    def __init__(self, position, rotation, fov, near=0, far=1000):
        super().__init__("camera", position, rotation)
        self.fov = fov
        self.near = near
        self.far = far
    
    def __str__(self):
        return f"<Camera:{self.position}>"

    def __repr__(self):
        return self.__str__()
    
    def look(self, dx, dy):
        self.rotation.rotate([
            self.rotation.x + dx, 
            self.rotation.y + dy, 
            self.rotation.z + 0])

    def walk(self, direction):
        if direction not in ('up', 'down', 'left', 'right', 'forward', 'backward'):
            raise ValueError("Invalid direction")
        
        if direction == 'up':
            self.position.y += 1
        elif direction == 'down':
            self.position.y -= 1
        elif direction == 'left':
            # Move left by camera rotation
            self.position.x -= np.cos(self.rotation.z)
            self.position.y -= np.sin(self.rotation.z)
        elif direction == 'right':
            # Move right by camera rotation
            self.position.x += np.cos(self.rotation.z)
            self.position.y += np.sin(self.rotation.z)
        elif direction == 'forward':
            # Move forward by camera rotation
            self.position.x += np.sin(self.rotation.z)
            self.position.y -= np.cos(self.rotation.z)
        elif direction == 'backward':
            # Move backward by camera rotation
            self.position.x -= np.sin(self.rotation.z)
            self.position.y += np.cos(self.rotation.z)
