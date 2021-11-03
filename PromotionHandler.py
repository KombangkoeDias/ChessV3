from side import side
from type import type
from UserInterface.ChessPiece import ChessPieces
from UserInterface.Square import Square
from UserInterface.Color import white,darkgreen
class PromotionHandler:
    def __init__(self,chessboard,screen):
        self.chessboard = chessboard
        # 4 choose squares
        self.myfirstSquare = None
        self.mysecondSquare = None
        self.mythirdSquare = None
        self.myfourthSquare = None
        self.promotionSquares = [self.myfirstSquare,self.mysecondSquare,self.mythirdSquare,self.myfourthSquare]
        self.choosePromotionSquare = None  # the player's choice of promotion
        self.putInSquare = None  # the pawn promotion square
        self.screen = screen  # screen passed from the chessbaord
    def determinePromotionSquares(self,side):
        if (side == side.whiteside):
            self.myfirstSquare = Square(900,20,70,70,white)
            self.mysecondSquare = Square(900,90,70,70,white)
            self.mythirdSquare = Square(900,160,70,70,white)
            self.myfourthSquare = Square(900,230,70,70,white)
            # update the promotionSquares list
            self.promotionSquares = [self.myfirstSquare, self.mysecondSquare, self.mythirdSquare, self.myfourthSquare]
        if (side == side.blackside):
            self.myfirstSquare = Square(900, 20, 70, 70, darkgreen)
            self.mysecondSquare = Square(900, 90, 70, 70, darkgreen)
            self.mythirdSquare = Square(900, 160, 70, 70, darkgreen)
            self.myfourthSquare = Square(900, 230, 70, 70, darkgreen)
            # update the promotionSquares list
            self.promotionSquares = [self.myfirstSquare, self.mysecondSquare, self.mythirdSquare, self.myfourthSquare]

    def drawChooose(self,side):
        """Draw the promotion choice squares according to side"""
        # add corresponding piece
        if(side == side.whiteside):
            Queen = ChessPieces('Assets\Pieces\whiteQueen.png', (910, 30), type.QueenW, 0, side.whiteside)
            Rook = ChessPieces('Assets\Pieces\whiteRook.png', (910, 100), type.RookW, 0, side.whiteside)
            Bishop = ChessPieces('Assets\Pieces\whiteBishop.png', (910, 170), type.BishopW, 0, side.whiteside)
            Knight = ChessPieces('Assets\Pieces\whiteKnight.png', (910, 240), type.KnightW, 0, side.whiteside)
        if(side == side.blackside):
            Queen = ChessPieces('Assets\Pieces/blackQueen.png', (910, 30), type.QueenB, 0, side.blackside)
            Rook = ChessPieces('Assets\Pieces/blackRook.png', (910, 100), type.RookB, 0, side.blackside)
            Bishop = ChessPieces('Assets\Pieces/blackBishop.png', (910, 170), type.BishopB, 0, side.blackside)
            Knight = ChessPieces('Assets\Pieces/blackKnight.png', (910, 240), type.KnightB, 0, side.blackside)
        # add piece to the choice squares
        self.myfirstSquare.addPieces(Queen)
        self.mysecondSquare.addPieces(Rook)
        self.mythirdSquare.addPieces(Bishop)
        self.myfourthSquare.addPieces(Knight)

        # draw square
        self.myfirstSquare.drawSquare(self.screen, select=False, eat=False, check=False)
        self.mysecondSquare.drawSquare(self.screen, select=False, eat=False, check=False)
        self.mythirdSquare.drawSquare(self.screen, select=False, eat=False, check=False)
        self.myfourthSquare.drawSquare(self.screen, select=False, eat=False, check=False)

        # draw piece
        self.screen.blit(Knight.image, Knight.rect)
        self.screen.blit(Bishop.image, Bishop.rect)
        self.screen.blit(Rook.image, Rook.rect)
        self.screen.blit(Queen.image, Queen.rect)

    def detectClick(self):
        """Detect if any of the choice square is clicked"""
        for square in self.promotionSquares:
            if(square.getclick()):
                self.choosePromotionSquare = square  # add it to the choosePromotionSquare field

    def findPromotionSquare(self):
        """Find if there's promotion"""
        promotion = False
        i = 0
        for j in range(8):
            if (self.chessboard.getSquare(i, j).Piece.type == type.PawnW):  # for white promotion
                self.chessboard.promotion = side.whiteside  # update the chessboard's promotion field
                self.chessboard.boardActive = False  # make board inactive
                self.putInSquare = self.chessboard.getSquare(i,j)  # update the pawn promotion square
                promotion = True
                print("promotion white")
                break

        i = 7
        for j in range(8):
            if (self.chessboard.getSquare(i, j).Piece.type == type.PawnB):  # for black promotion
                self.chessboard.promotion = side.blackside  # update the chessboard's promotion field
                self.chessboard.boardActive = False  # make board inactive
                self.putInSquare = self.chessboard.getSquare(i, j)  # update the pawn promotion square
                promotion = True
                print("promotion black")
                break
        if (not promotion):  # if neither white or black promotion occurred we update these values
            self.chessboard.promotion = False  # update the chessboard's promotion field to False
            self.putInSquare = None  # update the pawn promotion square


