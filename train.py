
from station import Station
from loader import file_loader
import random


class Train:
    def __init__(self, train_number, max_time):
        self.train_number = train_number
        self.time_travelled = 0
        self.stops = []
        self.max_time = max_time
        self.first_stop = " "
        self.next_stop = " "
        self.name = f"train_{self.train_number}"

class Route:
    def __init__(self, routes, max_time):
        self.stations = file_loader()
        self.trains = []
        self.routes = routes
        self.train_counter = 0

        # init train classes equal to number of routes
        for i in range(1, routes + 1):
            self.trains.append(Train(i, max_time))

    def pick_first_stop(self):
        self.train = self.trains[self.train_counter]
        self.train.first_stop = random.choice(self.stations)
        self.train.stops.append(self.train.first_stop)
        self.train.first_stop.set_visited()
        # print(self.train.first_stop.name)
        print(self.train.name)

    def route(self):

        while self.train_counter < self.routes:
            print(self.train_counter)
            self.pick_first_stop()

            while self.train.time_travelled <= 120:
                # pick next stop
                self.train.next_stop = random.choice(self.train.first_stop.connections)
                # if stop already visited, look for another one
                if self.train.next_stop not in self.train.stops:
                    self.train.next_stop.set_visited()
                    self.train.stops.append(self.train.next_stop)
                    # if statement makes sure time doesn't go over 120 minutes
                    if self.train.time_travelled + self.train.first_stop.distances[self.train.next_stop] <= 120:
                        # print(self.train.next_stop.name)
                        self.add_travel_time()
                        self.train.first_stop = self.train.next_stop
                    else:
                        break
                        
                else:
                    connection_counter = 0
                    for connection in self.train.first_stop.connections:
                        if connection.visited == True:
                            connection_counter += 1

                    if connection_counter == len(self.train.first_stop.connections):
                        break
            
            self.train_counter += 1
    
        for station in self.stations:
            print(station.name, end=" ")
            print(station.visited)
            print()


    def add_travel_time(self):
        self.train.time_travelled += self.train.first_stop.distances[self.train.next_stop]
        # print(self.train.time_travelled)



if __name__ == "__main__":
    route1 = Route(7, 120)
    route1.route()
