from station import Station
from loader import file_loader
import random
import plot
import pandas as pd
import score
import matplotlib.pyplot as plt

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
        self.train_route = []
        self.train_data = {}

        # init train classes equal to number of routes
        for i in range(1, routes + 1):
            self.trains.append(Train(i, max_time))


    def pick_first_stop(self):
        # keeps track of which train is currently picking a route
        self.train = self.trains[self.train_counter]

        # goes through all possible stations and finds ones with 1 connection and uses those and first stations
        for stations in self.stations:
            while len(stations.connections) == 1:
                self.train.first_stop = stations
                self.train.stops.append(self.train.first_stop)
<<<<<<< HEAD
=======
                self.train.first_stop.set_visited()
>>>>>>> d934e0f (new)
                return self.train.first_stop

        # when all 1 connection are used, a random station is picked as first station
        self.train.first_stop = random.choice(self.stations)
        self.train.stops.append(self.train.first_stop)
<<<<<<< HEAD
        return self.train.first_stop
    
    def route(self):
        # --------- pseudocode --------- #
        # train picks a first station
        # route is calculated from first station, using next station with shortest route
        # if at least 100 minutes is not reached, go to the last station visited and pick second shortest connection
        # if time still not reached, try all connections
        # if no connection adds up to at least 100 minutes, go back to the second last station visited and go back to step 2
        self.current_station = self.pick_first_stop()

        print(f"First station: {self.current_station.name}")

        while self.train.time_travelled <= 120:


            self.next_station = self.current_station.pick_shortest_connection(self.current_station)

                # should be code here that would switch to second shortest connection, cause otherwise you get infinite loop

            print(self.next_station.name)
=======
        self.train.first_stop.set_visited()
                

    def route(self):

        while self.train_counter < self.routes:
            # print(self.train_counter)
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
                        self.train_data[self.train.name] = self.train_route
                        break
                        
                else:
                    connection_counter = 0
                    for connection in self.train.first_stop.connections:
                        if connection.visited == True:
                            connection_counter += 1

                    if connection_counter == len(self.train.first_stop.connections):
                        self.train_data[self.train.name] = self.train_route
                        break
                
                self.train_route.append(self.train.next_stop.name)

                
            for stops in self.train.stops:
                print(self.train.name, ":", stops.name)
            self.train_route = []
            self.train_counter += 1
        for station in self.stations:
            if station.visited == False:
                print()
                print(station.name, end=" ")
                print(station.visited)
        print()
        
        # once number of required trains is reached, print + plot results and calculate score
        final_score = score.calculate_score(self.trains, self.stations)
        score.print_results(final_score, self.train_data)
        self.plot()
        
    def add_travel_time(self):
        self.train.time_travelled += self.train.first_stop.distances[self.train.next_stop]
        # print(self.train.time_travelled)
    
    def plot(self):
        df = plot.make_dataframe(self.train_data)
        coords_df = plot.load_coordinates()

        merged_plot = pd.merge(df, coords_df, on="stations").sort_values("train").reset_index()
        del merged_plot["index"]
>>>>>>> d934e0f (new)

            if self.no_useable_connections():
                break

            if self.connection_already_used():
                continue

            distance = self.current_station.get_travel_time(self.next_station)
            self.add_travel_time(distance)
            self.train.stops.append(self.next_station)
            self.use_connections(self.current_station, self.next_station)

            self.current_station = self.next_station
    

    def add_travel_time(self, distance):
        self.train.time_travelled += distance
    
    def use_connections(self, station1, station2):
        station1.used_connections.append(station2)
        station2.used_connections.append(station1)
    
    def connection_already_used(self):
        if self.current_station in self.next_station.used_connections and self.next_station in self.current_station.used_connections:
            return True
        
        return False
    
    def no_useable_connections(self):
        fail_counter = 0
        for station in self.current_station.connections:
            if self.current_station in station.used_connections:
                fail_counter += 1
        
        if fail_counter == len(self.current_station.connections):
            return True

        return False


if __name__ == "__main__":
    route1 = Route(7, 120)
    route1.route()
