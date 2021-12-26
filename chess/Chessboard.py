class ChessBoard:
    def __init__(self, clear_cage='.'):
        self.white_king_pos = [None, None]
        self.black_king_pos = [None, None]
        self.clear_cage = clear_cage
        self.value = []
        for i in range(8):
            self.value.append([clear_cage for i in range(8)])

    def __getitem__(self, item):
        if type(item) == type((0, 0)):
            return self.value[item[0]][item[1]]
        else:
            return self.value[item]

    def __setitem__(self, key, value):
        self.value[key] = value

    def search_king(self, color: str):
        target = 'wK' if color == 'w' else 'bK'
        for i in range(len(self.value)):
            for j in range(len(self.value[i])):
                if self[i, j] == target:
                    return i, j
        return 'No king on the board'

    def default_chess_build(self):
        from Pawn import Pawn
        from Rook import Rook
        from Knight import Knight
        from Queen import Queen
        from Bishop import Bishop
        from King import King
        w = 'w'
        b = 'b'
        self[0] = [Rook(w), Knight(w), Bishop(w), King(w, self, [0, 3]), Queen(w), Bishop(w), Knight(w), Rook(w)]
        self[1] = [Pawn(w) for i in range(8)]
        self[6] = [Pawn(b) for i in range(8)]
        self[7] = [Rook(b), Knight(b), Bishop(b), King(b, self, [0, 3]), Queen(b), Bishop(b), Knight(b), Rook(b)]

    def empty(self, cage):
        if self.value[cage[0]][cage[1]] == self.clear_cage:
            return True
        else:
            return False

    def code_str(self):
        str_code = []
        for i in self.value:
            str_code.append([])
            for j in i:
                str_code[-1].append(None if type(j) is str else j.code_name)
        return str_code

    def __str__(self):
        s = ""
        for i in self.value:
            for j in i:
                s = s + ("." if type(j) is str else j.name) + " "
            s = s + "\n"
        return s

    @staticmethod
    def within_the_board(cage):
        if 0 <= cage[0] <= 7:
            return True
        else:
            return False


board = ChessBoard()
board[0][0] = 0
board.default_chess_build()
print(board)

