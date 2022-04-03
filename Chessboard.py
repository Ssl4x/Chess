from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Queen import Queen
from Bishop import Bishop
from King import King


# noinspection PyUnresolvedReferences
class ChessBoard:
    def __init__(self, clear_cage='.'):
        self.white_king_pos = [0, 0]
        self.black_king_pos = [0, 0]
        self.clear_cage = clear_cage
        self.value = []
        self.turn = {'color': 'w', 'num': 1}
        self.prev_pos = None
        for i in range(8):
            self.value.append([clear_cage for _ in range(8)])

    def __getitem__(self, item):
        if type(item) is int:
            return self.value[item]
        else:
            return self.value[item[0]][item[1]]

    def __setitem__(self, key, value):
        if type(key) is int:
            self.value[key] = value
        else:
            self.value[key[0]][key[1]] = value

    def __copy__(self):
        ret = ChessBoard()
        ret.clear_cage = self.clear_cage
        ret.white_king_pos = self.white_king_pos
        ret.black_king_pos = self.black_king_pos
        ret.value = [i.copy() for i in self.value]
        return ret

    def copy(self):
        return self.__copy__()

    def default_chess_build(self):
        w = 'w'
        b = 'b'
        self[0] = [Rook(w), Knight(w), Bishop(w), King(w, self, (0, 3)), Queen(w), Bishop(w), Knight(w), Rook(w)]
        self[1] = [Pawn(w) for _ in range(8)]
        self[6] = [Pawn(b) for _ in range(8)]
        self[7] = [Rook(b), Knight(b), Bishop(b), King(b, self, (7, 3)), Queen(b), Bishop(b), Knight(b), Rook(b)]
        self.prev_pos = self.copy()

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

    def simple_str(self):
        s = ""
        for i in self.value:
            for j in i:
                s = s + ("." if type(j) is str else j.name) + " "
            s = s + "\n"
        return s

    def __str__(self):
        s = ""
        s = " " + s + "-" * 18 + "\n"
        num = 8
        for i in self.value[::-1]:
            s = s + str(num)
            num -= 1
            s = s + "|"
            for j in i[::-1]:
                s = s + ("." if type(j) is str else j.name) + " "
            s = s + "|"
            s = s + "\n"
        s = s + " " + "-" * 18 + "\n"
        s = s + "  " + "a b c d e f g h" + "\n"
        return s

    @staticmethod
    def within_the_board(cage):
        if 0 <= cage[0] <= 7 and 0 <= cage[1] <= 7:
            return True
        else:
            return False

    def cage_under_enemy_attack(self, color, cage):
        board = self.copy()
        board[cage] = Pawn(color)
        for y in range(8):
            for x in range(8):
                if board.empty((y, x)):
                    continue
                if board[y, x].turn(board, (y, x), cage, check_for_attack=True) == "ok":
                    return True
        return False

    def king_under_check(self, color):
        if self.cage_under_enemy_attack(color, self.white_king_pos if color == 'w' else self.black_king_pos):
            return True
        return False

    def make_turn(self, start_cage, target_cage):
        if self.empty(start_cage):
            print(start_cage)
            return "start cage is empty"
        if self[start_cage].color != self.turn['color']:
            return "now it's " + ('white' if self.turn['color'] == 'w' else 'black') + "'s turn"
        prev_pos = self.copy()
        t = self[start_cage].make_turn(self, start_cage, target_cage)
        if t == 'ok' or type(t) is tuple and t[0] == 'ok':
            if self.turn['color'] == 'b':
                self.turn['num'] += 1
            self.prev_pos = prev_pos
            self.turn['color'] = 'b' if self.turn['color'] == 'w' else 'w'
        return t

    def possible_turns(self, start_cage):
        turns = []
        targets = []
        for i in range(8):
            for j in range(8):
                targets.append([i, j])
        for target_cage in targets:
            if self[start_cage].turn(self, start_cage, target_cage) == "ok":
                turns.append(target_cage)
        return turns

    def checkmate(self):
        for color in ["w", "b"]:
            if not self.king_under_check(color):
                continue
            if not self.possible_turns(self.white_king_pos if color == "w" else self.black_king_pos):
                return color
        return False
