N = 8

# Check if a queen can be placed safely
def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True

# Backtracking function
def solve_queens(board, row, solutions):
    if row == N:
        solutions.append(board[:])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_queens(board, row + 1, solutions)

# Main function
def eight_queens():
    board = [-1] * N
    solutions = []

    solve_queens(board, 0, solutions)

    return solutions

# Find all solutions
solutions = eight_queens()

print("Total Solutions:", len(solutions))

# Display first solution
print("\nOne Solution:")
for row in solutions[0]:
    line = ['.'] * N
    line[row] = 'Q'
    print(' '.join(line))
