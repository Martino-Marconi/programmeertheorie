import code.classes.score as score

import copy


def hill_climber_algorithm(ro, final_score, algorithm, data_file):
    # deep copy current train data
    tmp_data = copy.deepcopy(ro.train_data)
    tmp_trains = copy.deepcopy(ro.trains)
    tmp_stations = copy.deepcopy(ro.stations)

    # improve route by adding stations to trains who have not travelled
    # for long enough
    ro.improve_train_length()

    for i in range(100):
        # improve route further by picking different end stations and seeing
        # if they improve the score
        ro.improve_last_stop()

        # if score has improved, keep new route; otherwise not
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

    # remove trains that go to stops that are all already visited by other trains
    ro.improve_trains_superfluous()

    # update train data
    ro.get_train_data()

    # calculate and plot scores
    algorithm.append_score(final_score)
    higher = algorithm.check_if_highest(final_score)

    if higher is True:
        ro.plot(ro.train_data)
        score.print_results(final_score, ro.train_data, data_file)
