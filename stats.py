class Stats:
    chances = 10

    def __init__(self):
        self.bulls = 0
        self.cows = 0

    def add_bulls(self):
        self.bulls += 1

    def add_cows(self):
        self.cows += 1

    def reset_bulls(self):
        self.bulls = 0

    def reset_cows(self):
        self.cows = 0

    def print_stats(self):
        print(f"Bulss: {self.bulls}, Cows: {self.cows}")
