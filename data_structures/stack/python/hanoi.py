from stack import Stack

class Hanoi:
    def __init__(self, num_of_discs=3):
        
        self.num_of_discs = num_of_discs
        if num_of_discs > 6:
            print('6 is the maximum number of discs. Number of discs has been set to 6.')
            self.num_of_discs = 6

        self.pegs = [Stack() for i in range(3)]

        for i in range(self.num_of_discs):
            self.pegs[0].push(self.num_of_discs - i)
        
        print(self.pegs[0].items)

    def display_board(self):
        board = []

        for i in range(self.num_of_discs-1, -1 ,-1):
            row = []
            for j in range(len(self.pegs)-1, -1, -1):
                print(i, j)


h = Hanoi(3)
h.display_board()