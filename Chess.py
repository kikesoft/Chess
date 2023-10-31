def create_board():
    board = []
    for _ in range(8):
        row = []
        for _ in range(8):
            row.append(".")
        board.append(row)
    return board

def add_pieces_to_board(board):
    # Define the position of the pieces
    positions = ["rnbqkbnr", "pppppppp", "........", "........", "........", "........", "PPPPPPPP", "RNBQKBNR"]
    
    # Add the pieces to the board
    for i in range(8):
        for j in range(8):
            board[i][j] = positions[i][j]
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

board = create_board()
board = add_pieces_to_board(board)
print_board(board)
