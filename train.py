from station import Station
from loader import file_loader
import random
import plot
import pandas as pd
import score
import matplotlib.pyplot as plt
import copy


class Train:
    def __init__(self, train_number, max_time):
        self.train_number = train_number
        self.time_travelled = 0
        self.stops = []
        self.max_time = max_time
        self.first_stop = " "
        self.next_stop = " "
        self.name = f"train_{self.train_number}"
        self.connections = []


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
        self.train = self.trains[self.train_counter]

        # for stations in self.stations:
        #     while len(stations.connections) == 1 and stations.visited == False:
        #         self.train.first_stop = stations
        #         self.train.stops.append(self.train.first_stop)
        #         self.train_route.append(self.train.first_stop.name)
        #         self.train.first_stop.set_visited()
        #         return self.train.first_stop
        self.train.first_stop = random.choice(self.stations)
        self.train.stops.append(self.train.first_stop)
        self.train_route.append(self.train.first_stop.name)
        return self.train.first_stop


    def route(self):

        while self.train_counter < self.routes:

            self.current_station = self.pick_first_stop()
            self.current_station.set_visited()

            # print(f"First station: {self.current_station.name}")

            fail_counter = 0
            while self.train.time_travelled <= 180:


                self.next_station = self.current_station.pick_shortest_connection(self.current_station)

                if self.next_station in self.train.stops:
                    fail_counter += 1

                    if fail_counter == 10:
                        break

                    continue

                if self.next_station == None:
                    break


                if self.no_useable_connections():
                    break

                if self.connection_already_used():
                    continue

                distance = self.current_station.get_travel_time(self.next_station)
                self.add_travel_time(distance)
                self.train.stops.append(self.next_station)
                self.next_station.set_visited()
                self.use_connections(self.current_station, self.next_station)

                self.current_station = self.next_station

            self.train_counter += 1

        self.improve_trains()
        # once number of required trains is reached, print + plot results and calculate score
        final_score = score.calculate_score(self.trains, self.stations)

        self.plot()
        score.print_results(final_score, self.train_data, "data/output.csv")
        tmp_data = copy.deepcopy(self.train_data)
        tmp_trains = copy.deepcopy(self.trains)
        tmp_stations = copy.deepcopy(self.stations)

        print(f"First score: {final_score}")
        self.improve_route()

        for i in range(100):
            self.improve_route_2()
            new_score = score.calculate_score(self.trains, self.stations)
            # print(f"Iteration {i}, Score: {new_score}")
            if new_score < final_score:
                self.train_data = tmp_data
                self.trains = tmp_trains
                self.stations = tmp_stations
                # print(f"Trains: {len(self.trains)}")
                # print("Not improved")
            else:
                tmp_data = copy.deepcopy(self.train_data)
                tmp_trains = copy.deepcopy(self.trains)
                tmp_stations = copy.deepcopy(self.stations)
                final_score = new_score
                # print(f"Trains: {len(self.trains)}")
                # print("Improved")
        
        self.improve_trains_2()
        
        self.get_train_data()

        print(f"Second score: {final_score}")

        self.plot()
        score.print_results(final_score, self.train_data, "data/output2.csv")
    
    def improve_route_2(self):
        train = random.choice(self.trains)
        unused_stations = []
        while len(train.stops) != 1:
            current_last_stop = train.stops[-1]
            train.stops.pop()

            next_stop = random.choice(list(train.stops[-1].connections.keys()))
            fail_counter = 0
            if next_stop != current_last_stop:
                train.stops.append(next_stop)
                next_stop.set_visited()
                distance = train.stops[-2].get_travel_time(next_stop)
                train.time_travelled += distance
                break
            while next_stop == current_last_stop:
                next_stop = random.choice(list(train.stops[-1].connections.keys()))
                fail_counter += 1
                if fail_counter == 10:
                    break

        if len(train.stops) == 1:
            self.improve_trains()

        self.improve_route_subfunction(train, unused_stations)
    
    def improve_trains_2(self):
        # remove trains that go to stops that have all already been visited
        trains_to_remove = []
        for train in self.trains:
            station_counter = 0
            for station in train.stops:
                if station.visited > 1:
                    station_counter += 1
                
                if station_counter == len(train.stops):
                    trains_to_remove.append(train)

        for train in trains_to_remove:
            if train in self.trains:
                for station in train.stops:
                    station.visited -= 1
                self.trains.remove(train)
                
                
    def improve_trains(self):
        self.improve_route_3()
        # Removes trains that only go to one station
        trains_to_remove = []

        # make list of trains to be removed
        for train in self.trains:
            if len(train.stops) == 1:
                trains_to_remove.append(train)
        
        # remove trains from route class
        for train in trains_to_remove:
            if train in self.trains:
                for station in train.stops:
                    station.visited -= 1
                self.trains.remove(train)
        
        # fix train numbers to make them consecutive again
        for i in range(1, len(self.trains)):
            self.trains[i].train_number = i
            self.trains[i].name = f"train_{i}"
    


    def improve_route(self):
        unused_stations = []

        for station in self.stations:
            if station.visited == False:
                unused_stations.append(station)

        # improve routes of trains until they're around 180 minutes, giving priority to unused stops
        for train in self.trains:
            self.improve_route_subfunction(train, unused_stations)
    
    def improve_route_3(self):
        unused_stations = []

        for station in self.stations:
            if station.visited == False:
                unused_stations.append(station)
        
        # make new trains and routes starting from stations that have not been visited yet
        while len(unused_stations) != 0 and len(self.trains) <= 20:
            train_number = self.trains[-1].train_number + 1
            train = Train(train_number, 180)
            self.trains.append(train)
            train.stops.append(unused_stations[0])
            unused_stations.pop(0)
            self.improve_route_subfunction(train, unused_stations)
    
    

    def improve_route_subfunction(self, train, unused_stations):
        second_fail_counter = 0

        while train.time_travelled < 180:
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
            if train.time_travelled + distance < 180:
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
    

    def plot(self):
        self.get_train_data()
        df = plot.make_dataframe(self.train_data)
        coords_df = plot.load_coordinates()

        merged_plot = pd.merge(df, coords_df, on="stations")

        plot.map_plot(merged_plot)


    def get_train_data(self):
        for train in self.trains:
            station_list = []
            for station in train.stops:
                station_list.append(station.name)

            self.train_data[train.name] = station_list


if __name__ == "__main__":

    route1 = Route(20, 180)

    route1.route()
