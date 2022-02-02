from code.algorithms import a_random, b_semi_random, shortest_connection
from code.classes.parameters import Random, Random_whc, Semi_random, Semi_random_whc, Shortest_con, Shortest_con_whc
from code.classes import parameters

import argparse
import time

if __name__ == "__main__":

    # create a command line argument parser
    parser = argparse.ArgumentParser(description="Build train network")
    parser.add_argument("algorithm", type=str, help="Choose algorithm. Options: random, semi-random, shortest-connection, all")
    parser.add_argument("runs", type=int, help="Number of runs")
    parser.add_argument("trains", type=int, default=20, help="Number of trains")
    parser.add_argument("duration", type=int, default=180, help="Maximum train duration")

    # parse command line arguments
    args = parser.parse_args()

    # assign command line arguments to variables
    # max_time in minutes; run_time in seconds
    algorithm = args.algorithm
    routes = args.trains
    max_time = args.duration
    runs = args.runs
    run_time = 120

    # create algorithm classes
    random = Random()
    random_whc = Random_whc()
    semi_random = Semi_random()
    semi_random_whc = Semi_random_whc()
    shortest_con = Shortest_con()
    shortest_con_whc = Shortest_con_whc()

    # set timer and amount of runs to default
    start = time.time()
    n_runs = 0

    # # option = run until run time is finished
    # while time.time() - start < run_time:
    #     for i in range(0, (run_time * 5), 10):
    #         if i == n_runs:
    #             print(f"runs: {n_runs}")
    #             break

    # option = run until allocated runs are finished
    for i in range(runs):
        # --------------------- RANDOM ---------------------
        # this algorithm randomly choses it stops
        # set hill climber True/False if run with(out) hill climber
        if algorithm == "random" or algorithm == "all":
            a_random.run(routes, max_time, random, random_whc, hill_climber=True)

        # ------------------ SEMI_RANDOM ------------------
        # this algorithm semi-randomly choses it stops
        # it picks it stop randemly, but a already visited
        # station cannot be visited again
        # set hill climber True/False if run with(out) hill climber
        if algorithm == "semi-random" or algorithm == "all":
            b_semi_random.run(routes, max_time, semi_random, semi_random_whc, hill_climber=True)

        # ---------------SHORTEST_CONNECTION --------------
        # this algorithm choses it stops based on the
        # shortest connection
        # set hill climber True/False if run with(out) hill climber
        if algorithm == "shortest-connection" or algorithm == "all":
            shortest_connection.run(routes, max_time, shortest_con, shortest_con_whc, hill_climber=True)

        # add one to runs
        n_runs += 1

    # plot the results in a histogram
    parameters.plot_results(n_runs, [random, random_whc, semi_random, semi_random_whc, shortest_con, shortest_con_whc])

