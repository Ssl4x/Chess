class Queen:
    def __init__(self, color):
        from colored_text import Colored
        self.color = color
        self.name = (Colored.WHITE if color == "w" else Colored.BLACK) + "Q" + Colored.END
        self.code_name = color + "Q"

    @staticmethod
    def turn(board, start_cage, target_cage, check_for_attack=False):
        from Chessboard import ChessBoard
        from Bishop import Bishop
        from Rook import Rook
        if not ChessBoard.within_the_board(target_cage):
            return "Impossible turn: target cage without the board"
        if Bishop.turn(board, start_cage, target_cage,
                       check_for_attack=True if check_for_attack else False) == "ok" or \
                Rook.turn(board, start_cage, target_cage,
                          check_for_attack=True if check_for_attack else False) == "ok":
            return "ok"
        else:
            return "Impossible turn"

    @staticmethod
    def make_turn(board, start_cage, target_cage):
        if Queen.turn(board, start_cage, target_cage) == "ok":
            board[target_cage] = board[start_cage]
            board[start_cage] = board.clear_cage
            return "ok"
        return Queen.turn(board, start_cage, target_cage)
