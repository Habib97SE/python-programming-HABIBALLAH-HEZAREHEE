import math


class Geometri:
    def __init__(self, x: float, y: float) -> None:
        """
            Initialize the geometri with x and y.
            Parameters:
                x: float - x coordinate middle of the geometri
                y: float - y coordinate middle of the geometri
            Returns:
                None : None
        """
        self.x = x
        self.y = y

    @property
    def x(self) -> float:
        """
            Returns the x coordinate of the geometri.
        """
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        """
            Sets the x coordinate of the geometri.
        """
        if isinstance(value, int):
            value = float(value)
        if not isinstance(value, float):
            raise TypeError("x must be float.")
        self._x = value

    @property
    def y(self) -> float:
        """
            Returns the y coordinate of the geometri.
        """
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        """
            Sets the y coordinate of the geometri.
        """
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
        """
            Draws the geometri.
        """
        plt.plot(self.x, self.y, "ro")
        plt.show()

    def translate(self, x: float, y: float) -> None:
        """
            Translates the geometri. 
            Parameters:
                x: float - x coordinate to translate the geometri
                y: float - y coordinate to translate the geometri
            Returns:
                None : None
        """
        if self.is_type_float(x, y):
            self.x += x
            self.y += y
        self.x += x
        self.y += y

    def is_type_float(*args) -> list:
        """
            Checks if the arguments are of type float.
            Parameters:
                *args: float - arguments to check
            Returns:
                bool : True if all arguments are of type float, otherwise False
        """
        for arg in args:
            if not isinstance(arg, float):
                return False
        return True

    def int_to_float(*args) -> list:
        """
            Converts all arguments of type int to type float.
            Parameters:
                *args: float - arguments to convert
            Returns:
                list : list of arguments of type float
        """
        for arg in args:
            if isinstance(arg, int):
                arg = float(arg)
        return args
