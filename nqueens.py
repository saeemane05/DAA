# N-Queens Problem

n = int(input("Enter board size: "))
first_col = int(input("Enter column for first queen: "))

board = []

for i in range(n):
    row = []

    for j in range(n):
        row.append(0)

    board.append(row)


board[0][first_col - 1] = 1


# Check whether queen can be placed
def is_safe(row, col):

    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:

        if board[i][j] == 1:
            return False

        i = i - 1
        j = j - 1

    # Check right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:

        if board[i][j] == 1:
            return False

        i = i - 1
        j = j + 1

    return True


# Solve using backtracking
def solve(row):

    if row == n:
        return True

    for col in range(n):

        if is_safe(row, col):

            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False


# Output
if solve(1):

    print("Solution:")

    for row in board:
        print(row)

else:
    print("No solution exists.")