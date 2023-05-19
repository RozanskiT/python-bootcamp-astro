import math

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __mul__(self, scalar):
        """Implement scalar multiplication."""
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def isclose(self, other, rel_tol=1e-9, abs_tol=0.0):
        return (math.isclose(self.x, other.x, rel_tol=rel_tol, abs_tol=abs_tol) and
                math.isclose(self.y, other.y, rel_tol=rel_tol, abs_tol=abs_tol) and
                math.isclose(self.z, other.z, rel_tol=rel_tol, abs_tol=abs_tol))

    def cross(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)

    def angle_between(self, other):
        from math import acos, degrees

        dot_product = self.dot(other)
        mag_self = self.magnitude()
        mag_other = other.magnitude()

        cos_angle = dot_product / (mag_self * mag_other)
        angle_rad = acos(cos_angle)

        return degrees(angle_rad)
    
    def rotate(self, axis, theta):
        """
        Rotate this vector by theta degrees around the specified axis
        """
        theta = math.radians(theta)  # Convert to radians
        axis = axis.normalize()  # Ensure axis is a unit vector

        term1 = self * math.cos(theta)
        term2 = (axis.cross(self)) * math.sin(theta)
        term3 = axis * (axis.dot(self)) * (1 - math.cos(theta))

        return term1 + term2 + term3
    
import unittest

class TestVector3D(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector3D(1, 2, 3)
        self.v2 = Vector3D(4, 5, 6)

    def test_add(self):
        result = self.v1 + self.v2
        self.assertTrue(result.isclose(Vector3D(5, 7, 9)))

    def test_sub(self):
        result = self.v1 - self.v2
        self.assertTrue(result.isclose(Vector3D(-3, -3, -3)))

    def test_dot(self):
        result = self.v1.dot(self.v2)
        self.assertEqual(result, 32)

    def test_cross(self):
        result = self.v1.cross(self.v2)
        self.assertTrue(result.isclose(Vector3D(-3, 6, -3)))

    def test_magnitude(self):
        result = self.v1.magnitude()
        self.assertEqual(result, math.sqrt(14))

    def test_normalize(self):
        result = self.v1.normalize()
        self.assertAlmostEqual(result.x, 1 / math.sqrt(14))
        self.assertAlmostEqual(result.y, 2 / math.sqrt(14))
        self.assertAlmostEqual(result.z, 3 / math.sqrt(14))

    def test_angle_between(self):
        result = self.v1.angle_between(self.v2)
        self.assertAlmostEqual(result, 12.933154491899135)

    def test_rotate(self):
        axis = Vector3D(0, 0, 1)
        result = self.v1.rotate(axis, 90)
        self.assertAlmostEqual(result.x, -2.0)
        self.assertAlmostEqual(result.y, 1.0)
        self.assertAlmostEqual(result.z, 3.0)

if __name__ == '__main__':
    unittest.main()
else:
    print("Importing example module.", __name__)
