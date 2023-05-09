def draw_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_winner(board):
    # check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != ' ':
            return board[i]

    # check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return board[i]

    # check diagonals
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return board[2]

    # check if the board is full
    if ' ' not in board:
        return 'Tie'

    # no winner yet
    return None

def play_game():
    board = [' ']*9
    players = ['X', 'O']
    current_player = players[0]
    winner = None

    while not winner:
        draw_board(board)

        move = input(f"Player {current_player}, enter a move (1-9): ")

        index = int(move) - 1
        if board[index] == ' ':
            board[index] = current_player
            winner = check_winner(board)
            current_player = players[(players.index(current_player) + 1) % 2]
        else:
            print("That space is already taken. Try again.")

    # display final board and winner
    draw_board(board)
    if winner == 'Tie':
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")


play_game()