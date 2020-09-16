import random
from typing import List


class Market:
    def __init__(self):
        self.ticker_snapshots: List[Ticker] = []
        self.init_snapshot()

    def init_snapshot(self):
        self.ticker_snapshots.append(Ticker())


class Ticker:
    def __init__(self):
        self.close = 100
        self.volume = 1000
        self.volume_max = 100000

    def tick(self):
        self.close = (1 + (random.randint(-100, 100) / 100)) * self.close
        self.volume = random.randint(1000, 100000)

