class Pawn:
    def __init__(self, color):
        from colored_text import Colored
        self.color = color
        self.name = (Colored.WHITE if color == "w" else Colored.BLACK) + "P" + Colored.END
        self.code_name = color + ""

    @staticmethod
    def turn(board, start_cage, target_cage, check_for_attack=False):
        from Chessboard import ChessBoard
        cop = board.copy()
        color = board[start_cage].color
        cop[target_cage] = cop[start_cage]
        cop[start_cage] = cop.clear_cage
        if not check_for_attack:
            if cop.king_under_check(color):
                return "Impossible turn: king under check"
        if not ChessBoard.within_the_board(target_cage):
            return "Impossible turn: target cage without the board"
        if not (board.empty(target_cage) or board[target_cage].color != board[start_cage].color):
            return "Impossible turn: you can't beat your pieces"
        if not abs(start_cage[0] - target_cage[0]) + abs(start_cage[1] - target_cage[1]) <= 2:
            return "Impossible turn: to long turn"
        operand = -1 if board[start_cage].color == 'b' else +1
        if start_cage[1] == target_cage[1] and ((board[start_cage].color == 'w' and target_cage[0] > start_cage[0]) or
                                                (board[start_cage].color == 'b' and target_cage[0] < start_cage[0])) \
                and board.empty((start_cage[0] + operand, start_cage[1])) and \
                ((abs(start_cage[0] - target_cage[0]) == 2 and (start_cage[0] == 6 or start_cage[0] == 1)) or
                 abs(start_cage[0] - target_cage[0]) == 1):
            return "ok"
        if abs(start_cage[1] - target_cage[1]) == abs(start_cage[0] - target_cage[0]) and \
                ((board[start_cage].color == 'w' and target_cage[0] > start_cage[0]) or
                 (board[start_cage].color == 'b' and target_cage[0] < start_cage[0])) and not board.empty(target_cage):
            return "ok"
        return "Impossible turn"

    @staticmethod
    def make_turn(board, start_cage, target_cage):
        if Pawn.turn(board, start_cage, target_cage) == "ok":
            board[target_cage] = board[start_cage]
            board[start_cage] = board.clear_cage
            if target_cage[0] in [0, 7]:
                from Queen import Queen
                board[target_cage] = Queen(board[target_cage].color)
                return "ok", "="
            return "ok"
        return Pawn.turn(board, start_cage, target_cage)
