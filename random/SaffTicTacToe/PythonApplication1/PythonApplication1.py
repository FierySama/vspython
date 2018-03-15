
board = [ ['X', 'X', 'O'], 
          ['X', 'X', 'O'], 
          ['O', 'O', 'O'] ]

def tictactoe(board):
    # check for invalid:
    var = abs(str(board).count('O') - str(board).count('X')) <= 1
    if not var:
        return print("Invalid")
    # check for horizontal wins
    if board[0][0] == board[0][1] == board[0][2] and not board[0][0] == " ":
        return print(board[0][0], "wins")
    elif board[1][0] == board[1][1] == board[1][2] and not board[1][0] == " ":
        return print(board[1][0], "wins")
    elif board[2][0] == board[2][1] == board[2][2] and not board[2][0] == " ":
        return print(board[2][0], "wins") 
    # check for vertical wins
    if board[0][0] == board[1][0] == board[2][0] and not board[0][0] == " ":
        return print(board[0][0], "wins") 
    elif board[0][1] == board[1][1] == board[2][1] and not board[0][1] == " ":
        return print(board[0][1], "wins") 
    elif board[0][2] == board[1][2] == board[2][2] and not board[0][2] == " ":
        return print(board[0][2], "wins")
    # check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] and not board[0][0] == " ":
        return print(board[0][0], "wins")
    elif board[0][2] == board[1][1] == board[2][0] and not board[0][2] == " ":
        return print(board[0][2], "wins")
    # check for draw
    if str(board).count(' ') == 8:
        return print("Draw")
    # check for ongoing
    if str(board).count(' ') > 8 and str(board).count(' ') <= 17:
        return print("Ongoing")

tictactoe(board)