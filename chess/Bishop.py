class Bishop:
    def __init__(self, color: str):
        from colored_text import Colored
        self.color = color
        self.name = (Colored.WHITE if color == "w" else Colored.BLACK) + "B" + Colored.END
        self.code_name = color + "B"

    @staticmethod
    def turn(board, start_cage: tuple[int, int], target_cage: tuple[int, int]):
        from Chessboard import ChessBoard
        if not ChessBoard.within_the_board(target_cage):
            return "without the board"
