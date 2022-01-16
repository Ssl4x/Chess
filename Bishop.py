class Bishop:
    def __init__(self, color):
        from colored_text import Colored
        self.color = color
        self.name = (Colored.WHITE if color == "w" else Colored.BLACK) + "B" + Colored.END
        self.code_name = color + "B"

    @staticmethod
    def turn(board, start_cage: tuple[int, int], target_cage: tuple[int, int], check_for_attack=False):
        from Chessboard import ChessBoard
        if not ChessBoard.within_the_board(target_cage):
            return "Impossible turn: target cage without the board"
        if not abs(target_cage[0] - start_cage[0]) == abs(target_cage[1] - start_cage[1]):
            return "Impossible turn"
        path = []
        vec = (1 if target_cage[0] > start_cage[0] else -1, 1 if target_cage[1] > start_cage[1] else -1)
        for i in range(1, abs(target_cage[0] - start_cage[0])):
            path.append([start_cage[0] + vec[0] * i, start_cage[1] + vec[1] * i])
        for cage in path:
            if not board.empty(cage):
                return "Impossible turn: can't jump over other pieces"
        if not (board.empty(target_cage) or board[target_cage].color != board[start_cage].color):
            return "Impossible turn: you can't beat your pieces"
        cop = board.copy()
        color = board[start_cage].color
        cop[target_cage] = cop[start_cage]
        cop[start_cage] = cop.clear_cage
        if not check_for_attack:
            if cop.king_under_check(color):
                return "Impossible turn: king under check"
        return "ok"

    @staticmethod
    def make_turn(board, start_cage, target_cage):
        if Bishop.turn(board, start_cage, target_cage) == "ok":
            board[target_cage] = board[start_cage]
            board[start_cage] = board.clear_cage
            return "ok"
        return Bishop.turn(board, start_cage, target_cage)
