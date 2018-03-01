from point import Point


class Ride:
    def __init__(self, id, row_start, column_start, row_finish, column_finish, earliest_start, latest_finish):
        self.id = id
        self.__position_start = Point(int(row_start), int(column_start))
        self.__position_finish = Point(int(row_finish), int(column_finish))
        self.__earlist_start = int(earliest_start)
        self.__latest_finish = int(latest_finish)

    @property
    def start(self):
        return self.__position_start

    @property
    def finish(self):
        return self.__position_finish

    @property
    def earliest_start(self):
        return self.__earlist_start

    @property
    def latest_finish(self):
        return self.__latest_finish

    def total_distance(self):
        return self.__position_start.distance_to(self.__position_finish)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Ride: ID: {4}, PS: {0}, PS: {1}, ES: {2}, LF: {3}"\
              .format(self.__position_start, self.__position_finish,
                      self.__earlist_start, self.__latest_finish, self.id)
