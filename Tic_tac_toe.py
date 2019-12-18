#Tic Tac Toe game in python

# We have 10 empty values rather than 9 so that input can be taken 1-9 compared to reading it 0-8
board = [' ' for x in range(10)]

#Insert the player in the choosen position
def positionplayed(user, pos):
    board[pos] = user
    
#Function tells use if the space is occupied 
def empty_space(pos):
    return board[pos] == ' '

#Display the board as a parameter
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    
# win cross top,win cross middle,win cross bottom, win down left side, win down middle side,win down right side, win diagonal    
def win(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or  (bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le) 

def valid_move():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                # check if the choosen position is valid
                if empty_space(move):
                    run = False
                    positionplayed('X', move)
                else:
                    print('Position occupied!, select something different')
            else:
                print('only accept variables in the range')
        except:
            print('Your turn!')
            
#AI will examine the board and determine the best move
            # go for the winning move
            # stop player from using winning position
            # randomly choose available corners or edges
            # if available take center position
            # know when the game is a tie
def AI_move():
    possibleMoves = [x for x, user in enumerate(board) if user == ' ' and x != 0]
    move = 0
    #AI takes new position or block opp winning move
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if win(boardCopy, let):
                move = i
                return move
    #AI first wants to choose a corner
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    # Next AI want the center as its nxt choice
    if 5 in possibleMoves:
        move = 5
        return move
    # Take edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move
# AI will choose randomly
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def fullboard(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('lets play Tic Tac Toe!')
    printBoard(board)

    while not(fullboard(board)):
        if not(win(board, 'O')):
            valid_move()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not(win(board, 'X')):
            move = AI_move()
            if move == 0:
                print('Tie Game!')
            else:
                positionplayed('O', move)
                print('AI placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if fullboard(board):
        print('Tie Game!')

while True:
    answer = input('Want to play Tic Tac Toe against The AI? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
