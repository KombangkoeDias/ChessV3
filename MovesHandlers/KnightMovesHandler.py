from side import side
from type import type

class KnightMovesHandler:
    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.possibleEats = list()
        self.possibleWalks = list()
    def findAllPossibleWalks(self,firstSquare):
        self.possibleWalks.clear() # clear the results before evaluating
        (row,col) = self.chessboard.findIJSquare(firstSquare)
        allPossibleMoves = [(row-1,col-2),(row-1,col+2),(row+1,col-2),(row+1,col+2),(row-2,col+1),(row-2,col-1),(row+2,col+1),(row+2,col-1)]
        for move in allPossibleMoves:
            if (self.chessboard.checkIJInSquare(move[0],move[1]) and self.chessboard.getSquare(move[0],move[1]).Piece.side == side.noside ):
                self.possibleWalks.append(self.chessboard.getSquare(move[0],move[1]))
        return self.possibleWalks
    def findAllPossibleEats(self,firstSquare):
        self.possibleEats.clear() # clear the results before evaluating
        (row, col) = self.chessboard.findIJSquare(firstSquare)
        allPossibleMoves = [(row - 1, col - 2), (row - 1, col + 2), (row + 1, col - 2), (row + 1, col + 2),
                            (row - 2, col + 1), (row - 2, col - 1), (row + 2, col + 1), (row + 2, col - 1)]

        for move in allPossibleMoves:
            if (self.chessboard.checkIJInSquare(move[0], move[1]) and self.chessboard.getSquare(move[0], move[1]).Piece.side != side.noside
            and self.chessboard.getSquare(move[0],move[1]).Piece.side != firstSquare.Piece.side):
                self.possibleEats.append(self.chessboard.getSquare(move[0], move[1]))
        return self.possibleEats