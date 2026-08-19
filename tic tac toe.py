board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

print("Welcome to Tic Tac Toe!")
print("Board positions:")
print("1 | 2 | 3")
print("--|---|--")
print("4 | 5 | 6")
print("--|---|--")
print("7 | 8 | 9")


def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--|---|--")
    print(board[3], "|", board[4], "|", board[5])
    print("--|---|--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def winner(player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    if board[3] == player and board[4] == player and board[5] == player:
        return True
    if board[6] == player and board[7] == player and board[8] == player:
        return True
    if board[0] == player and board[3] == player and board[6] == player:
        return True
    if board[1] == player and board[4] == player and board[7] == player:
        return True
    if board[2] == player and board[5] == player and board[8] == player:
        return True
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True

    return False


player = "X"

while True:
    show_board()

    move = input("Player " + player + ", enter a position (1-9): ")

    if not move.isdigit():
        print("Please enter a number.")
        continue

    move = int(move)

    if move < 1 or move > 9:
        print("Choose a number between 1 and 9.")
        continue

    if board[move - 1] != " ":
        print("That spot is already taken.")
        continue

    board[move - 1] = player

    if winner(player):
        show_board()
        print("Player", player, "wins!")
        break

    if " " not in board:
        show_board()
        print("It's a draw!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"