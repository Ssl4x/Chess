class Console:
    @staticmethod
    def input(board):
        while True:
            From, To = input("The first cage - where from, the second cage - where to go\n example: e2 e4").split()
            abc_to_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
            From = [abc_to_num[From[0]], int(From[1])]
            To = [abc_to_num[To[0]], int(To[1])]
            print(board[From].turn(board, From, To))
            if board[From].turn(board, From, To) == "ok":
                break
