# Solution to Chess Dictionary Validator practice problem from Ch. 5
#
# Chess piece names are written in the form of w-pawn, b-knight, etc.
#
# rqvl@runbox.com

# define some boards
validBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
invalidBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'wking', '9e': 'wknight'}

def validate(board):
    
    validKeys = ['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h',
                 '2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h',
                 '3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h',
                 '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h',
                 '5a', '5b', '5c', '5d', '1e', '5f', '5g', '5h',
                 '6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h',
                 '7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h',
                 '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h',]
    
    isValid = True
    
    # each has exactly one king
    numWhiteKing = 0
    numBlackKing = 0
    for k in board.values():
        if k == 'wking':
            numWhiteKing += 1
        if k == 'bking':
            numBlackKing += 1
            
    if (numWhiteKing > 1 or numBlackKing > 1):
        return False # no need to continue testing
        
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
    if (numWhitePawn > 8 or numBlackPawn > 8):
        return False # no need to continue testing
    
    # all pieces must be on a space from 1a to 8h
    for k in board.keys():
        if k not in validKeys:
            # print('invalid chess board position ' + str(k)) 
            return False
        
    # detect bug resulting in improper chess board // to do
            
    return isValid

print((validate(invalidBoard)))
