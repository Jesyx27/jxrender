import numpy as np

class Position():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def to_vector(self):
        return np.array([self.x, self.y, self.z])

    def distance_to_camera(self, camera):
        """ Returns Euclidean distance to the camera. """
        dx = self.x - camera.position.x
        dy = self.y - camera.position.y
        dz = self.z - camera.position.z

        return np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, scalar):
        return Position(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __truediv__(self, scalar):
        return Position(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def __str__(self) -> str:
        return f"Position({self.x}, {self.y}, {self.z})"
    
    def __repr__(self) -> str:
        return self.__str__()