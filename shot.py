class Shot:
    def __init__(self, decision, direction, y, x, result, sunk=False):
        self.decision = decision
        self.direction = direction
        self.y = y
        self.x = x
        self.result = result
        self.sunk = sunk

    @staticmethod
    def check_repeat(history, y, x):
        return any(s.y == y and s.x == x for s in history)
