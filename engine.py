"""

"""

class GameState:
    def __init__(self):
        self.board = [
            ["--", "--", "--"],
            ["--", "--", "--"],
            ["--", "--", "--"]
        ]
        self.human_to_move = True
        self.move_log = []

    def make_move(self, move):
        if self.human_to_move == True:
            self.board[move.row][move.col] = "x"
        else:
            self.board[move.row][move.col] = "o"

        self.move_log.append(move)
        self.human_to_move = not self.human_to_move


class Move:

    def __init__(self, target_square, board):
        self.row = target_square[0]
        self.col = target_square[1]