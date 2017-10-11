class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.adjacency_index = self.calc_index()

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def calc_index(self):
        return self.x + (15 * self.y)

    def all_adjacents(self):
        coords = []
        coords.append(Coordinate(self.x - 1, self.y - 1)) # BLD
        coords.append(Coordinate(self.x - 1, self.y)) # L
        coords.append(Coordinate(self.x - 1, self.y + 1)) # ULD
        coords.append(Coordinate(self.x, self.y + 1)) # U
        coords.append(Coordinate(self.x + 1, self.y + 1)) # URD
        coords.append(Coordinate(self.x + 1, self.y)) # R
        coords.append(Coordinate(self.x + 1, self.y - 1)) # BRD
        coords.append(Coordinate(self.x, self.y - 1)) # B
        return coords

    # Copies coordinate and sets the X value
    # Of the copy to value
    def copy_with_new_x(self, value):
        return Coordinate(value, self.y)

    # Copies coordinate and sets the Y value
    # Of the copy to value
    def copy_with_new_y(self, value):
        return Coordinate(self.x, value)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if self.y != other.y:
            return self.y < other.y
        else:
            return self.x < other.x
    def __hash__(self):
        return self.x * 13 + self.y * 31
