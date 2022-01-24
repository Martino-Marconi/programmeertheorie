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
        # --------- pseudocode --------- #
        # train picks the station with the shortest route
        # if shortest route is travelled, pick second shortest.
        # continue proces untill the train has the shortest route that is available
        # return the station from where it starts
        
        # keeps track of which train is currently picking a route
        self.train = self.trains[self.train_counter]
        
        empty_dataframe = pd.DataFrame()

        for stations in self.stations:
            new_station = {'station1' : stations, 'station2': stations.connections.keys(), 'time': stations.connections.values()}
            connections_df = pd.DataFrame.from_dict(new_station)
            empty_dataframe = empty_dataframe.append(connections_df, ignore_index=True)
        empty_dataframe = empty_dataframe.sort_values(by="time", ascending=True)
        # print(empty_dataframe)
        print()
        count = 0
        for index, row in empty_dataframe.iterrows():
            row_route = empty_dataframe.iloc[count]
            count += 1
            if row_route.station1 not in self.train.stops or row_route.station2 not in self.train.stops:
                print(self.train.stops)
                self.train.stops.append(row_route.station1)
                self.train.stops.append(row_route.station2)


                print(f"{row_route.station1.name} <> {row_route.station2.name} <> {row_route.time}")

                return row_route.station1
            continue

        # # when all connections are used, a random station is picked as first station
        # self.train.first_stop = random.choice(self.stations)
        # self.train.stops.append(self.train.first_stop)
        # print("d")
        # return self.train.first_stop













    def route(self):
        # --------- pseudocode --------- #
        # train picks a first station
        # route is calculated from first station, using next station with shortest route
        # if at least 100 minutes is not reached, go to the last station visited and pick second shortest connection
        # if time still not reached, try all connections
        # if no connection adds up to at least 100 minutes, go back to the second last station visited and go back to step 2
        
        while self.train_counter < self.routes:
        
            self.current_station = self.pick_first_stop()
            # print(f"First station: {self.current_station.name}")
            self.train_counter += 1
            print(self.train.stops)

        
        
        
        # while self.train.time_travelled <= 120:

        #     self.next_station = self.current_station.pick_shortest_connection(self.current_station)

        #         # should be code here that would switch to second shortest connection, cause otherwise you get infinite loop

        #     # print(self.next_station.name)

        #     if self.no_useable_connections():
        #         break

        #     if self.connection_already_used():
        #         continue

        #     distance = self.current_station.get_travel_time(self.next_station)
        #     self.add_travel_time(distance)
        #     self.train.stops.append(self.next_station)
        #     self.use_connections(self.current_station, self.next_station)

        #     self.current_station = self.next_station
    

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
