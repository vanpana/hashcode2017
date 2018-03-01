from operator import itemgetter

import main


def total_possible_car_trip(car, ride):
    return car.position.distance_to(ride.start) + ride.total_distance()


def get_ride_points(car, ride, time, bonus):
    current_bonus = 0
    cost = 0
    cost = cost + car.position.distance_to(ride.start)
    points = ride.total_distance()
    if cost + time < ride.earliest_start:
        current_bonus += bonus
        cost += ride.earliest_start - (time + cost)
    if cost + time > ride.latest_finish:
        return 0
    cost += points
    if cost + time == ride.earliest_start:
        current_bonus += bonus
    points += current_bonus
    return points, cost


def sort_by_points(car_ride_points):
    return sorted(car_ride_points, key=itemgetter(2), reverse=True)


# def filter_start(car_list, ride_list):
#     possible_rides = []
#     if len(ride_list) == 0:
#         return []
#     for car in car_list:
#         for ride in ride_list:
#             if ride.earliest_start + total_possible_car_trip(car, ride) <= ride.latest_finish and ride not in possible_rides:
#                 possible_rides.append(ride)
#     return possible_rides


def filter_possible(car_list, ride_list):
    possible_rides = []
    if len(ride_list) == 0:
        return []
    for car in car_list:
        for ride in ride_list:
            if not car.is_occupied and ride.earliest_start + total_possible_car_trip(car, ride) <= ride.latest_finish:
                points, cost = get_ride_points(car, ride, main.time, main.bonus)
                if(points!=0):
                    possible_rides.append([car, ride, points/cost])
    return sort_by_points(possible_rides)

