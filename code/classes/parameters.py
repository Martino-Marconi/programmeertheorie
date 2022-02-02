from numpy import average
import statistics
import matplotlib.pyplot as plt
import pandas as pd


def plot_results(runs, algorithms):
    """
    Plot histogram based on scores from different algorithms.
    """

    # create plot
    hist_plot = plt.figure("test_hist_plot", figsize=(18, 5))
    ax = plt.axes()

    colors = ["g", "b", "y", "r", "c", "m"]

    # assign colors to different algorithms
    for algorithm, color in zip(algorithms, colors):
        data = pd.DataFrame({'scores': algorithm.score_list})
        ax.hist(data['scores'], bins=100, label=algorithm.algorithm, color=color, alpha=0.5)

    # plot data
    ax.set_ylabel('frequentie')
    ax.set_xlabel('score')
    hist_plot.legend()
    hist_plot.suptitle(f'Scores per strategie voor {runs} runs')
    hist_plot.savefig("output/hist_scores_plot.png")


class Random:
    def __init__(self):
        """
        Random algorithm class
        """
        self.algorithm = "random"
        self.score_list = []
        self.highest = 0
        self.lowest = 0
        self.average = 0
        self.runs = 0
        self.st_deviation = int

    def append_score(self, score):
        """
        Append score to algorithm class
        """
        self.score_list.append(score)
        self.highest = max(self.score_list)
        self.lowest = min(self.score_list)
        self.average = average(self.score_list)
        self.runs += 1
        self.st_deviation = statistics.pstdev(self.score_list)

    def check_if_highest(self, score):
        """
        Checks if score is the highest score
        """
        if score >= self.highest:
            print(f"runs: {self.runs} -- {self.algorithm} IMPROVED with SCORE: {score}.")
            return True
        return False


class Random_whc:
    def __init__(self):
        """
        Random algorithm class with hill climber
        """
        self.algorithm = "random with hill climber"
        self.score_list = []
        self.highest = int
        self.lowest = int
        self.average = int
        self.runs = 0
        self.st_deviation = int

    def append_score(self, score):
        """
        Append score to algorithm class
        """
        self.score_list.append(score)
        self.highest = max(self.score_list)
        self.lowest = min(self.score_list)
        self.average = average(self.score_list)
        self.runs += 1
        self.st_deviation = statistics.pstdev(self.score_list)

    def check_if_highest(self, score):
        """
        Checks if score is the highest score
        """
        if score >= self.highest:
            print(f"runs: {self.runs} -- {self.algorithm} IMPROVED with SCORE: {score}.")
            return True
        return False


class Semi_random:
    def __init__(self):
        """
        Semi-random algorithm class.
        """
        self.algorithm = "Semi-Random"
        self.score_list = []
        self.highest = int
        self.lowest = int
        self.average = int
        self.runs = 0
        self.st_deviation = int

    def append_score(self, score):
        """
        Append score to algorithm class
        """
        self.score_list.append(score)
        self.highest = max(self.score_list)
        self.lowest = min(self.score_list)
        self.average = average(self.score_list)
        self.runs += 1
        self.st_deviation = statistics.pstdev(self.score_list)

    def check_if_highest(self, score):
        """
        Checks if score is the highest score
        """
        if score >= self.highest:
            print(f"runs: {self.runs} -- {self.algorithm} IMPROVED with SCORE: {score}.")
            return True
        return False


class Semi_random_whc:
    def __init__(self):
        """
        Semi-random algorithm with hill climber class.
        """
        self.algorithm = "Semi-Random with Hill Climber"
        self.score_list = []
        self.highest = int
        self.lowest = int
        self.average = int
        self.runs = 0
        self.st_deviation = int

    def append_score(self, score):
        """
        Append score to algorithm class
        """
        self.score_list.append(score)
        self.highest = max(self.score_list)
        self.lowest = min(self.score_list)
        self.average = average(self.score_list)
        self.runs += 1
        self.st_deviation = statistics.pstdev(self.score_list)

    def check_if_highest(self, score):
        """
        Checks if score is the highest score
        """
        if score >= self.highest:
            print(f"runs: {self.runs} -- {self.algorithm} IMPROVED with SCORE: {score}.")
            return True
        return False


class Shortest_con:
    def __init__(self):
        """
        Shortest connection algorithm class
        """
        self.algorithm = "Shortest connection"
        self.score_list = []
        self.highest = int
        self.lowest = int
        self.average = int
        self.runs = 0
        self.st_deviation = int

    def append_score(self, score):
        """
        Append score to algorithm class
        """
        self.score_list.append(score)
        self.highest = max(self.score_list)
        self.lowest = min(self.score_list)
        self.average = average(self.score_list)
        self.runs += 1
        self.st_deviation = statistics.pstdev(self.score_list)

    def check_if_highest(self, score):
        """
        Checks if score is the highest score
        """
        if score >= self.highest:
            print(f"runs: {self.runs} -- {self.algorithm} IMPROVED with SCORE: {score}.")
            return True
        return False


class Shortest_con_whc:
    def __init__(self):
        """
        Shortest connection with hill climber algorithm class
        """
        self.algorithm = "Shortest connection with Hill Climber"
        self.score_list = []
        self.highest = int
        self.lowest = int
        self.average = int
        self.runs = 0
        self.st_deviation = int

    def append_score(self, score):
        """
        Append score to algorithm class
        """
        self.score_list.append(score)
        self.highest = max(self.score_list)
        self.lowest = min(self.score_list)
        self.average = average(self.score_list)
        self.runs += 1
        self.st_deviation = statistics.pstdev(self.score_list)

    def check_if_highest(self, score):
        """
        Checks if score is the highest score
        """
        if score >= self.highest:
            print(f"runs: {self.runs} -- {self.algorithm} IMPROVED with SCORE: {score}.")
            return True
        return False
