from Chessboard import ChessBoard
import pygame


class Board2d:
    def __init__(self):
        from Game import Game
        self.W = 400
        self.H = 400

        self.sc = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Chess")

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.game = Game(visual=True, pgn_logger={"File": "logs.txt"})
        self.FPS = 60  # число кадров в секунду
        self.clock = pygame.time.Clock()

    def start_game(self):
        import pygame

        pygame.init()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.exit()

            self.draw_2d_board((0, 100, 0), self.WHITE)
            self.draw_board_annotation()
            self.draw_image_board(Board2d.convert_char_board_to_image_board(self.game.board.code_str()))
            pygame.display.update()
            self.game.turn()
            self.clock.tick(self.FPS)

    @staticmethod
    def load_piece_img(codename):
        pieces = {'wR': 'WhiteRook', 'wN': 'WhiteKnight', 'wB': 'WhiteBishop',
                  'wK': 'WhiteKing', 'wQ': 'WhiteQueen', 'w': 'WhitePawn',
                  'bR': 'BlackRook', 'bN': 'BlackKnight', 'bB': 'BlackBishop',
                  'bK': 'BlackKing', 'bQ': 'BlackQueen', 'b': 'BlackPawn'}
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

    def draw_board_annotation(self):
        int_to_letter = {7: 'h', 6: 'g', 5: 'f', 4: 'e', 3: 'd', 2: 'c', 1: 'b', 0: 'a'}
        font = pygame.font.Font("freesansbold.ttf", 12)
        for i in range(8):
            letter = font.render(int_to_letter[i], True, self.BLACK)
            num = font.render(str(i + 1), True, self.BLACK)
            self.sc.blit(letter, [i * 50, 388])
            self.sc.blit(num, [0, i * 50])

    def draw_2d_board(self, color1, color2):
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(self.sc, color2 if (i + j) % 2 == 0 else color1,
                                 (50 * j, 50 * i, 50 * j + 50, 50 * i + 50))

    @staticmethod
    def input():
        clicked = False
        click = (0, 0)
        clock = pygame.time.Clock()
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    prev_click = click
                    click = Board2d.define_a_cage_by_coordinates(event.pos)
                    if clicked:
                        return prev_click, click
                    else:
                        clicked = True
            clock.tick(30)

    @staticmethod
    def define_a_cage_by_coordinates(coord):
        x = coord[1] // 50
        y = coord[0] // 50
        return x, y
