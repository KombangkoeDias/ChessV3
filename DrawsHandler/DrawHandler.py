from side import side
from type import type

class DrawHandler:
    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.stalemate = False
        self.deadPosition = False
        self.mutualAgree = False # will not be implemented here
        self.fiftyMoves = False
        self.threeFoldRepetition = False

    def determineDraw(self):
        return (self.determineStaleMate(side.whiteside) or self.determineStaleMate(side.blackside)
                or self.determineDeadPosition() or self.determinefiftyMoves()
                or self.determineThreeFoldRepetition())

    def determineStaleMate(self,side):
        if (self.chessboard.evaluateCheckEngine.checkCheck(side)):
            return False
        for i in range(8):
            for j in range(8):
                currSquare = self.chessboard.getSquare(i,j)
                if(currSquare.Piece.side == side):
                    walkList = self.chessboard.evaluateMovesEngine.getFilteredPossibleWalks(currSquare)

                    if(len(walkList) > 0):
                        return False
                    else:
                        eatList = self.chessboard.evaluateMovesEngine.getFilteredPossibleEats(currSquare)
                        if(len(eatList) > 0):
                            return False
        print("Draw from ", side, "stalemate")
        return True

    def determineDeadPosition(self):
        # pretty hard to determine
        return False

    def determinefiftyMoves(self):
        if(len(self.chessboard.moves) > 50): # only when there are more than 50 moves stored
            for move in self.chessboard.moves[-50:]:
                # return false if the move is pawn move or it is eat move
                if(move.getFirstPiece().type == type.PawnB or move.getFirstPiece().type == type.PawnW):
                    return False
                if(move.IsEatMove()):
                    return False
        else:
            return False
        return True

    def determineThreeFoldRepetition(self):
        # still not working might skip the whole drawHandler
        if(len(self.chessboard.moves) >= 6):
            last6Moves = self.chessboard.moves[-6:]
            firstmove = last6Moves[0]
            secondmove = last6Moves[1]
            thirdmove = last6Moves[2]
            fourthmove = last6Moves[3]
            fifthmove = last6Moves[4]
            sixthmove = last6Moves[5]
            if (firstmove.getSecondSquare() == thirdmove.getFirstSquare() and thirdmove.getSecondSquare() == fifthmove.getFirstSquare() and
                    fifthmove.getSecondSquare() == firstmove.getFirstSquare()):
                if (secondmove.getSecondSquare() == fourthmove.getFirstSquare() and fourthmove.getSecondSquare() == sixthmove.getFirstSquare() and
                        sixthmove.getSecondSquare() == secondmove.getFirstSquare()):
                    return True
        return False