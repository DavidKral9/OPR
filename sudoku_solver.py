def print_board(board):
    """Print the Sudoku board in a readable format."""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Separator between 3x3 blocks

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Separator between columns

            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end=" ")

def is_valid(board, num, pos):
    """
    Check if a number can be placed at a specific position on the Sudoku board.
    Parameters:
    - board: Current Sudoku board (9x9 matrix).
    - num: Number to be placed (1-9).
    - pos: Tuple (row, col) representing the position on the board.
    """
    row, col = pos

    # Check row
    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    # Check 3x3 block
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(board):
    """
    Find the first empty cell on the Sudoku board.
    Returns: Tuple (row, col) of the empty cell or None if the board is full.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # Return position of empty cell

    return None

def solve_sudoku(board):
    """
    Recursively solve the Sudoku puzzle using the backtracking algorithm.
    Returns True if the puzzle is solved, otherwise False.
    """
    empty = find_empty(board)
    if not empty:
        return True  # The board is complete

    row, col = empty

    for num in range(1, 10):  # Numbers 1 to 9
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):  # Recursive call
                return True

            board[row][col] = 0  # Backtrack, reset the cell

    return False

def is_solvable(board):
    """
    Check if the given Sudoku board is solvable.
    This is done by ensuring no row, column, or 3x3 block has duplicate numbers
    and the puzzle has at least one solution.
    """
    # Check if the board violates Sudoku rules
    for row in range(len(board)):
        for col in range(len(board[0])):
            num = board[row][col]
            if num != 0:  # Ignore empty cells
                board[row][col] = 0  # Temporarily remove the number
                if not is_valid(board, num, (row, col)):
                    return False
                board[row][col] = num  # Restore the number

    # Check if the puzzle has at least one solution
    copy_board = [row[:] for row in board]  # Create a copy of the board
    return solve_sudoku(copy_board)

# example of sudoku board
board = [
    [0, 0, 2, 7, 8, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 9, 8, 0, 1],
    [4, 0, 0, 0, 0, 3, 0, 7, 0],
    [9, 0, 5, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 4, 0, 8],
    [0, 6, 0, 4, 0, 0, 0, 0, 7],
    [3, 0, 9, 8, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 3, 0, 6, 0, 0]
]

print("Original Sudoku puzzle:")
print_board(board)

if is_solvable(board):
    print("\nThe Sudoku puzzle is solvable. Solving...")
    solve_sudoku(board)
    print("\nSolved Sudoku puzzle:")
    print_board(board)
else:
    print("\nThe Sudoku puzzle is not solvable.")