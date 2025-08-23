class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[{"ship": None, "hit": False, "miss": False} for _ in range(size)] for _ in range(size)]
