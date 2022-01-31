from tempfile import tempdir
from code.classes.train import Train
from code.classes.train import Route
from code.classes.station import Station as st
import code.score.score as score

import random

def pick_first_stop(stations, stops):
    """
    Pick the first stop for each train. Semi-random algorithm, 
    because it is not possible to start at a station that is 
    already visited.
    """
    while True:
        
        first_stop = random.choice(stations)

        if first_stop not in stops:
            break
        continue

    return first_stop

def pick_random_connection(current_station, stops):
    """
    Pick random connection for current station. Try to get a connection
    that has not been visited before. Return the next station.
    """

    empty_list = []
    for stations in current_station.connections:
        empty_list.append(stations)

    
    for i in range(100):
        next_station = random.choice(empty_list)
        
        if next_station not in stops:
            break

    return next_station

def run(routes, max_time):
    """
    Randomly assign each station with one of the possible connections.
    """
    
    # import Train class as object called 'tr'
    tr = Train(routes, max_time)
    ro = Route(routes, max_time)
    

    # loop through all trains
    while ro.train_counter <= routes:
        ro.add_trains(ro.train_counter)
        train = ro.trains[(ro.train_counter - 1)]
        
        # pick random first stop 
        tr.current_station = pick_first_stop(ro.stations, ro.all_stops)
        tr.current_station.set_visited()
        train.stops.append(tr.current_station)
        ro.all_stops.append(tr.current_station)
        
        temp_stops = []

        # keep adding stations to list as long as train doesnt reach it's max time        
        while tr.time_travelled <= max_time:
            tr.next_station =  tr.current_station.pick_shortest_connection(tr.current_station)
            if tr.next_station == None:
                break

            distance = tr.current_station.get_travel_time(tr.next_station)

            # stop adding next stops if next stop will overwrite the maximum time
            if (distance + tr.time_travelled) > max_time:
                break

            if tr.next_station == None:
                break

            if tr.no_useable_connections():
                break

            if len(ro.all_stops) == 62:
                break

            tr.add_travel_time(distance)
            temp_stops.append(tr.next_station)





            # train.stops.append(tr.next_station)
            # tr.next_station.set_visited()
            tr.use_connections(tr.current_station, tr.next_station)
            # ro.all_stops.append(tr.current_station)
            tr.current_station = tr.next_station
        
        if tr.time_travelled < 80:
            for stops in temp_stops:
                train.stops.append(stops)
                stops.set_visited()
                ro.all_stops.append(stops)
                
            continue

        print(ro.train_counter, tr.time_travelled)
        tr.time_travelled = 0
        ro.train_counter += 1
        
        if ro.all_stations_visited(ro.stations):
            break
        

    
    # once number of required trains is reached, print + plot results and calculate score
    final_score = score.calculate_score(ro.trains, ro.stations)
    ro.get_train_data()
    ro.plot()
    score.print_results(final_score, ro.train_data)

    




        


