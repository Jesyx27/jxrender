import numpy as np

class Rotation:
    def __init__(self, x, y, z):
        """ Initialize the rotation with the given angles x, y, z """
        # Map to -pi to pi range
        self.x = x % (2 * np.pi)
        self.y = y % (2 * np.pi)
        self.z = z % (2 * np.pi)

    def rotate(self, d_rotation):
        """ Rotate the object by a given delta rotation [dx, dy, dz] """
        self.x = (self.x + d_rotation[0]) % (2 * np.pi)
        self.y = (self.y + d_rotation[1]) % (2 * np.pi)
        self.z = (self.z + d_rotation[2]) % (2 * np.pi)

    def to_vector(self):
        """ Return the rotation as a list [x, y, z] """
        return np.array([self.x, self.y, self.z])

    def get_rotation_matrix(self):
        """ Compute the full 3D rotation matrix using yaw (Z), pitch (Y), roll (X) """

        cx, cy, cz = np.cos([self.x, self.y, self.z])  # Compute cosines
        sx, sy, sz = np.sin([self.x, self.y, self.z])  # Compute sines

        # Rotation matrices for each axis
        rot_x = np.array([[1, 0, 0], [0, cx, -sx], [0, sx, cx]])  # Roll
        rot_y = np.array([[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]])  # Pitch
        rot_z = np.array([[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]])  # Yaw

        # Combine: First apply yaw (Z), then pitch (Y), then roll (X)
        rotation_matrix = rot_z @ rot_y @ rot_x  
        return rotation_matrix

    def __str__(self):
        return f"Rotation({self.x}, {self.y}, {self.z})"
    
    def __repr__(self):
        return self.__str__()
