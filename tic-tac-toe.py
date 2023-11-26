import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def player_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == ' ':
                return row, col
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def ai_move(board):
    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        if check_winner(board, 'O'):
            return i, j
        board[i][j] = ' '

    for i, j in get_empty_cells(board):
        board[i][j] = 'X'
        if check_winner(board, 'X'):
            return i, j
        board[i][j] = ' '

    return random.choice(get_empty_cells(board))

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:
            print("\nPlayer's turn (X):")
            row, col = player_move(board)
        else:
            print("\nAI's turn (O):")
            row, col = ai_move(board)

        board[row][col] = 'X' if turn % 2 == 0 else 'O'
        print_board(board)

        if check_winner(board, 'X'):
            print("Player wins!")
            break
        elif check_winner(board, 'O'):
            print("AI wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    tic_tac_toe()
