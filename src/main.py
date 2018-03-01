import Constants
import filters
from car import Car
from read_from_file import read_from_file

bonus = 0
time = 0
no_of_cars = 0

def get_free_cars(cars):
    free_cars = []
    for car in cars:
        if not car.is_occupied:
            free_cars.append(car)
    return free_cars


if __name__ == '__main__':
    constants, rides = read_from_file("data/e.in")
    write_file = "out/e2.out"
    no_of_cars, bonus, time = int(constants[2]), int(constants[4]), int(constants[5])
    cars = []
    for car in range(0, no_of_cars):
        cars.append(Car(car))

    assigned = []

    # print(len(rides))
    # rides = filters.filter_start(cars, rides)
    print(len(rides))

    entered = False
    while time:
        ctr = 0

        print(time)
        for car in cars:
            car.step()
            if not car.is_occupied:
                ctr += 1

        if ctr == len(cars) and entered:
            break

        entered = True

        sorted_rides = filters.filter_possible(get_free_cars(cars), rides)

        if len(rides) > 0:
            for car, ride, points in sorted_rides:
                if not car.is_occupied and ride.id not in assigned:
                    ctr -= 1
                    car.add_ride(ride)
                    assigned.append(ride.id)

                    for index in range(0, len(rides) + 1):
                        if rides[index].id == ride.id:
                            del rides[index]
                            break
                    print("Car {0}" " -> Ride {1}".format(car.id, ride.id))
            time -= 1
        else:
            time = 0

    with open(write_file, "w") as file:

        for car in cars:
            file.write("{0} ".format(len(car.get_rides)))
            for ride in car.get_rides:
                file.write("{0} ".format(ride.id))
            file.write("\n")


