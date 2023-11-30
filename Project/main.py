print("Sudoku Game")

sampleTable = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]


class Game:
    def __init__(self, row, col, table):
        self.row = row
        self.column = col
        self.table = table

    def printTable(self):
        print("+----+-----+-----+-----+-----+-----+-----+-----+-----+")
        for i in range(self.row):
            print("|", end=" ")
            for j in range(self.column):
                print(self.table[i][j], end="  |  ")
            print()
            print("+----+-----+-----+-----+-----+-----+-----+-----+-----+")

    def validNum(self, x, y, number):
        # Problem in row
        for i in range(9):
            if self.table[x][i] == number:
                # print("Problem in row!")
                return False

        # Problem in column
        for i in range(9):
            if self.table[i][y] == number:
                # print("Problem in column!")
                return False

        # Problem in region
        arr = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        region = ((x // 3) * 3) + (y // 3)
        for i in arr[region // 3]:
            for j in arr[region % 3]:
                if self.table[i][j] == number:
                    # print("Problem in region!")
                    return False

        return True

    def solveProblem(self, x, y):
        if y == 9:
            if x == 8:
                return True
            x += 1
            y = 0

        if self.table[x][y] > 0:
            return self.solveProblem(x, y + 1)

        for i in range(1, 10):
            if self.validNum(x, y, i):
                self.table[x][y] = i
                if self.solveProblem(x, y + 1):
                    return True
            self.table[x][y] = 0

        return False


sudokuGame = Game(9, 9, sampleTable)
sudokuGame.printTable()

print("\n\n\n")

if not sudokuGame.solveProblem(0, 0):
    print("This problem is not solvable")
else:
    print("This problem is solvable:")
    sudokuGame.printTable()
