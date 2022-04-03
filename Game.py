class Game:
    def __init__(self, pgn_logger: dict = False, custom=False, board=None, visual=False):
        from Chessboard import ChessBoard
        print("Game was started.\nTo find out possible commands write 'help'.")
        board: ChessBoard
        self.visual = visual
        self.board = ChessBoard()
        if pgn_logger is not False:
            from PGNLogger import PGNLogger
            pgn_logger
            self.pgn_logger = PGNLogger(file_name=pgn_logger["File"] if "File" in pgn_logger.keys() else None,
                                        event=pgn_logger["Event"] if "Event" in pgn_logger.keys() else None,
                                        site=pgn_logger["Site"] if "Site" in pgn_logger.keys() else None,
                                        date=pgn_logger["Date"] if "Date" in pgn_logger.keys() else None,
                                        t_round=pgn_logger["Round"] if "Round" in pgn_logger.keys() else None,
                                        white=pgn_logger["White"] if "White" in pgn_logger.keys() else None,
                                        black=pgn_logger["Black"] if "Black" in pgn_logger.keys() else None,
                                        result=pgn_logger["Result"] if "Result" in pgn_logger.keys() else None)
        else:
            self.pgn_logger = False
        if not custom:
            self.default_game_configure()
            return
        self.board = board

    def default_game_configure(self):
        self.board.default_chess_build()

    @staticmethod
    def help():
        print("1. To exit from game: write 'exit'\n"
              "2. To make make turn: to make a turn write the cage from which you want to walk"
              " and the cell where you want to walk. Example - e2 e4")

    def exit(self):
        if self.pgn_logger is not False:
            self.pgn_logger.exit()
        exit()

    def turn(self):
        from Console import Console
        ret = self.board.checkmate()
        if ret is not False:
            return f"Checkmate: {'white' if ret == 'w' else 'black'} win"
        ret = False
        commands = ['help', 'exit']
        while not ret:
            print(self.board)
            print("White" if self.board.turn["color"] == 'w' else "Black", "move")
            if self.visual:
                from Board2d import Board2d
                user_command = Board2d.input(self)
            else:
                user_command = Console.input()
            if user_command in commands:
                if user_command == 'help':
                    self.help()
                elif user_command == 'exit':
                    self.exit()
            else:
                ret = self.board.make_turn(user_command[0], user_command[1])
            if ret == 'ok':
                if self.pgn_logger is not False:
                    self.pgn_logger.turn(self.board, user_command[0], user_command[1])
                ret = True
            elif type(ret) is tuple and ret[0] == 'ok':
                if self.pgn_logger is not False:
                    self.pgn_logger.turn(self.board, user_command[0], user_command[1], custom=ret[1])
                ret = True
            else:
                print(self.board.make_turn(user_command[0], user_command[1]))
        return ret
