# Solution to Chess Dictionary Validator practice problem from Ch. 5
#
# Chess piece names are written in the form of w-pawn, b-knight, etc.
#
# rqvl@runbox.com

# define some boards
validBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
invalidBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'wking', '9e': 'wknight'}

def validate(board):
  
    isValid = True
    
    # create chess board list the only way I know how
    validKeys = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    s = ''
    for i in range(1,9):
        for j in range(8):
            s = str(i) + letters[j]
            validKeys.append(s)
    
    # each has exactly one king
    numWhiteKing = 0
    numBlackKing = 0
    for k in board.values():
        if k == 'wking':
            numWhiteKing += 1
        if k == 'bking':
            numBlackKing += 1
            
    if (numWhiteKing > 1 or numBlackKing > 1): return False
        
    # at most 16 pieces
    numPieces = 0
    for k in board.values():
        numPieces += 1
        
    #print('the number of pieces on this board was ' + str(numPieces)) #for debug
    if numPieces > 16: return False
    
    # at most 8 pawns
    numWhitePawn = 0
    numBlackPawn = 0
    for k in board.values():
        if k == 'wpawn':
            numWhiteKing += 1
        if k == 'bpawn':
            numBlackKing += 1
    if (numWhitePawn > 8 or numBlackPawn > 8): return False # no need to continue testing
    
    # all pieces must be on a space from 1a to 8h
    for k in board.keys():
        if k not in validKeys:
            # print('invalid chess board position ' + str(k)) 
            return False
        
    # detect bug resulting in improper chess board // to do            
    return isValid

print((validate(validBoard)))
