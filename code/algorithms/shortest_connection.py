from code.classes.train import Train, Route
from code.classes.train import Route
import code.score.score as score

import random



def pick_first_stop(stations, stops):
    """
    Pick the first stop for each train. Semi-random algorithm, 
    because it is not possible to start at a station that is 
    already visited.
    """
    
    # ----------- RANDOM FIRST STOP ---------------
    first_stop = pick_random_first_stop(stations, stops)

    return first_stop

    # # ----------- ONE CONNECTION ------------------
    # first_stop = ""
    # while True:

    #     first_stop = pick_random_first_stop(stations, stops)

    #     # for i in range(1, 5, 1):
    #     if len(first_stop.connections) == 1 and first_stop not in stops:
    #         first_stop = first_stop
    #         print(len(first_stop.connections))
    #         break

    #     # als alle first stops zijn bereden, break
        
    # if first_stop == None:
    #     first_stop = pick_random_first_stop(stations, stops)
    
    # return first_stop

    # ----------- SHORTEST CONENCTION -------------

def run(routes, max_time, hill_climber):
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

            if ro.all_stations_visited(ro.stations):
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
    ro.plot()
    score.print_results(final_score, ro.train_data, "data/output.csv")
    print(f"no score: {final_score}")

    
    
    # # ----------- HILL CLIMBER ------------------
    if hill_climber == True: 
        ro.improve_route()

        final_score = score.calculate_score(ro.trains, ro.stations)
        ro.plot()
        score.print_results(final_score, ro.train_data, "data/output2.csv")
        print(f"hc score: {final_score}")
        print()
    
def pick_random_first_stop(stations, stops):
    

    while True:
        
        first_stop = random.choice(stations)

        if first_stop not in stops:
            break
        continue

    return first_stop



        


