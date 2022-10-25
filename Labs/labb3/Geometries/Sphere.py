from .Geometry import Geometry
import math
import numpy as np
import matplotlib.pyplot as plt


class Sphere(Geometry):
    def __init__(self, x: float, y: float, radius: float) -> None:
        """
            Initialize the sphere with x, y and radius. 
            Parameters:
                x: float - x coordinate middle of the sphere
                y: float - y coordinate middle of the sphere
                radius: float - radius of the sphere
            Returns:
                None : None
        """
        super().__init__(x, y)
        self.radius = radius

    @property
    def area(self) -> float:
        """
            Returns the area of the sphere.
        """
        return 4 * math.pi * (self.radius ** 2)

    @property
    def perimeter(self) -> float:
        """
            Returns the perimeter of the sphere.
        """
        return 2 * math.pi * self.radius

    @property
    def volume(self) -> float:
        """
            Returns the volume of the sphere.
        """
        return (4/3) * math.pi * (self.radius ** 3)

    @property
    def radius(self) -> float:
        """
            Returns the radius of the sphere.
        """
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        """
            Sets the radius of the sphere.
        """
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
        """
            Translates the sphere with x and y. 
            Parameters:
                x: float - x coordinate
                y: float - y coordinate
            Returns:
                None : None
        """
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
        if not x >= self.x or not x <= self.radius:
            return False
        if not y >= self.y or not y <= self.radius:
            return False
        return True

    # Draw the sphere on plot
    def draw(self) -> None:
        """
            Draws the sphere on plot.

            Source: https://www.youtube.com/watch?v=DV4GjHH-fvc&ab_channel=SkillUpwithGenie
        """
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        u = np.linspace(0, 2*np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        r = self._radius

        x = r * np.outer(np.cos(u), np.sin(v))
        y = r * np.outer(np.sin(u), np.sin(v))
        z = r * np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_surface(x, y, z, rstride=5, cstride=5)
        plt.title(f"Sphere with radius {self._radius}")
        plt.show()
