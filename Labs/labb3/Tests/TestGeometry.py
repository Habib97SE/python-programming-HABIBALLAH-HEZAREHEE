from Geometries import Geometry
import unittest
import sys
sys.path.append(".")


class TestGeometry(unittest.TestCase):
    def test_Geometry_x(self):
        geometry = Geometry.Geometry(x=0, y=0)
        self.assertEqual(geometry.x, 0)

    def test_Geometry_y(self):
        geometry = Geometry.Geometry(x=0, y=0)
        self.assertEqual(geometry.y, 0)

    def test_Geometry_x_y(self):
        geometry = Geometry.Geometry(x=1, y=1)
        self.assertEqual(geometry.x, 1)
        self.assertEqual(geometry.y, 1)

    def test_Geometry_x_y_type(self):
        geometry = Geometry.Geometry(x=1, y=1)
        self.assertIsInstance(geometry.x, float)
        self.assertIsInstance(geometry.y, float)

    def test_Geometry_x_y_type_error(self):
        with self.assertRaises(TypeError):
            Geometry.Geometry(x="1", y="1")

    def test_Geometry_str(self):
        geometry = Geometry.Geometry(x=1, y=1)
        self.assertEqual(str(geometry), "(1.0, 1.0)")

    def test_Geometry_repr(self):
        geometry = Geometry.Geometry(x=1, y=1)
        self.assertEqual(repr(geometry), "Geometry(1.0, 1.0)")

    def test_Geometry_translate(self):
        geometry = Geometry.Geometry(x=1, y=1)
        geometry.translate(2, 2)
        self.assertEqual(geometry.x, 3.0)
        self.assertEqual(geometry.y, 3.0)

    def test_Geometry_translate_type_error(self):
        geometry = Geometry.Geometry(x=1, y=1)
        with self.assertRaises(TypeError):
            geometry.translate("2", "2")


def main():
    unittest.main()
