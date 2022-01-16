class Console:
    @staticmethod
    def input():
        # i = tuple(map(lambda x: (int(x[0]) - 1, int(x[1]) - 1), input("Write your turn\n").split()))
        i = input().split()
        if len(i) == 1:
            return i[0]
        try:
            i = ((int(i[0][0]) - 1, int(i[0][1]) - 1), (int(i[1][0]) - 1, int(i[1][1]) - 1))
        except ValueError:
            try:
                ctoi = {'a': 7, 'b': 6, 'c': 5, 'd': 4, 'e': 3, 'f': 2, 'g': 1, 'h': 0}
                i = ((int(i[0][1]) - 1, ctoi[i[0][0]]), (int(i[1][1]) - 1, ctoi[i[1][0]]))
            except ValueError:
                raise Exception("invalid input")
        return i
