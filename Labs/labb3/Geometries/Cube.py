from .Geometry import Geometry
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


class Cube(Geometry):
    def __init__(self, x: float, y: float, z: float, length: float, height: float, depth: float) -> None:
        """
            Initialize the cube with x, y, width, height and length.
            Parameters:
                x: float - x coordinate middle of the cube
                y: float - y coordinate middle of the cube
                length: float - length of the cube (x)
                height: float - height of the cube (y)
                depth: float - depth of the cube (z)
            Returns:
                None : None
        """
        super().__init__(x, y)
        self.z = z
        self.length = length
        self.height = height
        self.depth = depth

    @property
    def area(self) -> float:
        """
            Returns the area of the cube.
        """
        return 6 * (self.width * self.height)

    @property
    def perimeter(self) -> float:
        """
            Returns the perimeter of the cube.
        """
        return 12 * self.width

    @property
    def volume(self) -> float:
        """
            Returns the volume of the cube.
        """
        return self.width * self.height * self.length

    @property
    def length(self) -> float:
        """
            Returns the width of the cube.
        """
        return self._length

    @length.setter
    def length(self, value: float) -> None:
        """
            Sets the width of the cube.
        """
        if isinstance(value, int):
            value = float(value)
        if not isinstance(value, float):
            raise TypeError("width must be a float.")
        self._length = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        if isinstance(value, int):
            value = float(value)
        if not isinstance(value, float):
            raise TypeError("z must be a float.")
        self._z = value

    @property
    def height(self) -> float:
        """
            Returns the height of the cube.
        """
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        """
            Sets the height of the cube.
        """
        if isinstance(value, int):
            value = float(value)
        if not isinstance(value, float):
            raise TypeError("height must be a float.")
        self._height = value

    @property
    def depth(self) -> float:
        """
            Returns the length of the cube.
        """
        return self._depth

    @depth.setter
    def depth(self, value: float) -> None:
        """
            Sets the length of the cube.
        """
        if isinstance(value, int):
            value = float(value)
        if not isinstance(value, float):
            raise TypeError("length must be a float.")
        self._depth = value

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

    def translate(self, x: float, y: float, z: float) -> None:
        """
            Translates the cube with x, y and z. 
            Parameters:
                x: float - x coordinate
                y: float - y coordinate
                z: float - z coordinate
            Returns:
                None : None
        """
        if isinstance(x, int):
            x = float(x)
        if isinstance(y, int):
            y = float(y)
        if isinstance(z, int):
            z = float(z)
        if not isinstance(x, float) or not isinstance(y, float) or not isinstance(z, float):
            raise TypeError("x and y should be of type float.")
        self._x += x
        self._y += y
        self._z += z

    def is_inside(self, x: float, y: float, z: float) -> bool:
        """
            Returns True if x and y is greater than self._x and self._y
            and x and y are less than width and height.
            otherwise returns False
        """
        if not (self._x - (self._length / 2)) < x or not (self._x + (self._length / 2)) > x:
            return False
        if not (self._y - (self._height / 2)) < y or not (self._y + (self._height / 2)) > y:
            return False
        if not (self._z - (self._depth / 2)) < z or not (self._z + (self._depth / 2)) > z:
            return False
        return True

    # Draw the cube on plot

    def draw(self) -> None:
        """
            Draws the cube on plot.

            source: https://www.oraask.com/wiki/how-to-draw-3d-cube-using-matplotlib
        """
        sides = np.array(
            [int(self._length), int(self._height), int(self._depth)])
        data = np.ones(sides)
        fig = plt.figure(figsize=(9, 9))
        ax = fig.add_subplot(111, projection='3d')
        ax.voxels(data, facecolors="red")
        plt.title(
            f"Cube with dimension: {self._length}, {self._height} and {self._depth}")
        plt.show()
