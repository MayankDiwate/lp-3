def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")


def is_safe(board, row, col, n):
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Check upper diagonal on right side
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    # Base case: If all queens are placed
    if row >= n:
        return True
    
    # Try placing a queen in each column in the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the queen

            # Recur to place the rest of the queens
            if solve_n_queens(board, row + 1, n):
                return True
            
            # If placing queen in board[row][col] doesn't lead to a solution, backtrack
            board[row][col] = 0

    return False


# Main function to initialize the board and get user input
def main():
    # Get board size from the user
    n = int(input("Enter the size of the board (n x n): "))

    # Initialize an empty n x n board
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Get the position for the first queen
    row = int(input("Enter the row index for the first queen (0-based): "))
    col = int(input("Enter the column index for the first queen (0-based): "))

    # Check if the position is valid
    if 0 <= row < n and 0 <= col < n:
        # Place the first queen on the board
        board[row][col] = 1
        print("Board after placing the first queen:")
        print_board(board)
        
        # Solve the rest of the board starting from the next row
        if solve_n_queens(board, row + 1, n):
            print("Solution found:")
            print_board(board)
        else:
            print("No solution exists.")
    else:
        print("Invalid position for the first queen.")

# Run the main function
main()