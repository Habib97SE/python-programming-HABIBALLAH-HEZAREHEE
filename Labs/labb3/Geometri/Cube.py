from .Geometri import Geometri
import matplotlib.pyplot as plt


class Cube(Geometri):
    def __init__(self, x: float, y: float, width, height, length) -> None:
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.length = length

    @property
    def area(self) -> float:
        return 6 * (self.width * self.height)

    @property
    def perimeter(self) -> float:
        return 12 * self.width

    @property
    def volume(self) -> float:
        return self.width * self.height * self.length

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
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, value: float) -> None:
        if isinstance(value, int):
            value = float(value)
        if not isinstance(value, float):
            raise TypeError("length must be a float.")
        self._length = value

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.width}, {self.height}, {self.length})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.width}, {self.height}, {self.length})"

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
        if x >= self.x and x <= self.width:
            if y >= self.y and y <= self.height:
                return True
        return False

    # Draw the cube on plot
    def draw(self) -> None:
        fig, ax = plt.subplots()
        cube = plt.Rectangle((self.x, self.y), self.width,
                             self.height, color="r")
        ax.add_artist(cube)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        plt.show()
