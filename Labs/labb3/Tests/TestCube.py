from Geometries import Cube
import unittest
import sys
sys.path.append(".")


class TestCube(unittest.TestCase):
    def test_cube_x(self):
        cube = Cube.Cube(x=0, y=0, width=1, height=1, length=1)
        self.assertEqual(cube.x, 0)

    def test_cube_y(self):
        cube = Cube.Cube(x=0, y=0, width=1, height=1, length=1)
        self.assertEqual(cube.y, 0)

    def test_cube_x_y(self):
        cube = Cube.Cube(x=1, y=1, width=1, height=1, length=1)
        self.assertEqual(cube.x, 1)
        self.assertEqual(cube.y, 1)

    def test_cube_x_y_type(self):
        cube = Cube.Cube(x=1, y=1, width=1, height=1, length=1)
        self.assertIsInstance(cube.x, float)
        self.assertIsInstance(cube.y, float)

    def test_cube_x_y_type_error(self):
        with self.assertRaises(TypeError):
            Cube.Cube(x="1", y="1", width=1, height=1, length=1)

    def test_cube_width(self):
        cube = Cube.Cube(x=0, y=0, width=1, height=1, length=1)
        self.assertEqual(cube.width, 1)

    def test_cube_width_type(self):
        cube = Cube.Cube(x=0, y=0, width=1, height=1, length=1)
        self.assertIsInstance(cube.width, float)

    def test_cube_width_type_error(self):
        with self.assertRaises(TypeError):
            Cube.Cube(x=0, y=0, width="1", height=1, length=1)

    def test_cube_height(self):
        cube = Cube.Cube(x=0, y=0, width=1, height=1, length=1)
        self.assertEqual(cube.height, 1)

    def test_cube_height_type(self):
        cube = Cube.Cube(x=0, y=0, width=1, height=1, length=1)
        self.assertIsInstance(cube.height, float)

    def test_cube_height_type_error(self):
        with self.assertRaises(TypeError):
            Cube.Cube(x=0, y=0, width=1, height="1", length=1)

    def test_cube_length(self):
        cube = Cube.Cube(x=0, y=0, width=1, height=1, length=1)
        self.assertEqual(cube.length, 1)

    def test_cube_length_type(self):
        cube = Cube.Cube(x=0, y=0, width=1, height=1, length=1)
        self.assertIsInstance(cube.length, float)

    def test_cube_length_type_error(self):
        with self.assertRaises(TypeError):
            Cube.Cube(x=0, y=0, width=1, height=1, length="1")

    def test_cube_str(self):
        cube = Cube.Cube(x=1, y=1, width=1, height=1, length=1)
        self.assertEqual(str(cube), "(1.0, 1.0, 1.0, 1.0, 1.0)")

    def test_cube_repr(self):
        cube = Cube.Cube(x=1, y=1, width=1, height=1, length=1)
        self.assertEqual(repr(cube), "Cube(1.0, 1.0, 1.0, 1.0, 1.0)")

    def test_cube_translate(self):
        cube = Cube.Cube(x=1, y=1, width=1, height=1, length=1)
        cube.translate(2, 2)
        self.assertEqual(cube.x, 3.0)
        self.assertEqual(cube.y, 3.0)

    def test_cube_translate_type_error(self):
        cube = Cube.Cube(x=1, y=1, width=1, height=1, length=1)
        with self.assertRaises(TypeError):
            cube.translate("2", "2")

    def test_cube_area(self):
        cube = Cube.Cube(x=0, y=0, width=2, height=2, length=2)
        self.assertEqual(cube.area, 24.0)

    def test_cube_perimeter(self):
        cube = Cube.Cube(x=0, y=0, width=2, height=2, length=2)
        self.assertEqual(cube.perimeter, 24.0)

    def test_cube_volume(self):
        cube = Cube.Cube(x=0, y=0, width=2, height=2, length=2)
        self.assertEqual(cube.volume, 8.0)

    def test_cube_is_inside(self):
        cube = Cube.Cube(x=0, y=0, width=1, height=1, length=1)
        self.assertTrue(cube.is_inside(0, 0))

    def test_cube_is_not_inside(self):
        cube = Cube.Cube(x=0, y=0, width=1, height=1, length=1)
        self.assertFalse(cube.is_inside(2, 2))
