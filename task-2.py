import math

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
AI = 'O'
PLAYER = 'X'

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board, player):
    for row in board:
        if all(spot == player for spot in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(spot != ' ' for row in board for spot in row)

def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):
        return 1
    elif check_winner(board, PLAYER):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = AI
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def player_move(board):
    while True:
        try:
            x = int(input("Enter your move [1-9]: ")) - 1
            row = x // 3
            col = x % 3
            if board[row][col] == ' ':
                board[row][col] = PLAYER
                break
            else:
                print("Invalid move, cell already occupied.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

def main():
    while True:
        print_board(board)

        if check_winner(board, PLAYER):
            print("Player wins!")
            break
        elif check_winner(board, AI):
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        player_move(board)

        if not is_full(board) and not check_winner(board, PLAYER):
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = AI

if __name__ == "__main__":
    main()
