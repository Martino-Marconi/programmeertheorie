
import csv

def calculate_score(trains, stations):
    visit_true = 0
    visit_false = 0

    for station in stations:
        if station.visited > 0:
            visit_true += 1
        else:
            visit_false += 1

    stations_visited = visit_true / (visit_false + visit_true) 


    number_of_trains = len(trains)
    
    total_travel_time = 0

    for train in trains:
        total_travel_time += train.time_travelled
    
    score = stations_visited * 10000 - (number_of_trains * 100 + total_travel_time)

    return score

def print_results(score, train_data, data_file):

    score_dict = {"score": score}
    with open(data_file, "w") as file:
        writer = csv.writer(file)
        writer.writerow(["train", "stations"])
        for key, value in train_data.items():
            
            writer.writerow([key, value])

        for key, value in score_dict.items():
            writer.writerow([key, value])


        