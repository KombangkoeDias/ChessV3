
class Moves:
    def __init__(self,firstSquare, firstPiece, secondSquare, secondPiece, enPassant,castling,eatmove):
        self.firstSquare = firstSquare
        self.firstPiece = firstPiece
        self.secondSquare = secondSquare
        self.secondPiece = secondPiece
        self.enPassant = enPassant
        self.castling = castling
        self.eatmove = eatmove # determine if the move is eating move.

    def getFirstSquare(self):
        return self.firstSquare
    def getSecondSquare(self):
        return self.secondSquare
    def getFirstPiece(self):
        return self.firstPiece
    def getSecondPiece(self):
        return self.secondPiece
    def getEnpassant(self):
        return self.enPassant
    def getCastling(self):
        return self.castling
    def IsEatMove(self):
        return self.eatmove