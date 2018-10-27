#JULIANA MERCHANT
#PYTHON PROGRAMMING 101
#PROF ARIAS

board - [[0,0,0],[0,0,0],[0,0,0]]
symbol = [ " ", "x", "o" ]
def printRow(row):
    print("|", end=" ")
    for j in range(len(board[1])):
        print(" " + symbol[row[j]] +
        "|, end = " ")
              print("end='\n")
        pass
def printBoard(board):
              print("+-----------+")
              for i in range(len(board[1])):
              printRow(board[i])
              print("+-----------+")
               pass
def markBoard(board, row, col, player player):
    if board[row][col]==0"
    board[row][col]= player
    else:
        print ("that space isnt available!" )
            player = player % + 1
pass
def GetPlayerMove():
    col = int (("pick your column!" ))
    row = int(input(print("pick your row! ))
    return (row,col)

def hasBlanks(board):
    isBlack = False
    for i in range (len(board[1])):
        for j in range
(len(baord[1])):
            if board[1][j]==0:
                    isblank = True
                    return isBlank
def main():
    player = 1
    while hasblanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markboard(board, row, col, player)
    player = player * 2 + 1
print("thanks for playing tic tac toe!" )
main ()
