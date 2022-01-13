
import csv

from station import Station

def file_loader():

    stations = []


    with open("data/StationsHolland.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            # creates stations from csv file
            station = Station(row[0], row[1], row[2])
            stations.append(station)

    with open("data/ConnectiesHolland.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            for station in stations:
                for connection in stations:
                    if row[0] == station.name:
                        if row[1] == connection.name:
                            station.add_connection(connection)
                            station.add_distance(connection, row[2])
                    
                    if row[1] == station.name:
                        if row[0] == connection.name:
                            station.add_connection(connection)
                            station.add_distance(connection, row[2])
    

    # test print statements (TO BE REMOVED)
    for station in stations:
        print(station.name)
        for connection in station.connections:
            print(connection.name, end=", ")
        print()
        print(station.distances)


    return stations
