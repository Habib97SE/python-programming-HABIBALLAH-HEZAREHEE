from .Geometri import Geometri
import math
import matplotlib.pyplot as plt


class Circle(Geometri):
    def __init__(self, x: float, y: float, radius: float) -> None:
        """
            Initialize the circle with x, y and radius.
            Parameters:
                x: float - x coordinate middle of the circle
                y: float - y coordinate middle of the circle
                radius: float - radius of the circle
            Returns:
                None : None
        """
        super().__init__(x, y)
        self.radius = radius

    @property
    def area(self) -> float:
        """
            Returns the area of the circle.
            Returns:
                float : area of the circle
        """
        return math.pi * (self.radius ** 2)

    @property
    def perimeter(self) -> float:
        """
            Returns the perimeter of the circle.
            Returns:
                float : perimeter of the circle
        """
        return 2 * (math.pi * self.radius)

    @property
    def radius(self) -> float:
        """
            Returns the radius of the circle.
            Returns:
                float : radius of the circle
        """
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        """
            Sets the radius of the circle.
            Parameters:
                value: float - radius of the circle
            Returns:
                None : None
        """
        if isinstance(value, int):
            value = float(value)
        if not isinstance(value, float):
            raise TypeError("radius must be float.")
        self._radius = value

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.radius})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.radius})"

    def __eq__(self, other) -> bool:
        return self.area == other.area

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

    def translate(self, x: float, y: float) -> None:
        """
            Translates the circle with x and y. If x or y is not a float or int it raises a TypeError. 
            Parameters:
                x: float - x coordinate to translate the circle
                y: float - y coordinate to translate the circle
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

    def is_unit_circle(self) -> bool:
        """
            Returns True if the circle is a unit circle.
            Returns:
                bool : True if the circle is a unit circle
        """
        return self.radius == 1

    def is_inside(self, x: float, y: float) -> bool:
        """
            Returns True if x and y is greater than self._x and self._y
            and x and y are less than radius.
            otherwise returns False
        """
        if x >= self.x and x <= self.radius:
            return True
        return False

    # Draw the circle on plot
    def draw(self) -> None:
        """
            Draws the circle on a plot.
        """
        fig, ax = plt.subplots()
        circle = plt.Circle((self.x, self.y), self.radius, color="r")
        ax.add_artist(circle)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        plt.show()
