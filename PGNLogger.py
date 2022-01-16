class PGNLogger:
    def __init__(self, file_name, event=None, site=None, date=None, t_round=None, white=None, black=None, result=None):
        self.file_name = file_name
        self.event = event
        self.site = site
        self.date = date
        self.round = t_round
        self.white = white
        self.black = black
        if result is None:
            result = "*"
        self.result = result
        self.turns = [[]]

    def turn(self, board, start_cage, target_cage, custom=None):
        if custom is not None:
            self.turns[-1].append(custom)
        else:
            int_to_letter = {0: 'h', 1: 'g', 2: 'f', 3: 'e', 4: 'd', 5: 'c', 6: 'b', 7: 'a'}
            self.turns[-1].append(board[target_cage].code_name[1:] +
                                  int_to_letter[start_cage[1]] + str(start_cage[0] + 1) +
                                  int_to_letter[target_cage[1]] + str(target_cage[0] + 1))
        if len(self.turns[-1]) % 2 == 0:
            self.turns.append([])

    def exit(self):
        if self.turns == [[]]:
            exit()
        if not self.turns[-1]:
            self.turns.pop(len(self.turns) - 1)
        with open(self.file_name, "w") as f:
            for i in zip(["Event", "Site", "Data", "Round", "White", "Black", "Result"],
                         [self.event, self.site, self.date, self.round, self.white, self.black, self.result]):
                if i[1] is None:
                    i = list(i)
                    i[1] = "?"
                f.write(f'[{i[0]} "{i[1]}"]\n')
            i = 0
            for turn in self.turns:
                i += 1
                f.write(f"{i}. {turn[0]}{' ' + turn[1] if len(self.turns[-1]) == 2 else ''} ")
            f.write(self.result)
