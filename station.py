
class Station:
    def __init__(self, name, x_coord, y_coord):
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord

        self.connections = {}


    def add_connection(self, next_station, distance):

        self.connections[next_station] = int(distance)
    
    def get_connections(self):
        return self.connections
        

