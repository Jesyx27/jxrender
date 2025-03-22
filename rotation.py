import math

class Rotation:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

        self.cos_x = math.cos(math.radians(x))
        self.sin_x = math.sin(math.radians(x))
        self.cos_y = math.cos(math.radians(y))
        self.sin_y = math.sin(math.radians(y))
        self.cos_z = math.cos(math.radians(z))
        self.sin_z = math.sin(math.radians(z))

    def rotate(self, rotation) -> None:
        values = [rotation.x, rotation.y, rotation.z] if isinstance(rotation, Rotation) else rotation
        self.x, self.y, self.z = values

        self.cos_x = math.cos(math.radians(self.x))
        self.sin_x = math.sin(math.radians(self.x))
        self.cos_y = math.cos(math.radians(self.y))
        self.sin_y = math.sin(math.radians(self.y))
        self.cos_z = math.cos(math.radians(self.z))
        self.sin_z = math.sin(math.radians(self.z))

    def __add__(self, rotation):
        if isinstance(rotation, Rotation):
            return Rotation(self.x + rotation.x, self.y + rotation.y, self.z + rotation.z)
        else:
            return Rotation(self.x + rotation[0], self.y + rotation[1], self.z + rotation[2])

    def __iadd__(self, rotation):
        if isinstance(rotation, Rotation):
            self.rotate(self + rotation)
        else:
            self.rotate(self + Rotation(*rotation))
            print(self)
        return self
    
    def __mul__(self, rotation):
        if isinstance(rotation, Rotation):
            return Rotation(self.x * rotation.x, self.y * rotation.y, self.z * rotation.z)
        else:
            return Rotation(self.x * rotation[0], self.y * rotation[1], self.z * rotation[2])

    def __imul__(self, rotation):
        if isinstance(rotation, Rotation):
            self.rotate(self * rotation)
        else:
            self.rotate(self * Rotation(rotation[0], rotation[1], rotation[2]))
        return self

    def __truediv__(self, rotation):
        if isinstance(rotation, Rotation):
            return Rotation(self.x / rotation.x, self.y / rotation.y, self.z / rotation.z)
        else:
            return Rotation(self.x / rotation[0], self.y / rotation[1], self.z / rotation[2])
    
    def __itruediv__(self, rotation):
        if isinstance(rotation, Rotation):
            self.rotate(self / rotation)
        else:
            self.rotate(self / Rotation(rotation[0], rotation[1], rotation[2]))
        return self
    
    def __str__(self):
        return f"Rotation: x={self.x}, y={self.y}, z={self.z}"