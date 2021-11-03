import enum

class castlingtype(enum.Enum):
    blackLeftCastling = "black left castling"
    blackRightCastling = "black right castling"
    whiteLeftCastling = "white left castling"
    whiteRightCastling = "white right castling"
    noCastling = "not castling"

def findCastlingType(chessboard,firstSquare,secondSquare):
    row1,col1 = chessboard.findIJSquare(firstSquare)
    row2,col2 = chessboard.findIJSquare(secondSquare)
    if (row1 == row2 == 0 and col2 == 2):
        return castlingtype.blackRightCastling
    elif(row1 == row2 == 0 and col2 == 6):
        return castlingtype.blackLeftCastling
    elif(row1 == row2 == 7 and col2 == 2):
        return castlingtype.whiteLeftCastling
    elif(row1 == row2 == 7 and col2 == 6):
        return castlingtype.whiteRightCastling
