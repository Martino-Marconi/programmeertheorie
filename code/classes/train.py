# from code.classes import station
from code.classes.loader import file_loader
from code.visualisation import plot

import random
import pandas as pd
import code.score.score as score
from collections import defaultdict

class Route:
    def __init__(self, routes, max_time):
        self.trains = []
        self.routes = routes
        self.max_time = max_time
        self.train_counter = 1
        self.stations = file_loader()
        self.train_data = {}
        self.all_stops = []
        self.stations_visited = 0
        self.list_scores = []

    def add_trains(self, i):
        self.trains.append(Train(i, self.max_time))

    def get_train_data(self):

        for train in self.trains:
            station_list = []
            for station in train.stops:
                station_list.append(station.name)

            self.train_data[train.name] = station_list

    def plot(self):
        self.get_train_data()
        df = plot.make_dataframe(self.train_data)
        coords_df = plot.load_coordinates()

        merged_plot = pd.merge(df, coords_df, on="stations")

        plot.map_plot(merged_plot, self.train_counter)

    def all_stations_visited(self,stations):
        
        visit_true = 0
        visit_false = 0

        for station in stations:
            if station.visited == True:
                visit_true += 1
            else:
                visit_false += 1

        self.stations_visited = visit_true / (visit_false + visit_true)

        if self.stations_visited >= 0.8:
            return True
        return False

    def improve_route(self):
            unused_stations = []

            for station in self.stations:
                if station.visited == False:
                    unused_stations.append(station)

            # improve routes of trains until they're around 180 minutes, giving priority to unused stops
            for train in self.trains:
                self.improve_route_subfunction(train, unused_stations)
            
            unused_stations = []

            for station in self.stations:
                if station.visited == False:
                    unused_stations.append(station)
            
            # make new trains and routes starting from stations that have not been visited yet
            while len(unused_stations) != 0:
                train_number = self.trains[-1].train_number + 1
                train = Train(train_number, 180)
                self.trains.append(train)
                train.stops.append(unused_stations[0])
                unused_stations.pop(0)
                self.improve_route_subfunction(train, unused_stations)
            # print(unused_stations)
        

    def improve_route_subfunction(self, train, unused_stations):
        second_fail_counter = 0

        while train.time_travelled < self.max_time:
            # pick current and next stop
            current_stop = train.stops[-1]

            next_stop = random.choice(list(train.stops[-1].connections.keys()))
            for station in unused_stations:
                if station in current_stop.connections:
                    next_stop = station
                    break
            
            # break if all possible connections have been visited already
            if next_stop in train.stops:
                stop_counter = 0
                for station in current_stop.connections:
                    if station in train.stops:
                        stop_counter += 1
                    
                    elif station not in train.stops:
                        next_stop = station
                    
                if stop_counter == len(current_stop.connections):
                    break

            # add station to train.stops if travel time allows it
            distance = current_stop.get_travel_time(next_stop)
            if train.time_travelled + distance < self.max_time:
                train.stops.append(next_stop)
                train.time_travelled += distance
                next_stop.set_visited()
                current_stop = next_stop
            else:
                break

            second_fail_counter += 1
            if second_fail_counter == 20:
                second_fail_counter = 0
                break
    
class Train:
    def __init__(self, train_number, max_time):
        # self.name = f"train_{self.train_number}"
        self.train_number = train_number
        self.name = f"train_{self.train_number}"
        self.max_time = max_time
        self.time_travelled = 0
        self.first_station = " "
        self.current_station = " "
        self.next_station = " "
        self.stops = []
        self.train_route = self.stops
        
    def no_useable_connections(self):
        fail_counter = 0
        for station in self.current_station.connections:
            if self.current_station in station.used_connections:
                fail_counter += 1
        
        if fail_counter == len(self.current_station.connections):
            return True

        return False

    def connection_already_used(self):
            if self.current_station in self.next_station.used_connections and self.next_station in self.current_station.used_connections:
                return True
            
            return False
    
    def add_travel_time(self, distance):

        self.time_travelled += distance

    def use_connections(self, station1, station2):
        station1.used_connections.append(station2)
        station2.used_connections.append(station1)

   

    