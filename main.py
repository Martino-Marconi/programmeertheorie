from code.classes.train import Route
from code.algorithms import a_random, b_semi_random, time_travelled, shortest_connection
from code.classes.parameters import Random, Random_whc, Semi_random, Semi_random_whc, Shortest_con, Shortest_con_whc

from sys import argv
import time

if __name__ == "__main__":

    random = Random()
    random_whc = Random_whc()
    semi_random = Semi_random()
    semi_random_whc = Semi_random_whc()
    shortest_con = Shortest_con()
    shortest_con_whc = Shortest_con_whc()

    routes = 20
    max_time = 180
    run_time = 5

    start = time.time()
    n_runs = 0

    while time.time() - start < run_time:
        print(f"run: {n_runs}")
        
        # --------------------- RANDOM ---------------------
        # randomly pick first stop
        # print("random")
        # for x in range(runs):
        # a_random.run(routes, max_time, random, random_whc, hill_climber=False)
        # print()
        a_random.run(routes, max_time, random, random_whc, hill_climber=True)


        # ------------------ SEMI_RANDOM ------------------
        # semi-randomly pick first stop
        # Average: xxxx (1000 runs)
        # print("semi-random")
        # for x in range(runs):
        # b_semi_random.run(routes, max_time, semi_random, semi_random_whc, hill_climber=False)
        # print()
        b_semi_random.run(routes, max_time, semi_random, semi_random_whc, hill_climber=True)


        # ---------------SHORTEST_CONNECTION --------------
        # semi-randomly pick first stop
        # Average: xxxx (1000 runs)
        # print("shortest-connection")
        # for x in range(runs):  
        # shortest_connection.run(routes, max_time, shortest_con, shortest_con_whc, hill_climber=False)
        # print()
        shortest_connection.run(routes, max_time, shortest_con, shortest_con_whc, hill_climber=True)


        # add one to runs
        n_runs += 1
        print()
        print()






