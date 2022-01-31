import random


class Station:
    def __init__(self, name, x_coord, y_coord):
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord

        self.connections = {}
        self.used_connections = []
        self.visited = 0

    def add_connection(self, connected_station, distance):
        """
        Adds connected stations with distance to self.connections dict
        """

        self.connections[connected_station] = distance

    def pick_shortest_connection(self, current_station):
        """
        Picks shortest possible connection out of connected stations
        """

        distance_counter = 10000
        next_station = None
        stations = current_station.connections
        possible_stations = []

        for station in stations:
            possible_stations.append(station)
            if int(stations[station]) < distance_counter:
                if station not in current_station.used_connections and current_station not in station.used_connections:
                    distance_counter = stations[station]
                    next_station = station

        if next_station is None:
            next_station = random.choice(possible_stations)

        return next_station

    def get_travel_time(self, connection):
        """
        Returns the distance to a connection
        """
        return self.connections[connection]

    def set_visited(self):
        """
        Set visited to True if a station has been visited already
        """
        self.visited += 1
