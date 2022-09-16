import collections


class Solution:
    # every row and column has 1-9 no repeat
    # every 3 by 3 box has 1-9 no repeat
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        hashsetHor = set()  # for the row
        hashsetVer = set()  # for the column
        hashsetSquare = [[set() for i in range(3)]for j in range(3)]

        print (hashsetSquare)
        for row in range(9):
            hashsetHor.clear()  # clears set for next row
            hashsetVer.clear()  # clears set for next column
            for col in range(9):
                if hor != ".": # filters blank space
                    continue
                # checking horizontal
                hor = board[row][col]
                if hor != ".":  # filters blank space
                    if hor in hashsetHor:
                        return False
                    hashsetHor.add(hor)

                # checking vertical
                ver = board[col][row]
                if ver != ".":  # filters blank space
                    if ver in hashsetVer:
                        return False
                    hashsetVer.add(ver)

                # checking quadants
                if hor != ".":  # filters blank space
                    # 0-8 coords is converted into 0-2 coords by dividing by 3 and rounding down
                    if hor in hashsetSquare[row//3][col//3]:
                        return False
                    hashsetSquare[row//3][col//3].add(hor)


        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:  # the same idea as above but using dictionaries and a little more optimised
        cols = collections.defaultdict(set)  # the key is col #, value is set
        rows = collections.defaultdict(set)  # the key is row #, value is set
        squares = collections.defaultdict(set)  # the key is 0-2 coord in a tuple, value is set

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue  # skips everything after

                if board[r][c] in rows[r] or \
                   board[r][c] in cols[c] or \
                   board[r][c] in squares[(r//3, c//3)]:
                    return False
                else:  # these add funtions will not work if the defaultdict isn't a set
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])
        print(cols)
        return True

    # false example
    '''board = \
        [["8","3",".",  ".","7",".",  ".",".","."]
        ,["6",".",".",  "1","9","5",  ".",".","."]
        ,[".","9","8",  ".",".",".",  ".","6","."]

        ,["8",".",".",  ".","6",".",  ".",".","3"]
        ,["4",".",".",  "8",".","3",  ".",".","1"]
        ,["7",".",".",  ".","2",".",  ".",".","6"]

        ,[".","6",".",  ".",".",".",  "2","8","."]
        ,[".",".",".",  "4","1","9",  ".",".","5"]
        ,[".",".",".",  ".","8",".",  ".","7","9"]]'''
    # true example
    board = \
        [["5","3",".",  ".","7",".",  ".",".","."]
        ,["6",".",".",  "1","9","5",  ".",".","."]
        ,[".","9","8",  ".",".",".",  ".","6","."]

        ,["8",".",".",  ".","6",".",  ".",".","3"]
        ,["4",".",".",  "8",".","3",  ".",".","1"]
        ,["7",".",".",  ".","2",".",  ".",".","6"]

        ,[".","6",".",  ".",".",".",  "2","8","."]
        ,[".",".",".",  "4","1","9",  ".",".","5"]
        ,[".",".",".",  ".","8",".",  ".","7","9"]]
    print(isValidSudoku(2, board))