
class Station:
    def __init__(self, name, x_coord, y_coord):
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord

        self.visited = False

        self.connections = []
        self.distances = {}

    def add_connection(self, next_station):
        self.connections.append(next_station)

    def add_distance(self, next_station, distance):

        self.distances[next_station] = float(distance)
    
    def get_connections(self):
        return self.connections

    def set_visited(self):
        self.visited = True
