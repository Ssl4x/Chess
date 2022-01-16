class King:
    def __init__(self, color: str, board, position: tuple[int, int]):
        from colored_text import Colored
        self.color = color
        self.name = (Colored.WHITE if color == "w" else Colored.BLACK) + 'K' + Colored.END
        self.code_name = color + "K"
        self.moved = False
        if color == 'w':
            board.white_king_pos = position
        else:
            board.black_king_pos = position

    @staticmethod
    def turn(board, start_cage, target_cage, check_for_attack=False):
        from Chessboard import ChessBoard
        board: ChessBoard
        if not ChessBoard.within_the_board(target_cage):
            return "Impossible turn: target cage without the board"
        if not (board.empty(target_cage) or board[target_cage].color != board[start_cage].color):
            return "Impossible turn: you can't beat your pieces"
        if abs(start_cage[1] - target_cage[1]) == 2 and start_cage[0] == target_cage[0] and not board[start_cage].moved:
            if start_cage[1] - target_cage[1] == 2 and not board[start_cage[0], 0].moved or \
                    start_cage[1] - target_cage[1] == -2 and not board[start_cage[0], 7].moved:
                if board.empty(target_cage) and \
                        board.empty((target_cage[0], int(target_cage[1] + (start_cage[1] - target_cage[1]) / 2))) and \
                        not board.cage_under_enemy_attack(board[start_cage].color,
                                                          (target_cage[0],
                                                          int(target_cage[1] + (start_cage[1] - target_cage[1]) / 2))):
                    return 'ok', (start_cage[0], 0) if start_cage[1] - target_cage[1] == 2 else (start_cage[0], 7), \
                           (target_cage[0], int(target_cage[1] + (start_cage[1] - target_cage[1]) / 2))
        if not (abs(start_cage[0] - target_cage[0]) <= 1 and abs(start_cage[1] - target_cage[1]) <= 1):
            return "Impossible turn"
        # check
        color = board[start_cage].color
        cop = board.copy()
        cop[target_cage] = cop[start_cage]
        cop[start_cage] = board.clear_cage
        if cop[target_cage].color == 'w':
            cop.white_king_pos = target_cage
        else:
            cop.black_king_pos = target_cage
        if not check_for_attack:
            if cop.king_under_check(color):
                return "Impossible turn: King under attack"
        return "ok"

    @staticmethod
    def make_turn(board, start_cage, target_cage):
        ret = King.turn(board, start_cage, target_cage)
        if ret == "ok":
            board[target_cage] = board[start_cage]
            board[start_cage] = board.clear_cage
            if board[target_cage].color == 'w':
                board.white_king_pos = target_cage
            else:
                board.black_king_pos = target_cage
            board[target_cage].moved = True
            return "ok"
        # castling
        elif type(ret) is tuple and ret[0] == "ok":
            board[target_cage] = board[start_cage]
            board[start_cage] = board.clear_cage
            if board[target_cage].color == 'w':
                board.white_king_pos = target_cage
            else:
                board.black_king_pos = target_cage
            board[target_cage].moved = True
            board[ret[2]] = board[ret[1]]
            board[ret[1]] = board.clear_cage
            board[ret[2]].moved = True
            return "ok", "0-0" if start_cage[1] - target_cage[1] == 2 else "0-0-0"
        if type(ret) is tuple:
            print((ret[0], ret[1], ret[2], "ERROR"))
            ret = (ret[0], ret[1], ret[2], "ERROR")
        return ret
