class Queen:
    def __init__(self, color: str):
        from colored_text import Colored
        self.color = color
        self.name = (Colored.WHITE if color == "w" else Colored.BLACK) + "Q" + Colored.END
        self.code_name = color + "Q"

    @staticmethod
    def turn(board, start_cage, target_cage):
        from Chessboard import ChessBoard
        if not ChessBoard.within_the_board(target_cage):
            return "without the board"