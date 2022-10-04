from Geometries import Rectangle
import unittest
import sys
sys.path.append(".")


class TestRectangle(unittest.TestCase):
    def test_rectangle_x(self):
        rectangle = Rectangle.Rectangle(x=0, y=0, width=1, height=1)
        self.assertEqual(rectangle.x, 0)

    def test_rectangle_y(self):
        rectangle = Rectangle.Rectangle(x=0, y=0, width=1, height=1)
        self.assertEqual(rectangle.y, 0)

    def test_rectangle_x_y(self):
        rectangle = Rectangle.Rectangle(x=1, y=1, width=1, height=1)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 1)

    def test_rectangle_x_y_type(self):
        rectangle = Rectangle.Rectangle(x=1, y=1, width=1, height=1)
        self.assertIsInstance(rectangle.x, float)
        self.assertIsInstance(rectangle.y, float)

    def test_rectangle_x_y_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle.Rectangle(x="1", y="1", width=1, height=1)

    def test_rectangle_width(self):
        rectangle = Rectangle.Rectangle(x=0, y=0, width=1, height=1)
        self.assertEqual(rectangle.width, 1)

    def test_rectangle_height(self):
        rectangle = Rectangle.Rectangle(x=0, y=0, width=1, height=1)
        self.assertEqual(rectangle.height, 1)

    def test_rectangle_width_height(self):
        rectangle = Rectangle.Rectangle(x=0, y=0, width=2, height=2)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 2)

    def test_rectangle_width_height_type(self):
        rectangle = Rectangle.Rectangle(x=0, y=0, width=2, height=2)
        self.assertIsInstance(rectangle.width, float)
        self.assertIsInstance(rectangle.height, float)

    def test_rectangle_width_height_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle.Rectangle(x=0, y=0, width="2", height="2")

    def test_rectangle_str(self):
        rectangle = Rectangle.Rectangle(x=1, y=1, width=1, height=1)
        self.assertEqual(str(rectangle), "(1.0, 1.0, 1.0, 1.0)")

    def test_rectangle_repr(self):
        rectangle = Rectangle.Rectangle(x=1, y=1, width=1, height=1)
        self.assertEqual(repr(rectangle), "Rectangle(1.0, 1.0, 1.0, 1.0)")

    def test_rectangle_translate(self):
        rectangle = Rectangle.Rectangle(x=1, y=1, width=1, height=1)
        rectangle.translate(2, 2)
        self.assertEqual(rectangle.x, 3.0)
        self.assertEqual(rectangle.y, 3.0)

    def test_rectangle_translate_type_error(self):
        rectangle = Rectangle.Rectangle(x=1, y=1, width=1, height=1)
        with self.assertRaises(TypeError):
            rectangle.translate("2", "2")

    def test_rectangle_area(self):
        rectangle = Rectangle.Rectangle(x=0, y=0, width=2, height=2)
        self.assertEqual(rectangle.area, 4.0)

    def test_rectangle_perimeter(self):
        rectangle = Rectangle.Rectangle(x=0, y=0, width=2, height=2)
        self.assertEqual(rectangle.perimeter, 8.0)
