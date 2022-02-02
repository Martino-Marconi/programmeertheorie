from code.classes.train import Train
from code.classes.train import Route
import code.score.score as score

import copy
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

def run(routes, max_time, semi_random, semi_random_whc, hill_climber):
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

        # keep adding stations to list as long as train doesnt reach it's max time        
        while tr.time_travelled <= max_time:
            
            tr.next_station = pick_random_connection(tr.current_station, ro.all_stops)

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
            train.stops.append(tr.next_station)

            tr.next_station.set_visited()
            tr.use_connections(tr.current_station, tr.next_station)
            ro.all_stops.append(tr.current_station)
            tr.current_station = tr.next_station

        tr.time_travelled = 0
        ro.train_counter += 1
        
        if ro.all_stations_visited(ro.stations):
            break
        

    
    # once number of required trains is reached, print + plot results and calculate score
    final_score = score.calculate_score(ro.trains, ro.stations)
    train_data = ro.get_train_data()

    semi_random.append_score(final_score)
    if_higher = semi_random.check_if_highest(final_score)
    
    if if_higher:
        ro.plot(train_data)
        score.print_results(final_score, ro.train_data, "code/score/output_semi_random.csv")
        print(f"normal score: {final_score}")


    # # ----------- HILL CLIMBER ------------------
    if hill_climber == True: 
        tmp_data = copy.deepcopy(ro.train_data)
        tmp_trains = copy.deepcopy(ro.trains)
        tmp_stations = copy.deepcopy(ro.stations)
        ro.improve_route()


        for i in range(100):
            ro.improve_route_2()
            new_score = score.calculate_score(ro.trains, ro.stations)
            if new_score < final_score:
                ro.train_data = tmp_data
                ro.trains = tmp_trains
                ro.stations = tmp_stations
            else:
                tmp_data = copy.deepcopy(ro.train_data)
                tmp_trains = copy.deepcopy(ro.trains)
                tmp_stations = copy.deepcopy(ro.stations)
                final_score = new_score
        
        ro.improve_trains_2()
        train_data = ro.get_train_data()

        semi_random_whc.append_score(final_score)
        higher = semi_random_whc.check_if_highest(final_score)

        if higher:
            ro.plot(train_data)
            score.print_results(final_score, ro.train_data, "code/score/output_semi_random_whc.csv")
            print(f"hill c. score: {final_score}")
            print()


    




        


