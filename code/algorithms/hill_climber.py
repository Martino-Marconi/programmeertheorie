import code.score.score as score

import copy

def hill_climber_algorithm(ro, final_score, algorithm, data_file):
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

    algorithm.append_score(final_score)
    higher = algorithm.check_if_highest(final_score)
    
    if higher == True:
        ro.plot(ro.train_data)
        score.print_results(final_score, ro.train_data, data_file)