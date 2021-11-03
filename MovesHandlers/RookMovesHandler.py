from type import type
from side import side

class RookMovesHandler:
    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.possibleWalks = list()
        self.possibleEats = list()

    def findAllPossibleWalks(self,firstSquare):
        self.possibleWalks.clear() # clear the list first
        (row, col) = self.chessboard.findIJSquare(firstSquare)
        top = (row - 1, col)
        left = (row, col - 1)
        right = (row, col + 1)
        bottom = (row + 1, col)
        while (self.chessboard.checkIJInSquare(top[0], top[1]) and
               self.chessboard.getSquare(top[0], top[1]).Piece.type == type.Empty):
            self.possibleWalks.append(self.chessboard.getSquare(top[0], top[1]))
            top = (top[0] - 1, top[1])
        while (self.chessboard.checkIJInSquare(left[0], left[1]) and
               self.chessboard.getSquare(left[0], left[1]).Piece.type == type.Empty):
            self.possibleWalks.append(self.chessboard.getSquare(left[0], left[1]))
            left = (left[0], left[1] - 1)
        while (self.chessboard.checkIJInSquare(right[0], right[1]) and
               self.chessboard.getSquare(right[0], right[1]).Piece.type == type.Empty):
            self.possibleWalks.append(self.chessboard.getSquare(right[0], right[1]))
            right = (right[0], right[1] + 1)
        while (self.chessboard.checkIJInSquare(bottom[0], bottom[1]) and
               self.chessboard.getSquare(bottom[0], bottom[1]).Piece.type == type.Empty):
            self.possibleWalks.append(self.chessboard.getSquare(bottom[0], bottom[1]))
            bottom = (bottom[0] + 1, bottom[1])
        return self.possibleWalks
    def findAllPossibleEats(self,firstSquare):
        self.possibleEats.clear() # clear the list first
        (row, col) = self.chessboard.findIJSquare(firstSquare)
        top = (row - 1, col)
        left = (row, col - 1)
        right = (row, col + 1)
        bottom = (row + 1, col)
        while (self.chessboard.checkIJInSquare(top[0], top[1])):
            if (self.chessboard.getSquare(top[0], top[1]).Piece.type != type.Empty):
                topSquare = self.chessboard.getSquare(top[0], top[1])
                if (topSquare.Piece.side != firstSquare.Piece.side):
                    self.possibleEats.append(topSquare)
                break
            top = (top[0] - 1, top[1])

        while (self.chessboard.checkIJInSquare(left[0], left[1])):
            if (self.chessboard.getSquare(left[0], left[1]).Piece.type != type.Empty):
                leftSquare = self.chessboard.getSquare(left[0], left[1])
                if (leftSquare.Piece.side != firstSquare.Piece.side):
                    self.possibleEats.append(leftSquare)
                break
            left = (left[0], left[1] - 1)

        while (self.chessboard.checkIJInSquare(right[0], right[1])):
            if (self.chessboard.getSquare(right[0], right[1]).Piece.type != type.Empty):
                rightSquare = self.chessboard.getSquare(right[0], right[1])
                if (rightSquare.Piece.side != firstSquare.Piece.side):
                    self.possibleEats.append(rightSquare)
                break
            right = (right[0], right[1] + 1)

        while (self.chessboard.checkIJInSquare(bottom[0], bottom[1])):
            if (self.chessboard.getSquare(bottom[0], bottom[1]).Piece.type != type.Empty):
                bottomSquare = self.chessboard.getSquare(bottom[0], bottom[1])
                if (bottomSquare.Piece.side != firstSquare.Piece.side):
                    self.possibleEats.append(bottomSquare)
                break
            bottom = (bottom[0] + 1, bottom[1])
        return self.possibleEats