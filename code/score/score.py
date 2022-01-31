
import csv

def calculate_score(trains, stations):
    visit_true = 0
    visit_false = 0

    for station in stations:
        if station.visited == True:
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

    new_score = score
    # print(new_score)
    highest_current_score = publish_highest_score(score)

    if float(new_score) > float(highest_current_score):
    
        score_dict = {"score": score}
        with open(data_file, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["train", "stations"])
            for key, value in train_data.items():
                # print([key, value])
                
                writer.writerow([key, value])

            for key, value in score_dict.items():
                writer.writerow([key, value])
                # print(f"New Score! {[key, value]}")
                # print()

def publish_highest_score(score):

    with open('code/score/output.csv', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        old_score = last_line[6:]

    return old_score
        