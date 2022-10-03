from .Geometri import Geometri
import math
import matplotlib.pyplot as plt


class Sphere(Geometri):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y)
        self.radius = radius

    @property
    def area(self) -> float:
        return 4 * math.pi * (self.radius ** 2)

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    @property
    def volume(self) -> float:
        return (4/3) * math.pi * (self.radius ** 3)

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if isinstance(value, int):
            value = float(value)
        if not isinstance(value, float):
            raise TypeError("radius must be a float.")
        self._radius = value

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.radius})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.radius})"

    def __eq__(self, other) -> bool:
        return self.volume == other.volume

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other) -> bool:
        return self.volume < other.volume

    def __le__(self, other) -> bool:
        return self.volume <= other.volume

    def __gt__(self, other) -> bool:
        return self.volume > other.volume

    def __ge__(self, other) -> bool:
        return self.volume >= other.volume

    def translate(self, x: float, y: float) -> None:
        if isinstance(x, int):
            x = float(x)
        if isinstance(y, int):
            y = float(y)
        if not isinstance(x, float) or not isinstance(y, float):
            raise TypeError("x and y should be of type float.")
        self._x += x
        self._y += y

    def is_inside(self, x: float, y: float) -> bool:
        """
            Returns True if x and y is greater than self._x and self._y
            and x and y are less than width and height.
            otherwise returns False
        """
        if x >= self.x and x <= self.radius:
            if y >= self.y and y <= self.radius:
                return True
        return False

    # Draw the sphere on plot
    def draw(self) -> None:
        fig, ax = plt.subplots()
        circle = plt.Circle((self.x, self.y), self.radius, color="r")
        ax.add_artist(circle)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        plt.show()
