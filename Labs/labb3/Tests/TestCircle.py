from Geometries import Circle
import unittest
import sys
sys.path.append(".")


class TestCircle(unittest.TestCase):
    def test_circle_x(self):
        circle = Circle.Circle(x=0, y=0, radius=1)
        self.assertEqual(circle.x, 0)

    def test_circle_y(self):
        circle = Circle.Circle(x=0, y=0, radius=1)
        self.assertEqual(circle.y, 0)

    def test_circle_x_y(self):
        circle = Circle.Circle(x=1, y=1, radius=1)
        self.assertEqual(circle.x, 1)
        self.assertEqual(circle.y, 1)

    def test_circle_x_y_type(self):
        circle = Circle.Circle(x=1, y=1, radius=1)
        self.assertIsInstance(circle.x, float)
        self.assertIsInstance(circle.y, float)

    def test_circle_x_y_type_error(self):
        with self.assertRaises(TypeError):
            Circle.Circle(x="1", y="1", radius=1)

    def test_circle_radius(self):
        circle = Circle.Circle(x=0, y=0, radius=1)
        self.assertEqual(circle.radius, 1)

    def test_circle_radius_type(self):
        circle = Circle.Circle(x=0, y=0, radius=1)
        self.assertIsInstance(circle.radius, float)

    def test_circle_radius_type_error(self):
        with self.assertRaises(TypeError):
            Circle.Circle(x=0, y=0, radius="1")

    def test_circle_str(self):
        circle = Circle.Circle(x=1, y=1, radius=1)
        self.assertEqual(str(circle), "(1.0, 1.0, 1.0)")

    def test_circle_repr(self):
        circle = Circle.Circle(x=1, y=1, radius=1)
        self.assertEqual(repr(circle), "Circle(1.0, 1.0, 1.0)")

    def test_circle_translate(self):
        circle = Circle.Circle(x=1, y=1, radius=1)
        circle.translate(2, 2)
        self.assertEqual(circle.x, 3.0)
        self.assertEqual(circle.y, 3.0)

    def test_circle_translate_type_error(self):
        circle = Circle.Circle(x=1, y=1, radius=1)
        with self.assertRaises(TypeError):
            circle.translate("2", "2")

    def test_circle_area(self):
        circle = Circle.Circle(x=0, y=0, radius=2)
        self.assertEqual(circle.area, 12.566370614359172)

    def test_circle_perimeter(self):
        circle = Circle.Circle(x=0, y=0, radius=2)
        self.assertEqual(circle.perimeter, 12.566370614359172)

    def test_circle_is_unit_circle(self):
        circle = Circle.Circle(x=0, y=0, radius=1)
        self.assertTrue(circle.is_unit_circle())

    def test_circle_is_not_unit_circle(self):
        circle = Circle.Circle(x=0, y=0, radius=2)
        self.assertFalse(circle.is_unit_circle())

    def test_circle_is_inside(self):
        circle = Circle.Circle(x=0, y=0, radius=1)
        self.assertTrue(circle.is_inside(0, 0))

    def test_circle_is_not_inside(self):
        circle = Circle.Circle(x=0, y=0, radius=1)
        self.assertFalse(circle.is_inside(2, 2))
