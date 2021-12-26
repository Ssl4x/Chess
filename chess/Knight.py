class Knight:
    def __init__(self, color: str):
        from colored_text import Colored
        self.color = color
        self.name = (Colored.WHITE if color == "w" else Colored.BLACK) + "k" + Colored.END
        self.code_name = color + "k"

    @staticmethod
    def turn(board, start_cage, target_cage):
        from Chessboard import ChessBoard
        if not(board.empty(target_cage) or board[target_cage].color != board[start_cage].color):
            return "Impossible turn"
        i = start_cage
        s_possible_turns = [[i[0] + 2, i[1] + 1], [i[0] + 2, i[1] - 1], [i[0] - 2, i[1] + 1], [i[0] - 2, i[1] - 1],
                            [i[0] + 1, i[1] + 2], [i[0] + 1, i[1] - 2], [i[0] - 1, i[1] + 2], [i[0] - 1, i[1] - 2]]
        possible_turns = []
        for i in s_possible_turns:
            if ChessBoard.within_the_board(i):
                possible_turns.append(i)
        if target_cage not in possible_turns:
            return "Impossible turn"
        return "ok"
