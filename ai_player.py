import random
from .player import Player
from .shot import Shot

class AiPlayer(Player):
    def __init__(self):
        super().__init__(False)
        self.target_stack = []

    def choose_target(self, history, board):
        while self.target_stack:
            y, x = self.target_stack.pop()
            if not Shot.check_repeat(history, y, x):
                return y, x
        while True:
            y = random.randint(0, board.size-1)
            x = random.randint(0, board.size-1)
            if not Shot.check_repeat(history, y, x):
                return y, x

    def ai_turn(self, history, board, other_player):
        y, x = self.choose_target(history, board)
        ship_hit = self.fire(board, y, x)
        if ship_hit:
            for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                ny, nx = y+dy, x+dx
                if 0 <= ny < board.size and 0 <= nx < board.size:
                    if not Shot.check_repeat(history, ny, nx):
                        self.target_stack.append((ny, nx))
            sunk = ship_hit.hp == 0
            history.append(Shot("AI", None, y, x, "hit", sunk))
        else:
            history.append(Shot("AI", None, y, x, "miss"))
