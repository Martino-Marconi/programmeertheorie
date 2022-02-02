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
        Add connection to station class.
        """
        self.connections[connected_station] = distance

    def pick_shortest_connection(self, current_station):
        """
        Pick the closest connection based on travel time out
        of all possible station connections.
        """
        distance_counter = 10000
        next_station = None
        stations = current_station.connections

        for station in stations:
            if int(stations[station]) < distance_counter:
                if station not in current_station.used_connections and current_station not in station.used_connections:
                    distance_counter = stations[station]
                    next_station = station
        return next_station

    def get_travel_time(self, connection):
        """
        Return travel time
        """
        time = self.connections[connection]
        return time

    def set_visited(self):
        """
        Add 1 every time a station is visited by a train.
        """
        self.visited += 1
