from code.algorithms import a_random, b_semi_random, shortest_connection
from code.classes.parameters import Random, Random_whc, Semi_random, Semi_random_whc, Shortest_con, Shortest_con_whc

import time
from sys import argv

if __name__ == "__main__":

    # 
    random = Random()
    random_whc = Random_whc()
    semi_random = Semi_random()
    semi_random_whc = Semi_random_whc()
    shortest_con = Shortest_con()
    shortest_con_whc = Shortest_con_whc()

    # check command line arguments
    if len(argv) not in [1,2, 3, 4, 5]:
        print("Usage: python3 main.py [algorithm] [runs] [available trains] [train duration]")
        exit(1)

    # command line arguments
    # nog afmaken

    # allocate data to required values
    # max time in minutes, run time in seconds
    routes = 20
    max_time = 180
    run_time = 60

    # set timer and amount of runs to default
    start = time.time()
    n_runs = 0

    # run until run time is finished
    while time.time() - start < run_time:
        for i in range(0, (run_time * 5), 10):
            if i == n_runs:
                print(f"runs: {n_runs}")
                break
        
        # --------------------- RANDOM ---------------------
        # this algorithm randomly choses it stops
        # set hill climber True/False if run with(out) hill climber
        a_random.run(routes, max_time, random, random_whc, hill_climber=True)


        # ------------------ SEMI_RANDOM ------------------
        # this algorithm semi-randomly choses it stops
        # it picks it stop randemly, but a already visited 
        # station cannot be visited again
        # set hill climber True/False if run with(out) hill climber
        b_semi_random.run(routes, max_time, semi_random, semi_random_whc, hill_climber=True)


        # ---------------SHORTEST_CONNECTION --------------
        # this algorithm choses it stops based on the 
        # shortest connection
        # set hill climber True/False if run with(out) hill climber
        shortest_connection.run(routes, max_time, shortest_con, shortest_con_whc, hill_climber=True)

        # ---------------LOWEST_CONNECTIONS--------------
        # this algorithm choses it stops based on the 
        # connected station with the lowest possible 
        # connected stations
        # ---------------------EMPTY----------------------

        # add one to runs
        n_runs += 1







