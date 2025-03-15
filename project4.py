def print_board(board):
    """
    Prints the current state of the tic-tac-toe board.
    
    Args:
        board: A 3x3 list representing the board state
    """
    for i, row in enumerate(board):
        row_str = " "  # Initialize string with a space
        for j, value in enumerate(row):
            row_str += value  # Add the cell value (X, O, or space)
            if j != len(row) - 1:  # If not the last column
                row_str += " | "  # Add separator between columns
        
        print(row_str)  # Print the formatted row
        if i != len(board) - 1:  # If not the last row
            print("---------")  # Print horizontal divider

def get_move(turn, board):
    """
    Get and validate player move, then update the board.
    
    Args:
        turn: Current player's symbol ('X' or 'O')
        board: The game board to update
    """
    while True:  # Loop until a valid move is entered
        row = int(input("Row: "))  # Get row input (1-3)
        col = int(input("Col: "))  # Get column input (1-3)
        
        # Validate the move - check if row is in range
        if row < 1 or row > len(board):
            print("Invalid row, try again")
        # Check if column is in range
        elif col < 1 or col > len(board[row - 1]):
            print("Invalid col, try again")
        # Check if the position is already taken
        elif board[row - 1][col - 1] != " ":
            print("Already taken, try again")
        else:
            break  # Valid move, exit the loop
        
    # Update the board with the player's symbol (X or O)
    board[row - 1][col - 1] = turn
    

def check_win(board, turn):
    """
    Check if the current player has won.
    
    Args:
        board: The game board
        turn: Current player's symbol ('X' or 'O')
    
    Returns:
        bool: True if the player has won, False otherwise
    """
    # Define all possible winning lines (rows, columns, diagonals)
    lines = [ 
        [(0, 0), (0, 1), (0, 2)],  # Top row
        [(1, 0), (1, 1), (1, 2)],  # Middle row
        [(2, 0), (2, 1), (2, 2)],  # Bottom row
        [(0, 0), (1, 0), (2, 0)],  # Left column
        [(0, 1), (1, 1), (2, 1)],  # Middle column
        [(0, 2), (1, 2), (2, 2)],  # Right column
        [(0, 0), (1, 1), (2, 2)],  # Diagonal from top-left
        [(0, 2), (1, 1), (2, 0)],  # Diagonal from top-right
    ]
    
    # Check each winning line
    for line in lines:
        win = True  # Assume win until we find a mismatch
        for pos in line:
            row, col = pos  # Unpack the position tuple
            if board[row][col] != turn:  # If any position doesn't match the player's symbol
                win = False  # Not a win
                break
            
        if win:  # If we checked all positions and found a win
            return True
    
    return False  # No winning lines found
    
# Initialize an empty 3x3 board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

turn = "X"  # Start with player X (note: code has a bug here, initializes as "A")
turn_number = 0  # Track number of turns taken
print_board(board)  # Display initial empty board

# Main game loop - maximum 9 turns possible
while turn_number < 9:
    print()
    print("It is the", turn, "player's turn. Please select your move")
    
    get_move(turn, board)  # Get and validate player move
    
    print_board(board)  # Display updated board
    winner = check_win(board, turn)  # Check if current player won
    
    if winner:  # If we have a winner
        break  # Exit the loop
    
    # Switch to the other player
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    turn_number += 1  # Increment turn counter
    
# End of game - display result
if turn_number == 9:  # If all 9 moves were made without a winner
    print("Tied game.")
else:  # If we have a winner
    print("The winner was", turn)