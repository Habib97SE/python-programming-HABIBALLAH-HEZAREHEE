from Geometries import Sphere
import unittest
import sys
sys.path.append(".")


class TestSphere(unittest.TestCase):
    def test_sphere_x(self):
        sphere = Sphere.Sphere(x=0, y=0, radius=1)
        self.assertEqual(sphere.x, 0)

    def test_sphere_y(self):
        sphere = Sphere.Sphere(x=0, y=0, radius=1)
        self.assertEqual(sphere.y, 0)

    def test_sphere_x_y(self):
        sphere = Sphere.Sphere(x=1, y=1, radius=1)
        self.assertEqual(sphere.x, 1)
        self.assertEqual(sphere.y, 1)

    def test_sphere_x_y_type(self):
        sphere = Sphere.Sphere(x=1, y=1, radius=1)
        self.assertIsInstance(sphere.x, float)
        self.assertIsInstance(sphere.y, float)

    def test_sphere_x_y_type_error(self):
        with self.assertRaises(TypeError):
            Sphere.Sphere(x="1", y="1", radius=1)

    def test_sphere_radius(self):
        sphere = Sphere.Sphere(x=0, y=0, radius=1)
        self.assertEqual(sphere.radius, 1)

    def test_sphere_radius_type(self):
        sphere = Sphere.Sphere(x=0, y=0, radius=1)
        self.assertIsInstance(sphere.radius, float)

    def test_sphere_radius_type_error(self):
        with self.assertRaises(TypeError):
            Sphere.Sphere(x=0, y=0, radius="1")

    def test_sphere_str(self):
        sphere = Sphere.Sphere(x=1, y=1, radius=1)
        self.assertEqual(str(sphere), "(1.0, 1.0, 1.0)")

    def test_sphere_repr(self):
        sphere = Sphere.Sphere(x=1, y=1, radius=1)
        self.assertEqual(repr(sphere), "Sphere(1.0, 1.0, 1.0)")

    def test_sphere_translate(self):
        sphere = Sphere.Sphere(x=1, y=1, radius=1)
        sphere.translate(2, 2)
        self.assertEqual(sphere.x, 3.0)
        self.assertEqual(sphere.y, 3.0)

    def test_sphere_translate_type_error(self):
        sphere = Sphere.Sphere(x=1, y=1, radius=1)
        with self.assertRaises(TypeError):
            sphere.translate("2", "2")

    def test_sphere_area(self):
        sphere = Sphere.Sphere(x=0, y=0, radius=2)
        self.assertEqual(sphere.area, 50.26548245743669)

    def test_sphere_perimeter(self):
        sphere = Sphere.Sphere(x=0, y=0, radius=2)
        self.assertEqual(sphere.perimeter, 12.566370614359172)

    def test_sphere_volume(self):
        sphere = Sphere.Sphere(x=0, y=0, radius=2)
        self.assertEqual(sphere.volume, 33.510321638291124)

    def test_sphere_is_inside(self):
        sphere = Sphere.Sphere(x=0, y=0, radius=1)
        self.assertTrue(sphere.is_inside(0, 0))

    def test_sphere_is_not_inside(self):
        sphere = Sphere.Sphere(x=0, y=0, radius=1)
        self.assertFalse(sphere.is_inside(2, 2))
