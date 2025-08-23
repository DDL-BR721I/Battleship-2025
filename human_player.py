from .player import Player
from .shot import Shot

class Human_player(Player):
    def __init__(self):
        super().__init__(True)

    def human_turn(self, history, other_player, board, y, x):
        hit_ship = self.fire(board, y, x)
        if hit_ship:
            sunk = hit_ship.hp == 0
            history.append(Shot("human", None, y, x, "hit", sunk))
            return "hit"
        else:
            history.append(Shot("human", None, y, x, "miss"))
            return "miss"
