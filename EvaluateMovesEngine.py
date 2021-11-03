from type import type
from side import side
from MovesHandlers.PawnMovesHandler import PawnMovesHandler
from MovesHandlers.KnightMovesHandler import KnightMovesHandler
from MovesHandlers.BishopMovesHandler import BishopMovesHandler
from MovesHandlers.RookMovesHandler import RookMovesHandler
from MovesHandlers.QueenMovesHandler import QueenMovesHandler
from MovesHandlers.KingMovesHandler import KingMovesHandler

class EvaluateMovesEngine:
    def __init__(self, chessboard,evaluateCheckEngine):
        self.chessboard = chessboard
        self.PawnMovesHandler = PawnMovesHandler(chessboard)
        self.KnightMovesHandler = KnightMovesHandler(chessboard)
        self.BishopMovesHandler = BishopMovesHandler(chessboard)
        self.RookMovesHandler = RookMovesHandler(chessboard)
        self.QueenMovesHandler = QueenMovesHandler(chessboard)
        self.KingMovesHandler = KingMovesHandler(chessboard)
        self.evaluateCheckEngine = evaluateCheckEngine
        self.handlers = [self.PawnMovesHandler,self.KnightMovesHandler,self.BishopMovesHandler,self.RookMovesHandler,
                         self.QueenMovesHandler,self.KingMovesHandler]
    def evaluateMove(self,firstSquare,secondSquare):
        possiblewalks = self.getFilteredPossibleWalks(firstSquare)
        possibleeats = self.getFilteredPossibleEats(firstSquare)
        if (secondSquare in possiblewalks or secondSquare in possibleeats):
            return True
        else:
            return False
    def clearResult(self):
        self.PawnMovesHandler.possibleWalks.clear()
        self.PawnMovesHandler.possibleEats.clear()
        self.KnightMovesHandler.possibleWalks.clear()
        self.KnightMovesHandler.possibleEats.clear()
        self.BishopMovesHandler.possibleWalks.clear()
        self.BishopMovesHandler.possibleEats.clear()
        self.RookMovesHandler.possibleWalks.clear()
        self.RookMovesHandler.possibleEats.clear()
        self.QueenMovesHandler.possibleWalks.clear()
        self.QueenMovesHandler.possibleEats.clear()
        self.KingMovesHandler.possibleWalks.clear()
        self.KingMovesHandler.possibleEats.clear()
    def getPossibleWalks(self,firstSquare):
        possiblewalks = list()
        if (firstSquare.Piece.type == type.PawnW or firstSquare.Piece.type == type.PawnB):
            possiblewalks = self.PawnMovesHandler.findAllPossibleWalks(firstSquare)
        elif (firstSquare.Piece.type == type.KnightW or firstSquare.Piece.type == type.KnightB):
            possiblewalks = self.KnightMovesHandler.findAllPossibleWalks(firstSquare)
        elif (firstSquare.Piece.type == type.BishopW or firstSquare.Piece.type == type.BishopB):
            possiblewalks = self.BishopMovesHandler.findAllPossibleWalks(firstSquare)
        elif (firstSquare.Piece.type == type.RookW or firstSquare.Piece.type == type.RookB):
            possiblewalks = self.RookMovesHandler.findAllPossibleWalks(firstSquare)
        elif (firstSquare.Piece.type == type.QueenW or firstSquare.Piece.type == type.QueenB):
            possiblewalks = self.QueenMovesHandler.findAllPossibleWalks(firstSquare)
        elif (firstSquare.Piece.type == type.KingW or firstSquare.Piece.type == type.KingB):
            possiblewalks = self.KingMovesHandler.findAllPossibleWalks(firstSquare)
        return possiblewalks
    def getPossibleEats(self,firstSquare):
        possibleeats = list()
        if (firstSquare.Piece.type == type.PawnW or firstSquare.Piece.type == type.PawnB):
            possibleeats = self.PawnMovesHandler.findAllPossibleEats(firstSquare)
        elif (firstSquare.Piece.type == type.KnightW or firstSquare.Piece.type == type.KnightB):
            possibleeats = self.KnightMovesHandler.findAllPossibleEats(firstSquare)
        elif (firstSquare.Piece.type == type.BishopW or firstSquare.Piece.type == type.BishopB):
            possibleeats = self.BishopMovesHandler.findAllPossibleEats(firstSquare)
        elif (firstSquare.Piece.type == type.RookW or firstSquare.Piece.type == type.RookB):
            possibleeats = self.RookMovesHandler.findAllPossibleEats(firstSquare)
        elif (firstSquare.Piece.type == type.QueenW or firstSquare.Piece.type == type.QueenB):
            possibleeats = self.QueenMovesHandler.findAllPossibleEats(firstSquare)
        elif (firstSquare.Piece.type == type.KingW or firstSquare.Piece.type == type.KingB):
            possibleeats = self.KingMovesHandler.findAllPossibleEats(firstSquare)
        return possibleeats
    def getFilteredPossibleWalks(self,firstSquare):
        """This function return all possible walks for the piece in the firstSquare parameter
        :param firstSquare the square to determine all walks"""
        return self.evaluateCheckEngine.filterWalks(self.getPossibleWalks(firstSquare),firstSquare)
    def getFilteredPossibleEats(self,firstSquare):
        """This function return all possible eats for the piece in the firstSquare parameter
        :param firstSquare the square to determine all eats"""
        return self.evaluateCheckEngine.filterEats(self.getPossibleEats(firstSquare),firstSquare)


