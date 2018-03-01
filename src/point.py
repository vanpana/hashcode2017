class Point:
    def __init__(self, row, col):
        self.__row = row
        self.__col = col

    @property
    def row(self):
        return self.__row

    @property
    def col(self):
        return self.__col

    def distance_to(self, other):
        return abs(self.__row - other.row) + abs(self.col - other.col)

    def __str__(self):
        return "({0}, {1})".format(self.__row, self.__col)
