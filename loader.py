
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
                # adds connections to stations
                if row[0] == station.name:
                    station.add_connection(row[1], row[2])
                if row[1] == station.name:
                    station.add_connection(row[0], row[2])
    
    return stations


if __name__ == "__main__":
    file_loader()
