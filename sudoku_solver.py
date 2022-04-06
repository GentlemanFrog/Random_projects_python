# Sudoku solver able to solve every puzzle we give to it, puzzle should be in from of
# list of lists where ich inner list is a row in our sudoku puzzle

# steps:
# 1. Where you can start in puzzle
# 1.1 Is this puzzle properly solved
# 2. If there is a place to put number, then make a guess between 1 and 9
# 3. Checking if guess is correct
# 4. Calling function again to solve
# 5. Cathcing that our guess can be wrong and we have to back track to solve
# 6. Solution can't be find what then....

# Function for finding spot (row, colume) which is not filled on the sudoku
def find_empty(puzzle):
    # Open spaces will be -1
    # return row, col tuple (or (None, None) if there is none)
    # keep in mind that we are using 0-8 for our indicies
    # so we search each row and each column and we will return first empty space we meet
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == -1:
                return row, column

    return None, None # no empty spaces


def is_guess_valid(puzzle, guess, row, col):
    # return True when our guess is valid
    # so when out guess is number which is already in the row or column or
    # 3x3 matrix we check it and return false

    # checking row: (all values of the row are on the row index so we can simply check them)
    row_values = puzzle[row]
    if guess in row_values:
        return False

    # # checking columns:
    # col_values = []
    # # we have to search our column values through the list of rows at the same index
    # for i in range(9): # in range(9) cos this is all number of rows
    #     col_values.append(puzzle[i][column])
    # # using list comprahension:
    col_values = [puzzle[i][col] for i in range(8)]
    if guess in col_values:
        return False

    # checking 3x3 matrix:
    # problem in this situation is that we have to know where 3x3 starts
    # and then we have to iterate on all rows and columns of this 3x3 matrix to know if its ok
    # so to get starting point of the row:
    row_start = (row // 3) *3 #1//3 = 0, 5//3 = 1 ... and after we multiply it by 3 we get exact index
    # of starting row, then we have to iterate through 3x3 matrix
    # we can do the same for columns
    col_start = (col // 3) *3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    # if we pass we can return true:
    return True


def solve_sudoku(puzzle):
    # 1. step choosing where we wanna start
    row, col = find_empty(puzzle)
    # Validation of properly solved puzzle:
    if row is None:
        return True

    # step 2:
    for guess in range(1,10):
        # step 3:
        if is_guess_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # recursivly call function again if its valid:
            if solve_sudoku(puzzle):
                return True
        # When its not true: step 5
        # when guess is not valid, we need to backtrack and try other numbers:
        puzzle[row][col] = -1  # reset value

    # step 6: puzzle is unsolvable so we returning false
    return False


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(example_board)
    print(solve_sudoku(example_board))
    print(example_board)