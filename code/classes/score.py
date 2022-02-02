import csv


def calculate_score(trains, stations):
    """
    Calculate score based on formula given for train routes.
    The higher the score, the better the route.
    """
    visit_true = 0
    visit_false = 0

    # calculate how many stations have been visited
    for station in stations:
        if station.visited > 0:
            visit_true += 1
        else:
            visit_false += 1

    stations_visited = visit_true / (visit_false + visit_true)

    # calculate total travel time
    number_of_trains = len(trains)
    total_travel_time = 0

    for train in trains:
        total_travel_time += train.time_travelled

    # formula to calculate score
    score = stations_visited * 10000 - (number_of_trains * 100 + total_travel_time)

    return score


def print_results(score, train_data, data_file):
    """
    Print train names and their stops, together with the route score
    to a csv file.
    """
    score_dict = {"score": score}
    with open(data_file, "w") as file:
        writer = csv.writer(file)
        writer.writerow(["train", "stations"])
        for key, value in train_data.items():

            writer.writerow([key, value])

        for key, value in score_dict.items():
            writer.writerow([key, value])
