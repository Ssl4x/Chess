class Rook:
    def __init__(self, color):
        from colored_text import Colored
        self.color = color
        self.name = (Colored.WHITE if color == "w" else Colored.BLACK) + "R" + Colored.END
        self.code_name = color + "R"
        self.moved = False

    @staticmethod
    def turn(board, start_cage: tuple[int, int], target_cage: tuple[int, int], check_for_attack=False):
        from Chessboard import ChessBoard
        board: ChessBoard
        if not ChessBoard.within_the_board(target_cage):
            return "Impossible turn: target cage without the board"
        if start_cage[0] == target_cage[0]:
            path = [[start_cage[0], i] for i in range(min(start_cage[1], target_cage[1]) + 1, max(start_cage[1], target_cage[1]))]
        elif start_cage[1] == target_cage[1]:
            path = [[i, start_cage[1]] for i in range(min(start_cage[0], target_cage[0]) + 1, max(start_cage[0], target_cage[0]))]
        else:
            return "Impossible turn!"
        for cage in path:
            if not board.empty(cage):
                return "Impossible turn: can't jump over other pieces"
        if (not board.empty(target_cage)) and board[target_cage].color == board[start_cage].color:
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
        if Rook.turn(board, start_cage, target_cage) == "ok":
            board[target_cage] = board[start_cage]
            board[start_cage] = board.clear_cage
            board[target_cage].moved = True
            return "ok"
        return Rook.turn(board, start_cage, target_cage)
