import math


class Geometri:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        if isinstance(value, int):
            value = float(value)
        if not isinstance(value, float):
            raise TypeError("x must be float.")
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        if isinstance(value, int):
            value = float(value)
        if not isinstance(value, float):
            raise TypeError("y must be float.")
        self._y = value

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def draw(self) -> None:
        plt.plot(self.x, self.y, "ro")
        plt.show()

    def translate(self, x: float, y: float) -> None:
        if self.is_type_float(x, y):
            self.x += x
            self.y += y
        self.x += x
        self.y += y

    def is_type_float(*args):
        for arg in args:
            if not isinstance(arg, float):
                return False
        return True

    def int_to_float(*args):
        for arg in args:
            if isinstance(arg, int):
                arg = float(arg)
        return args
