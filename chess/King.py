class King:
    def __init__(self, color: str, board, position: list[int, int]):
        from colored_text import Colored
        self.color = color
        self.name = (Colored.WHITE if color == "w" else Colored.BLACK) + 'K' + Colored.END
        self.code_name = color + "K"
        if color == 'w':
            board.white_king_pos = position
        else:
            board.black_king_pos = position

    def turn(self, board, start_cage, target_cage):
        from Chessboard import ChessBoard
        if not ChessBoard.within_the_board(target_cage):
            return "without the board"

    @staticmethod
    def check_for_check(color: str):
        pass
