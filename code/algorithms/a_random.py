from code.classes.train import Train
from code.classes.train import Route

import code.score.score as score

import copy
import random

def pick_first_stop(stations):
    """
    Pick the first stop for each train.
    """
    
    first_stop = random.choice(stations)
    
    return first_stop

def pick_random_connection(current_station):
    """
    Pick random connection for current station. Return the next station.
    """

    empty_list = []
    for stations in current_station.connections:
        empty_list.append(stations)

    next_station = random.choice(empty_list)

    return next_station


def run(routes, max_time, random, random_whc, hill_climber):
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
        tr.current_station = pick_first_stop(ro.stations)
        tr.current_station.set_visited()
        train.stops.append(tr.current_station)

        # keep adding stations to list as long as train doesnt reach it's max time        
        while tr.time_travelled <= max_time:
            

            tr.next_station = pick_random_connection(tr.current_station)

            distance = tr.current_station.get_travel_time(tr.next_station)

            # stop adding next stops if next stop will overwrite the maximum time
            if (distance + tr.time_travelled) > max_time:
                break

            tr.add_travel_time(distance)
            train.stops.append(tr.next_station)
            tr.next_station.set_visited()
            tr.use_connections(tr.current_station, tr.next_station)

            tr.current_station = tr.next_station

        tr.time_travelled = 0
        ro.train_counter += 1

    
    
    # once number of required trains is reached, print + plot results and calculate score
    final_score = score.calculate_score(ro.trains, ro.stations)
    ro.get_train_data()

    random.append_score(final_score)
    higher = random.check_if_highest(final_score)
    if higher == True:
        ro.plot(ro.train_data)
        score.print_results(final_score, ro.train_data, "code/score/output_random.csv")


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
        ro.get_train_data()

        random_whc.append_score(final_score)
        higher = random_whc.check_if_highest(final_score)
        
        if higher == True:
            ro.plot(ro.train_data)
            score.print_results(final_score, ro.train_data, "code/score/output_random_whc.csv")





    




        


