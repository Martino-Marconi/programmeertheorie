from code.classes.loader import file_loader
from code.classes import plot

import random
import pandas as pd


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
        """
        Add trains to route class.
        """
        self.trains.append(Train(i, self.max_time))

    def get_train_data(self):
        """
        Return dictionary of train names and all
        stops they have visited.
        """
        for train in self.trains:
            station_list = []
            for station in train.stops:
                station_list.append(station.name)

            self.train_data[train.name] = station_list

        return self.train_data

    def plot(self, train_data):
        """
        Plot train data onto map of the Netherlands.
        """
        df = plot.make_dataframe(train_data)
        coords_df = plot.load_coordinates()

        merged_plot = pd.merge(df, coords_df, on="stations")

        plot.map_plot(merged_plot)

    def all_stations_visited(self, stations):
        """
        Check if all possible stations have been visited.
        """
        visit_true = 0
        visit_false = 0

        for station in stations:
            if station.visited > 0:
                visit_true += 1
            else:
                visit_false += 1

        self.stations_visited = visit_true / (visit_false + visit_true)

        if self.stations_visited >= 0.8:
            return True
        return False

    def improve_train_length(self):
        """
        Adds stations to trains that have not travelled for 180 minutes yet.
        This function does not check if a station has not been visited
        before.
        """
        unused_stations = []

        for station in self.stations:
            if station.visited is False:
                unused_stations.append(station)

        # improve routes of trains until they're around 180 minutes, giving priority to unused stops
        for train in self.trains:
            self.improve_route_subfunction(train, unused_stations)

    def improve_route_subfunction(self, train, unused_stations):
        """
        This function adds stations to existing trains if this
        is possible.
        """

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

    def improve_last_stop(self):
        """
        Go back to a train's second-to-last stop
        and pick a new last stop based on its connections, to see
        if a train can go further.
        """
        train = random.choice(self.trains)
        unused_stations = []
        while len(train.stops) != 1:
            current_last_stop = train.stops[-1]
            train.stops.pop()

            # pick a new next stop
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

        # improve trains if a train only has one stop left
        if len(train.stops) == 1:
            self.improve_trains()

        self.improve_route_subfunction(train, unused_stations)

    def improve_route_new_trains(self):
        """
        If there are stations that have not been visited before after all
        trains have stopped, make new trains with those stations as starting
        points.
        """
        unused_stations = []

        for station in self.stations:
            if station.visited is False:
                unused_stations.append(station)

        # make new trains and routes starting from stations that have not been visited yet
        while len(unused_stations) != 0 and len(self.trains) <= 20:
            train_number = self.trains[-1].train_number + 1
            train = Train(train_number, 180)
            self.trains.append(train)
            train.stops.append(unused_stations[0])
            unused_stations[0].visited += 1
            unused_stations.pop(0)
            self.improve_route_subfunction(train, unused_stations)

    def improve_trains(self):
        """
        Removes trains that only go to one station, and adds trains
        for each station that has not been visited before.
        """
        self.improve_route_new_trains()
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

    def improve_trains_superfluous(self):
        """
        Removes trains that go to stops that are all already visited
        by other trains.
        """
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
        """
        Break from route function if all connections have already been
        visited by a train, meaning it can't continue.
        """
        fail_counter = 0
        for station in self.current_station.connections:
            if self.current_station in station.used_connections:
                fail_counter += 1

        if fail_counter == len(self.current_station.connections):
            return True

        return False

    def connection_already_used(self):
        """
        Check if a connection between two stations has already been used.
        """
        if self.current_station in self.next_station.used_connections:
            if self.next_station in self.current_station.used_connections:
                return True

        return False

    def add_travel_time(self, distance):
        """
        Add distance between two stations to a train's travel time.
        """
        self.time_travelled += distance

    def use_connections(self, station1, station2):
        """
        Add two stations to each other's used connections, meaning
        the connection between them has been used.
        """
        station1.used_connections.append(station2)
        station2.used_connections.append(station1)
