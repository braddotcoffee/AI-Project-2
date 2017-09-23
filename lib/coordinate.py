class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    # --- Allows overwriting default getter and setter --- #
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        if value < 0 or value > 15:
            raise ValueError("X Value Outside Range Of Board")
        self._x = value

    # --- Allows overwriting default getter and setter --- #
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        if value < 0 or value > 15:
            raise ValueError("Y Value Outside Range Of Board")
        self._y = value

    # Copies coordinate and sets the X value
    # Of the copy to value
    def copy_with_new_x(self, value):
        return Coordinate(value, self.y)

    # Copies coordinate and sets the Y value
    # Of the copy to value
    def copy_with_new_y(self, value):
        return Coordinate(self.x, y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if self.y != other.y:
            return self.y < other.y
        else:
            return self.x < other.x
    def __hash__(self):
        return self._x * 13 + self._y * 31
