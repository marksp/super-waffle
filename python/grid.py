board = []

for row in range(3):
    board.append([])
    for column in range(3):
        board[row].append('x')

print(board)

def print_board(board):
    for row in board:
        print (" ".join(row))

print_board(board)