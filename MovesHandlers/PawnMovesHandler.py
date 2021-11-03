from type import type
from side import side
from PromotionHandler import PromotionHandler

class PawnMovesHandler:
    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.possibleWalks = list()
        self.possibleEats = list()
    def findAllPossibleWalks(self,firstSquare):
        self.possibleWalks.clear()  # clear the list first
        (row, col) = self.chessboard.findIJSquare(firstSquare)
        if (firstSquare.Piece.type == type.PawnW): # for white
            one_step_square = self.chessboard.getSquare(row-1,col)
            if (row == 6):
                two_step_square = self.chessboard.getSquare(row - 2, col)
                if (one_step_square.Piece.type == type.Empty):
                    self.possibleWalks.append(one_step_square)
                    if (two_step_square.Piece.type == type.Empty):
                        self.possibleWalks.append(two_step_square)
            else:
                if (one_step_square.Piece.type == type.Empty):
                    self.possibleWalks.append(one_step_square)

        if (firstSquare.Piece.type == type.PawnB): # for black
            one_step_square = self.chessboard.getSquare(row + 1, col)
            if (row == 1):
                two_step_square = self.chessboard.getSquare(row + 2, col)
                if (one_step_square.Piece.type == type.Empty):
                    self.possibleWalks.append(one_step_square)
                    if (two_step_square.Piece.type == type.Empty):
                        self.possibleWalks.append(two_step_square)
            else:
                if (one_step_square.Piece.type == type.Empty):
                    self.possibleWalks.append(one_step_square)
        return self.possibleWalks
    def findAllPossibleEats(self,firstSquare):
        self.possibleEats.clear()  # clear the list first
        (row, col) = self.chessboard.findIJSquare(firstSquare)
        if (firstSquare.Piece.type == type.PawnW): # for white
            if (self.chessboard.checkIJInSquare(row-1,col-1)): # check if it's in the square before creating
                left_eat_square = self.chessboard.getSquare(row-1,col-1)
                if (left_eat_square.Piece.side == side.blackside): # and if that square's piece is opponent's add it to eat list
                    self.possibleEats.append(left_eat_square)
            if (self.chessboard.checkIJInSquare(row-1,col+1)): # check if it's in the square before creating
                right_eat_square = self.chessboard.getSquare(row - 1, col + 1)
                if (right_eat_square.Piece.side == side.blackside): # and if that square's piece is opponent's add it to eat list
                    self.possibleEats.append(right_eat_square)
        if firstSquare.Piece.type == type.PawnB: # for black
            if (self.chessboard.checkIJInSquare(row+1,col-1)): # check if it's in the square before creating
                left_eat_square = self.chessboard.getSquare(row + 1, col - 1)
                if (left_eat_square.Piece.side == side.whiteside): # and if that square's piece is opponent's add it to eat list
                    self.possibleEats.append(left_eat_square)
            if (self.chessboard.checkIJInSquare(row+1,col+1)): # check if it's in the square before creating
                right_eat_square = self.chessboard.getSquare(row + 1, col + 1)
                if (right_eat_square.Piece.side == side.whiteside): # and if that square's piece is opponent's add it to eat list
                    self.possibleEats.append(right_eat_square)
        self.findEnPassant(firstSquare) # add more to possibleEats for En Passant
        return self.possibleEats

    def findEnPassant(self,firstSquare):
        """ This function detects en passant possibilities and add it to self.possibleEats """
        (row,col) = self.chessboard.findIJSquare(firstSquare) # get row and column of the chosen pawn.

        if (firstSquare.Piece.side == side.whiteside): # for white
            if (self.chessboard.findIJSquare(firstSquare)[0] == 3): # for white side it's only possible when the pawn is at row 3
                piece = self.chessboard.moves[-1].getFirstPiece()
                (firstlast1, firstlast2) = self.chessboard.findIJSquare(self.chessboard.moves[-1].getFirstSquare())
                (secondlast1, secondlast2) = self.chessboard.findIJSquare(self.chessboard.moves[-1].getSecondSquare())
                # the condition for the last move is that the opponent adjacent-column pawn is just move 2 steps
                if (firstlast1 == row-2 and secondlast1 == row and (firstlast2 == col + 1 or firstlast2 == col - 1)
                        and piece.type == type.PawnB):
                    self.possibleEats.append(self.chessboard.getSquare(row - 1, firstlast2)) # so we add the en passant square to the eatlist
        else: # for black
            if (self.chessboard.findIJSquare(firstSquare)[0] == 4):# for white side it's only possible when the pawn is at row 4
                piece = self.chessboard.moves[-1].getFirstPiece()
                (firstlast1, firstlast2) = self.chessboard.findIJSquare(self.chessboard.moves[-1].getFirstSquare())
                (secondlast1, secondlast2) = self.chessboard.findIJSquare(self.chessboard.moves[-1].getSecondSquare())
                # the condition for the last move is that the opponent adjacent-column pawn is just move 2 steps
                if (firstlast1 == row+2 and secondlast1 == row and (firstlast2 == col + 1 or firstlast2 == col - 1)
                        and piece.type == type.PawnW):
                    self.possibleEats.append(self.chessboard.getSquare(row + 1, firstlast2)) # so we add the en passant square to the eatlist




