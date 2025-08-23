import random
from .ship import Ship
from .shot import Shot

class Player:
    def __init__(self, is_human=False):
        self.is_human = is_human
        self.fleet = [Ship(l) for l in [5,4,3,3,2]]

    def place(self, board, ship, y, x, direction):
        if not self.check_fit(board, ship, y, x, direction):
            return False
        for i in range(ship.length):
            ny, nx = y, x
            if direction == "left":  nx -= i
            if direction == "right": nx += i
            if direction == "up":    ny -= i
            if direction == "down":  ny += i
            board.board[ny][nx]["ship"] = ship
        return True

    def random_place(self, board):
        for ship in self.fleet:
            while True:
                y = random.randint(0, board.size-1)
                x = random.randint(0, board.size-1)
                direction = random.choice(["left","right","up","down"])
                if self.place(board, ship, y, x, direction):
                    break
        return board

    def fire(self, board, y, x):
        tile = board.board[y][x]
        if tile.get("hit") or tile.get("miss"):
            return None
        if tile.get("ship"):
            ship = tile["ship"]
            ship.hp -= 1
            tile["hit"] = True
            if ship.hp == 0 and ship in self.fleet:
                self.fleet.remove(ship)
            return ship
        else:
            tile["miss"] = True
            return None

    def check_fit(self, board, ship, y, x, direction):
        for i in range(ship.length):
            ny, nx = y, x
            if direction == "left":  nx -= i
            if direction == "right": nx += i
            if direction == "up":    ny -= i
            if direction == "down":  ny += i
            if not (0 <= ny < board.size and 0 <= nx < board.size):
                return False
            if board.board[ny][nx].get("ship"):
                return False
        return True
