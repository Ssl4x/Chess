from Chessboard import ChessBoard
import pygame


class Board2d:
    def __init__(self, name):
        self.name = name
        self.W = 400
        self.H = 400

        self.sc = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Chess")

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        self.FPS = 60  # число кадров в секунду
        self.clock = pygame.time.Clock()

    def start_board(self):
        import pygame
        pygame.init()
        clicked = False
        click = (0, 0)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("Нажата кнопка: ", event.button, event.pos)
                    print(Board2d.define_a_cage_by_coordinates(event.pos))
                    prev_click = click
                    click = Board2d.define_a_cage_by_coordinates(event.pos)
                    if clicked:
                        pass
                    else:
                        pass

            Board2d.draw_2d_board(self, self.GREEN, self.WHITE)
            chessboard = ChessBoard()
            chessboard.default_chess_build()
            self.draw_image_board(Board2d.convert_char_board_to_image_board(chessboard.code_str()))
            pygame.display.update()
            self.clock.tick(self.FPS)

    @staticmethod
    def load_piece_img(codename):
        pieces = {'wR': 'WhiteRook', 'wk': 'WhiteKnight', 'wB': 'WhiteBishop',
                  'wK': 'WhiteKing', 'wQ': 'WhiteQueen', 'wP': 'WhitePawn',
                  'bR': 'BlackRook', 'bk': 'BlackKnight', 'bB': 'BlackBishop',
                  'bK': 'BlackKing', 'bQ': 'BlackQueen', 'bP': 'BlackPawn'}
        return pygame.image.load(f"images\\{pieces[codename]}.png").convert_alpha()

    @staticmethod
    def convert_char_board_to_image_board(char_board):
        img_board = []
        for i in char_board:
            img_board.append([])
            for j in i:
                if j is not None:
                    img_board[-1].append(Board2d.load_piece_img(j))
                else:
                    img_board[-1].append(None)
        return img_board

    def draw_image_board(self, img_board):
        for i in range(8):
            for j in range(8):
                if img_board[j][i] is not None:
                    self.sc.blit(img_board[j][i], (i * 50, j * 50))

    def draw_2d_board(self, color1, color2):
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(self.sc, color2 if (i + j) % 2 == 0 else color1,
                                 (50 * j, 50 * i, 50 * j + 50, 50 * i + 50))

    @staticmethod
    def define_a_cage_by_coordinates(coord):
        x = coord[0] // 50
        y = coord[1] // 50
        return x, y


board = Board2d("board")
board.start_board()
