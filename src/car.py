from point import Point


class Car:
    def __init__(self, id):
        self.id = id
        self.__position = Point(0, 0)
        self.__is_occupied = False
        self.__ride_list = []
        self.__steps_left = 0

    @property
    def position(self):
        return self.__position

    def set_position(self, row, col):
        self.__position = Point(row, col)
        return self

    def set_occupied(self, occupied):
        self.__is_occupied = occupied
        return self

    @property
    def is_occupied(self):
        return self.__is_occupied

    @property
    def steps_left(self):
        return self.__steps_left

    @property
    def get_rides(self):
        return self.__ride_list

    def add_ride(self, ride):
        self.__ride_list.append(ride)
        self.__steps_left = ride.total_distance()
        self.__position = ride.finish
        self.__is_occupied = True

    def step(self):
        if self.__steps_left > 0:
            self.__steps_left -= 1

            if self.__steps_left == 0:
                self.__is_occupied = False

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Car: id = {4}, position = {0}, occupied = {1}, ride_list = {2}, steps_left = {3}"\
            .format(self.position, self.__is_occupied, self.__ride_list, self.__steps_left, self.id)
