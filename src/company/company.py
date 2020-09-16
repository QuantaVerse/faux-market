import random


class Company:
    def __init__(self):
        self.id = random.randint(100000, 999999)
        self.name = "ABC"
        self.total_stocks = 100000
        self.face_value = 2
        self.market_value = 2
