import csv

from station import Station
from connection import Connection

def file_loader():

    stations = []

    with open("data/StationsNationaal.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            # creates stations from csv file
            station = Station(row[0], row[1], row[2])
            stations.append(station)

    with open("data/ConnectiesNationaal.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            for station in stations:
                for connection in stations:
                    if row[0] == station.name:
                        if row[1] == connection.name:
                            station.add_connection(connection, float(row[2]))
                    
                    if row[1] == station.name:
                        if row[0] == connection.name:
                            station.add_connection(connection, float(row[2]))

    return stations

if __name__ == "__main__":
    file_loader()
