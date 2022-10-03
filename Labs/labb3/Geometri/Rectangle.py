from .Geometri import Geometri
import matplotlib.pyplot as plt


class Rectangle(Geometri):
    """
        This class represents a rectangle. The rectangle has a width and a height and middle point x and y. 
        The rectangle can be translated and can check if a point is inside the rectangle.

    """

    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        super().__init__(x, y)
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        if isinstance(value, int):
            value = float(value)
        if not isinstance(value, float):
            raise TypeError("width must be a float.")
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        if isinstance(value, int):
            value = float(value)
        if not isinstance(value, float):
            raise TypeError("height must be a float.")
        self._height = value

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return (2 * self.width) + (2 * self.height)

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.width}, {self.height})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.width}, {self.height})"

    def __eq__(self, other) -> bool:
        if self.area == other.area:
            return True
        return False

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other) -> bool:
        return self.area() < other.area()

    def __le__(self, other) -> bool:
        return self.area() <= other.area()

    def __gt__(self, other) -> bool:
        return self.area() > other.area()

    def __ge__(self, other) -> bool:
        return self.area() >= other.area()

    def is_square(self) -> bool:
        if self.width == self.height:
            return True
        return False

    def translate(self, x: float, y: float) -> None:
        if isinstance(x, int):
            x = float(x)
        if isinstance(y, int):
            y = float(y)
        if not isinstance(x, float) or not isinstance(y, float):
            raise TypeError("x and y should be of type float.")

        self.x += x
        self.y += y

    def is_inside(self, x: float, y: float) -> bool:
        # x and y must be greater than self.x and self.y but less than radius
        if isinstance(x, int):
            x = float(x)
        if isinstance(y, int):
            y = float(y)
        if not self.is_type_float(x, y):
            raise TypeError("x and y should be of type float.")
        if x > self.x and x < self.radius:
            return True
        return False

    def draw(self) -> None:
        plt.plot(self.x, self.y, "ro")
        plt.show()
