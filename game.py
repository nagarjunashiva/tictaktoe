def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True

    for i in range(3):
        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    for _ in range(9):
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        while board[row][col] != " ":
            print("That cell is already taken. Try again.")
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        turn += 1
    else:
        print_board(board)
        print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
