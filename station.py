class Station:
    def __init__(self, name, x_coord, y_coord):
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord

        self.connections = {}
        self.used_connections = []
    
    def add_connection(self, connected_station, distance):
        self.connections[connected_station] = distance
    
    def pick_shortest_connection(self, current_station):

        distance_counter = 10000
        next_station = ""
        stations = current_station.connections

        for station in stations:
            if int(stations[station]) < distance_counter:
                if station not in current_station.used_connections:
                    distance_counter = stations[station]
                    next_station = station

        return next_station
    
    def get_travel_time(self, connection):
        return self.connections[connection]
