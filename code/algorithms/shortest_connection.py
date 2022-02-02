from code.classes.train import Train, Route
import code.classes.score as score
import code.algorithms.hill_climber as hc

import random
import pandas as pd


def pick_first_stop(stations, stops):
    """
    Pick the first stop for each train based on the
    shortest connection.
    """
    first_stop = pick_shortest_connection_start(stations, stops)

    return first_stop


def run(routes, max_time, shortest_con, shortest_con_whc, hill_climber):
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

            tr.next_station = tr.current_station.pick_shortest_connection(tr.current_station)

            # break if no station is available
            if tr.next_station is None:
                break

            distance = tr.current_station.get_travel_time(tr.next_station)

            # stop adding next stops if next stop will overwrite the maximum time
            if (distance + tr.time_travelled) > max_time:
                break
            
            # break if there are no useable connections
            if tr.no_useable_connections():
                break
            
            # break if all stations have been visited already
            if ro.all_stations_visited(ro.stations):
                break
            
            # add travel time
            tr.add_travel_time(distance)

            # append station to train
            train.stops.append(tr.next_station)
            tr.next_station.set_visited()
            tr.use_connections(tr.current_station, tr.next_station)
            ro.all_stops.append(tr.current_station)

            tr.current_station = tr.next_station

        tr.time_travelled = 0
        ro.train_counter += 1

        # break if all stations have been visited
        if ro.all_stations_visited(ro.stations):
            break

    # once number of required trains is reached, print + plot results and calculate score
    final_score = score.calculate_score(ro.trains, ro.stations)
    ro.get_train_data()

    shortest_con.append_score(final_score)
    higher = shortest_con.check_if_highest(final_score)

    if higher is True:
        ro.plot(ro.train_data)

        data_file = "output/shortest_connection.csv"
        score.print_results(final_score, ro.train_data, data_file)

    # # ----------- HILL CLIMBER ------------------
    if hill_climber is True:
        data_file = "output/shortest_connection_whc.csv"
        hc.hill_climber_algorithm(ro, final_score, shortest_con_whc, data_file)


def pick_shortest_connection_start(stations, stops):
    empty_dataframe = pd.DataFrame()

    # add connections to dataframe and sort dataframe based on travel time
    for station in stations:
        new_station = {'station1': station, 'station2': station.connections.keys(), 'time': station.connections.values()}
        connections_df = pd.DataFrame.from_dict(new_station)
        empty_dataframe = empty_dataframe.append(connections_df, ignore_index=True)
    sorted_dataframe = empty_dataframe.sort_values(by="time", ascending=True, ignore_index=True)

    # get shortest connection from dataframe
    for index, row in sorted_dataframe.iterrows():
        count = random.choice(range(index, (index+3)))
        first_stop = sorted_dataframe.iloc[count]

        if first_stop.station1 not in stops or first_stop.station2 not in stops:

            return first_stop.station1
        continue

    first_stop = pick_random_first_stop(stations, stops)
    return first_stop


def pick_random_first_stop(stations, stops):
    """
    Pick a random first stop based on all stations.
    """
    while True:

        first_stop = random.choice(stations)

        if first_stop not in stops:
            break
        continue

    return first_stop
