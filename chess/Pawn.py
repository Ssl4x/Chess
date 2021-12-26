class Pawn:
    def __init__(self, color: str):
        from colored_text import Colored
        self.color = color
        self.name = (Colored.WHITE if color == "w" else Colored.BLACK) + "P" + Colored.END
        self.code_name = color + "P"

    @staticmethod
    def turn(board, start_cage, target_cage):
        from Chessboard import ChessBoard
        if not ChessBoard.within_the_board(target_cage):
            return "without the board"
        if board[start_cage].color == "w":
            if target_cage[1] == start_cage[1] + 1:
                if target_cage[0] == start_cage[0] and board.empty(target_cage):
                    return "ok"
                elif (target_cage[0] == start_cage[0] - 1 or target_cage[0] == start_cage + 1) and\
                        not board.empty(target_cage) and board[target_cage].color != board[start_cage].color:
                    return "ok"
            elif target_cage[1] == start_cage[1] + 2:
                if target_cage[0] == start_cage[0] and board.empty(target_cage):
                    return "ok"
        else:
            if target_cage[1] == start_cage[1] - 1:
                if target_cage[0] == start_cage[0] and board.empty(target_cage):
                    return "ok"
                elif (target_cage[0] == start_cage[0] - 1 or target_cage[0] == start_cage + 1) and\
                        not board.empty(target_cage) and board[target_cage].color != board[start_cage].color:
                    return "ok"
            elif target_cage[1] == start_cage[1] - 2:
                if target_cage[0] == start_cage[0] and board.empty(target_cage):
                    return "ok"
        return "Impossible turn"
