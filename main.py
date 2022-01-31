from code.classes.train import Route

from code.algorithms import a_random
from code.algorithms import b_semi_random
from code.algorithms import time_travelled
from code.algorithms import shortest_connection


# from code.algorithms import breadth_first
from code.classes.loader import file_loader

if __name__ == "__main__":

    # # ask for user input
    # print()
    # routes = int(input("How many trains are available? "))
    # print()
    # max_time = int(input("How many minutes does a train drive? "))
    # print()
    # runs = int(input("How many runs? "))
    # print()
    # hill_climber = input("Hillclimber is = True or False? ")
    # print()

    # add trains to Route class
    routes = 20
    max_time = 180
    runs = 5
    hill_climber = True

    print(f"Routes: {routes}")
    print(f"Max time: {max_time}")
    print(f"Runs: {runs}")
    print()

    # --------------------- RANDOM ---------------------
    # randomly pick first stop
    print("random")
    for x in range(runs):
        a_random.run(routes, max_time, hill_climber)
    print()


    # ------------------ SEMI_RANDOM ------------------
    # semi-randomly pick first stop
    # Average: xxxx (1000 runs)
    print("semi-random")
    for x in range(runs):
        b_semi_random.run(routes, max_time, hill_climber)
    print()


    # ---------------SHORTEST_CONNECTION --------------
    # semi-randomly pick first stop
    # Average: xxxx (1000 runs)
    print("shortest-connection")
    for x in range(runs):  
        shortest_connection.run(routes, max_time, hill_climber)
    print()

    # # # ---------------TIME_TRAVELLED ------------------
    # # # semi-randomly pick first stop
    # # # Average: xxxx (1000 runs)
    # for x in range(runs):  
    #     time_travelled.run(routes, max_time)
    # print()

    # ---------------HILL_CLIMBER -------------------
    # semi-randomly pick first stop
    # Average: xxxx (1000 runs)
    
    # improve_route.run(routes, max_time)






