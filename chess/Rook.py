class Rook:
    def __init__(self, color):
        from colored_text import Colored
        self.color = color
        self.name = (Colored.WHITE if color == "w" else Colored.BLACK) + "R" + Colored.END
        self.code_name = color + "R"

    @staticmethod
    def turn(board, start_cage: tuple[int, int], target_cage: tuple[int, int]):
        from Chessboard import ChessBoard
        if not ChessBoard.within_the_board(target_cage):
            return "without the board"
        if start_cage[0] == target_cage[0]:
            path = [[start_cage[0], i] for i in
                    range(min(start_cage[1], target_cage[1]) + 1, max(start_cage[1], start_cage[1]))]
        elif start_cage[1] == target_cage[1]:
            path = [[start_cage[1], i] for i in
                    range(min(start_cage[0], target_cage[0]) + 1, max(start_cage[0], start_cage[0]))]
        else:
            return "Impossible turn!"
        for cage in path:
            if board[cage[0], cage[1]] != board.clear_cage:
                return "Impossible turn"
        return "ok"
