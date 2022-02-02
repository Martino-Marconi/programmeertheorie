from code.classes.station import Station

import csv


def file_loader():
    """
    Load data from csv files and make station classes
    based on that data.
    """
    stations = []

    # get station names and coordinates from csv
    with open("input/StationsNationaal.csv") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            # creates station classes
            station = Station(row[0], row[1], row[2])
            stations.append(station)

    # get station connections from csv
    with open("input/ConnectiesNationaal.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            for station in stations:
                for connection in stations:
                    # add connections to station objects that match names in csv file
                    if row[0] == station.name:
                        if row[1] == connection.name:
                            station.add_connection(connection, float(row[2]))

                    if row[1] == station.name:
                        if row[0] == connection.name:
                            station.add_connection(connection, float(row[2]))

    return stations
