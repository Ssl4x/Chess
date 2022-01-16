class Knight:
    def __init__(self, color):
        from colored_text import Colored
        self.color = color
        self.name = (Colored.WHITE if color == "w" else Colored.BLACK) + "N" + Colored.END
        self.code_name = color + "N"

    @staticmethod
    def turn(board, start_cage, target_cage, check_for_attack=False):
        from Chessboard import ChessBoard
        if not(board.empty(target_cage) or board[target_cage].color != board[start_cage].color):
            return "Impossible turn: you can't beat your pieces"
        i = start_cage
        s_possible_turns = ((i[0] + 2, i[1] + 1), (i[0] + 2, i[1] - 1), (i[0] - 2, i[1] + 1), (i[0] - 2, i[1] - 1),
                            (i[0] + 1, i[1] + 2), (i[0] + 1, i[1] - 2), (i[0] - 1, i[1] + 2), (i[0] - 1, i[1] - 2))
        possible_turns = []
        for j in s_possible_turns:
            if ChessBoard.within_the_board(j):
                possible_turns.append(j)
        if target_cage not in possible_turns:
            return "Impossible turn"
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
        if Knight.turn(board, start_cage, target_cage) == "ok":
            board[target_cage] = board[start_cage]
            board[start_cage] = board.clear_cage
            return "ok"
        return Knight.turn(board, start_cage, target_cage)
