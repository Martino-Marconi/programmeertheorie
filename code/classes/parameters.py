from numpy import average
import statistics


class Random:
    def __init__(self):
        self.algorithm = "random"
        self.score_list = []
        self.highest = 0
        self.lowest = 0
        self.average = 0
        self.runs = 0
        self.st_deviation = int


    def append_score(self, score):

        self.score_list.append(score)
        self.highest = max(self.score_list)
        self.lowest = min(self.score_list)
        self.average = average(self.score_list)
        self.runs += 1
        self.st_deviation = statistics.pstdev(self.score_list)
        print(f"{self.algorithm} = Score: {score}, Highest: {self.highest}, Average: {self.average}")

        

    def check_if_highest(self, score):
        
        print(score)
        print(self.highest)

        if score >= self.highest:
            return True
        return False



class Random_whc:
    def __init__(self):
        self.algorithm = "random with hill climber"
        self.score_list = []
        self.highest = int
        self.lowest = int
        self.average = int
        self.runs = 0
        self.st_deviation = int


    def append_score(self, score):

        self.score_list.append(score)
        self.highest = max(self.score_list)
        self.lowest = min(self.score_list)
        self.average = average(self.score_list)
        self.runs += 1
        self.st_deviation = statistics.pstdev(self.score_list)
        print(f"{self.algorithm} = Score: {score}, Highest: {self.highest}, Average: {self.average}")

        
    def check_if_highest(self, score):

        if score >= self.highest:
            return True
        return False
        

class Semi_random:
    def __init__(self):
        self.algorithm = "Semi-Random"
        self.score_list = []
        self.highest = int
        self.lowest = int
        self.average = int
        self.runs = 0
        self.st_deviation = int


    def append_score(self, score):

        self.score_list.append(score)
        self.highest = max(self.score_list)
        self.lowest = min(self.score_list)
        self.average = average(self.score_list)
        self.runs += 1
        self.st_deviation = statistics.pstdev(self.score_list)
        print(f"{self.algorithm} = Score: {score}, Highest: {self.highest}, Average: {self.average}")

        
    def check_if_highest(self, score):

        if score >= self.highest:
            return True
        return False


class Semi_random_whc:
    def __init__(self):
        self.algorithm = "Semi-Random with Hill Climber"
        self.score_list = []
        self.highest = int
        self.lowest = int
        self.average = int
        self.runs = 0
        self.st_deviation = int


    def append_score(self, score):

        self.score_list.append(score)
        self.highest = max(self.score_list)
        self.lowest = min(self.score_list)
        self.average = average(self.score_list)
        self.runs += 1
        self.st_deviation = statistics.pstdev(self.score_list)
        print(f"{self.algorithm} = Score: {score}, Highest: {self.highest}, Average: {self.average}")

        
    def check_if_highest(self, score):

        if score >= self.highest:
            return True
        return False

class Shortest_con:
    def __init__(self):
        self.algorithm = "Shortest connection"
        self.score_list = []
        self.highest = int
        self.lowest = int
        self.average = int
        self.runs = 0
        self.st_deviation = int


    def append_score(self, score):

        self.score_list.append(score)
        self.highest = max(self.score_list)
        self.lowest = min(self.score_list)
        self.average = average(self.score_list)
        self.runs += 1
        self.st_deviation = statistics.pstdev(self.score_list)
        print(f"{self.algorithm} = Score: {score}, Highest: {self.highest}, Average: {self.average}")

        
    def check_if_highest(self, score):

        if score >= self.highest:
            return True
        return False


class Shortest_con_whc:
    def __init__(self):
        self.algorithm = "Shortest connection with Hill Climber"
        self.score_list = []
        self.highest = int
        self.lowest = int
        self.average = int
        self.runs = 0
        self.st_deviation = int


    def append_score(self, score):

        self.score_list.append(score)
        self.highest = max(self.score_list)
        self.lowest = min(self.score_list)
        self.average = average(self.score_list)
        self.runs += 1
        self.st_deviation = statistics.pstdev(self.score_list)
        print(f"{self.algorithm} = Score: {score}, Highest: {self.highest}, Average: {self.average}")

        
    def check_if_highest(self, score):

        if score >= self.highest:
            return True
        return False

