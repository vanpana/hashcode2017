from ride import Ride


def read_from_file(filename):
    """

    :rtype:
    R - number of rows in grid
    C – number of columns of the grid
    F – number of vehicles in the fleet
    N – number of rides
    B – per-ride bonus for starting the ride on time
    T – number of steps in the simulation
    Rides - list of rides
    """
    with open(filename, "r") as file:
        counter = 0
        constants = []
        rides = []
        for line in file:
            line = line.strip("\n")
            
            if counter == 0:
                constants = line.split(" ")
            else:
                ride_raw = line.split(" ")
                rides.append(Ride(counter - 1, *ride_raw))

            counter += 1

        return constants, rides
