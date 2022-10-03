import unittest
from Geometri import Geometri, Rectangle, Circle, Cube, Sphere


class TestGeometri(unittest.TestCase):
    def test_geometri_x(self):
        geometri = Geometri.Geometri(x=0, y=0)
        self.assertEqual(geometri.x, 0)

    def test_geometri_y(self):
        geometri = Geometri.Geometri(x=0, y=0)
        self.assertEqual(geometri.y, 0)

    def test_geometri_x_y(self):
        geometri = Geometri.Geometri(x=1, y=1)
        self.assertEqual(geometri.x, 1)
        self.assertEqual(geometri.y, 1)

    def test_geometri_x_y_type(self):
        geometri = Geometri.Geometri(x=1, y=1)
        self.assertIsInstance(geometri.x, float)
        self.assertIsInstance(geometri.y, float)

    def test_geometri_x_y_type_error(self):
        with self.assertRaises(TypeError):
            Geometri.Geometri(x="1", y="1")

    def test_geometri_str(self):
        geometri = Geometri.Geometri(x=1, y=1)
        self.assertEqual(str(geometri), "(1.0, 1.0)")

    def test_geometri_repr(self):
        geometri = Geometri.Geometri(x=1, y=1)
        self.assertEqual(repr(geometri), "Geometri(1.0, 1.0)")

    def test_geometri_translate(self):
        geometri = Geometri.Geometri(x=1, y=1)
        geometri.translate(2, 2)
        self.assertEqual(geometri.x, 3.0)
        self.assertEqual(geometri.y, 3.0)

    def test_geometri_translate_type_error(self):
        geometri = Geometri.Geometri(x=1, y=1)
        with self.assertRaises(TypeError):
            geometri.translate("2", "2")

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


def main():
    print("Test begins ...")
    unittest.main()
    print("Test ended.")


if __name__ == "__main__":
    main()
