
from station import Station
from loader import file_loader
import random


class Train:
    def __init__(self, train_number, max_time):
        self.train_number = train_number
        self.time_travelled = 0
        self.stops = []
        self.max_time = max_time

class Route:
    def __init__(self, routes, max_time):
        self.stations = file_loader()
        self.trains = []

        # init train classes equal to number of routes
        for i in range(1, routes + 1):
            self.trains.append(Train(i, max_time))

    def pick_first_stop(self):
        self.train = self.trains[0]
        self.first_stop = random.choice(self.stations)
        print(self.first_stop.name)

    def route(self):
        next_stop = random.choice(self.first_stop.connections)
        self.add_travel_time(self.first_stop, next_stop)
        print(next_stop.name)
    
    def add_travel_time(self, first_stop, next_stop):
        pass
        
        


if __name__ == "__main__":
    route1 = Route(7, 120)
    route1.pick_first_stop()
    route1.route()
