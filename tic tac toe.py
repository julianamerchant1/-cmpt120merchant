# CMPT 120 Intro to Programming
# Lab #7 – Lists and Error Handling
# Author: JULIANA MERCHANT
# Created: 2018-24-18
symbol = [ " ", "x", "o" ]
def printRow(row):
    # initialize output to the left border
    sRow = '|'
    for i in range(3):
        sRow += ' ' + symbol[row[i]] + ' |'
    print(sRow)
    # for each square in the row...
    # add to output the symbol for this square followed by a border
    # print the completed output for this row
    pass
def printBoard(board):
    # print the top border
    print('+-----------+')
    # for each row in the board...
    for i in range(3):
        printRow(board[i])
        print('+-----------+')
# print the row
# print the next border

#done ^^^

    pass
def markBoard(board, row, col, player):
# check to see whether the desired square is blank
# if so, set it to the player number
    #pass
    if board[row][col] == 0:
        board[row][col] = player
        
def getPlayerMove():
    #input("Input X or O [___] :") # prompt the user separately for the row and column numbers
    #return (0,0) # then return that row and column instead of (0,0)
    row = int(input("Enter row number: "))
    col = int(input("Enter column number: "))
    return row, col

def hasBlanks(board):
    # for each row in the board...
    # for each square in the row...
    # check whether the square is blank
    # if so, return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return True
    return False
#    if []: #not working, should this be a 'for i in' statement?
#        return True
#    else:
#        return False # if no square is blank, return False
def main():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn
main()
