class MovingAverage:

    def __init__(self, size: int):
        self.window = []
        self.size = size

    def next(self, val: int) -> float:
        self.window.append(val)
        return sum(self.window[-self.size:]) / min(len(self.window),self.size)