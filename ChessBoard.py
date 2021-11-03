import pygame
from UserInterface.Color import lightSquare,darkSquare,green
from type import type
from side import side
from UserInterface.Square import Square
from UserInterface.ChessPiece import ChessPieces
from EvaluateMovesEngine import EvaluateMovesEngine
from MovesHandlers.evaluateCheck import EvaluateCheck
from MovesHandlers.KingMovesHandler import CastlingMovesHandler
from Moves import Moves
from castling import castlingtype,findCastlingType
from PromotionHandler import PromotionHandler
from UserInterface.DrawButtons import drawReverseMoveButton,drawBackButton
from DrawsHandler.DrawHandler import DrawHandler
from Mode import mode
from OpponentMovesEngine import OpponentMovesEngine, opposite
from stockfishIntegrationEngine import stockfishIntegrationEngine

class Board:
    def __init__(self,screen,GameMode,mainMenuFunc,PlayerSide):
        """ initialize the ChessBoard """
        self.Squarelist = list() # Squarelist will hold the list of rows of Squares.
        self.clicklist = list() # clicklist will hold the chosen Square and Destination Square.
        self.screen = screen # the screen passed from UI.py
        self.InitializeBoard() # call to set up the board
        self.boardActive = True
        self.possibleWalks = list() # the list to store possible walk squares
        self.possibleEats = list() # the list to store possible eat squares
        self.moves = list() # list to store all the moves taken
        self.evaluateCheckEngine = EvaluateCheck(self)
        self.evaluateMovesEngine = EvaluateMovesEngine(self,self.evaluateCheckEngine)  # the class that call the handlers to evaluate the moves.
        self.whiteischecked = False
        self.blackischecked = False
        self.BlackKingCastlingHandler = CastlingMovesHandler(side.blackside,self)  # the class handling castling
        self.WhiteKingCastlingHandler = CastlingMovesHandler(side.whiteside,self)  # the class handling castling
        self.promotion = False
        self.promotionHandler = PromotionHandler(self,self.screen)
        self.DrawHandler = DrawHandler(self)
        if(GameMode == mode.TwoPlayer):
            self.currentSide = side.whiteside
        else:
            self.currentSide = PlayerSide
        self.GameMode = GameMode
        self.mainMenuFunc = mainMenuFunc
        self.opponentMovesEngine = OpponentMovesEngine(depth=5,chessboard=self)
        self.stockfishIntegrationEngine = stockfishIntegrationEngine(self)
    def InitializeBoard(self):
        """ return the initialized board as SquareList"""
        self.Squarelist = list() # make it a list
        for i in range(8):
            mylist = list()
            self.Squarelist.append(mylist)  # create rows
        for i in range(8):
            for j in range(8):
                if ((i + j) % 2 == 0): # we need to do this to add color to be like chess board.
                    newSquare = Square(220 + 70 * j, 30 + 70 * i, 70, 70, lightSquare)  # the location of each of the square.
                    piecelocation = (newSquare.x + 10, newSquare.y + 10)  # the location of each piece.
                    # add empty to every square first.
                    newSquare.addPieces(ChessPieces('Assets\Pieces\empty.png', piecelocation, type.Empty, None, side.noside))
                    # then change it if it's the case.

                    if (i == 1):
                        newSquare.addPieces(
                            ChessPieces('Assets/Pieces/blackPawn.png', piecelocation, type.PawnB, j, side.blackside))

                    if (i == 0):

                        if (j == 0):
                            newSquare.addPieces(
                                ChessPieces('Assets/Pieces/blackRook.png', piecelocation, type.RookB, 0, side.blackside))
                        if (j == 2):
                            newSquare.addPieces(
                                ChessPieces('Assets/Pieces/blackBishop.png', piecelocation, type.BishopB, 0, side.blackside))

                        if (j == 4):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces/blackKing.png', piecelocation, type.KingB, 0, side.blackside))

                        if (j == 6):
                            newSquare.addPieces(
                                ChessPieces('Assets/Pieces/blackKnight.png', piecelocation, type.KnightB, 1, side.blackside))

                    if (i == 6):
                        newSquare.addPieces(
                            ChessPieces('Assets\Pieces\whitePawn.png', piecelocation, type.PawnW, j, side.whiteside))
                    if (i == 7):
                        if (j == 1):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteKnight.png', piecelocation, type.KnightW, 0, side.whiteside))
                        if (j == 3):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteQueen.png', piecelocation, type.QueenW, 0, side.whiteside))
                        if (j == 5):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteBishop.png', piecelocation, type.BishopW, 1, side.whiteside))
                        if (j == 7):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteRook.png', piecelocation, type.RookW, 1, side.whiteside))
                    self.Squarelist[i].append(newSquare)
                else:
                    # the same just another half.
                    newSquare = Square(220 + 70 * j, 30 + 70 * i, 70, 70, darkSquare)
                    piecelocation = (newSquare.x + 10, newSquare.y + 10)
                    newSquare.addPieces(ChessPieces('Assets\Pieces\empty.png', piecelocation, type.Empty, None, side.noside))

                    if (i == 1):
                        newSquare.addPieces(
                            ChessPieces('Assets/Pieces/blackPawn.png', piecelocation, type.PawnB, j, side.blackside))
                    if (i == 0):
                        if (j == 1):
                            newSquare.addPieces(
                                ChessPieces('Assets/Pieces/blackKnight.png', piecelocation, type.KnightB, 0, side.blackside))
                        if (j == 3):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces/blackQueen.png', piecelocation, type.QueenB, 0, side.blackside))
                        if (j == 5):
                            newSquare.addPieces(
                                ChessPieces('Assets/Pieces/blackBishop.png', piecelocation, type.BishopB, 1, side.blackside))
                        if (j == 7):
                            newSquare.addPieces(
                                ChessPieces('Assets/Pieces/blackRook.png', piecelocation, type.RookB, 1, side.blackside))

                    if (i == 6):
                        newSquare.addPieces(
                            ChessPieces('Assets\Pieces\whitePawn.png', piecelocation, type.PawnW, j, side.whiteside))
                    if (i == 7):
                        if (j == 0):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteRook.png', piecelocation, type.RookW, 0, side.whiteside))
                        if (j == 2):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteBishop.png', piecelocation, type.BishopW, 0, side.whiteside))
                        if (j == 4):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteKing.png', piecelocation, type.KingW, 0, side.whiteside))
                        if (j == 6):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteKnight.png', piecelocation, type.KnightW, 1, side.whiteside))
                    self.Squarelist[i].append(newSquare)

    def drawBoardAndPieces(self):
        """ draw board and piece when things changes, ( draw squares according to the Squares in Square list, and draw piece
        according to the piece location and image file in Square list)
        """

        for i in range(8):
            for j in range(8):
                if (len(self.clicklist) > 0 and (i,j) == self.findIJSquare(self.clicklist[0])):
                    self.getSquare(i, j).drawSquare(self.screen,select=True,eat=False,check=False)
                elif (self.whiteischecked and self.getSquare(i,j).Piece.type == type.KingW):
                    self.getSquare(i,j).drawSquare(self.screen,select=False,eat=False,check=True) # draw purple squares for king if checked
                elif (self.blackischecked and self.getSquare(i,j).Piece.type == type.KingB):
                    self.getSquare(i,j).drawSquare(self.screen,select=False,eat=False,check=True) # draw purple squares for king if checked
                else:
                    self.getSquare(i,j).drawSquare(self.screen,select=False,eat=False,check=False)

        for walkSquare in self.possibleWalks: # for possible walks draw green dots.
            pygame.draw.circle(self.screen, green, (walkSquare.x + 35, walkSquare.y + 35), 7)
        for eatSquare in self.possibleEats:
            eatSquare.drawSquare(self.screen,select=False,eat=True,check=False)

        for i in range(8):
            for j in range(8):
                if (self.getSquare(i,j).Piece.type != type.Empty): # pieces are drawn after all squares are drawn
                    self.getSquare(i,j).Piece.drawPieces(self.screen,self.getSquare(i,j))

    def getSquare(self,i,j):
        """ return the square at position (i,j) """
        return self.Squarelist[i][j]

    def detectDraw(self):
        if(self.DrawHandler.determineDraw()):
            self.boardActive = False
            print("Draw")


    def detectClick(self):
        """ detect the click in all the squares on the board and append the clicked square to the click list """
        if(self.boardActive):
            for i in range(8):
                for j in range(8):
                    if (self.getSquare(i,j).getclick()):
                        if (len(self.clicklist) == 0 and self.getSquare(i,j).Piece.type != type.Empty
                                and self.getSquare(i,j).Piece.side == self.currentSide):
                            self.clicklist.append(self.getSquare(i, j))

                            # get possible walks and eats
                            self.possibleWalks = self.evaluateMovesEngine.getFilteredPossibleWalks(self.getSquare(i, j))
                            self.possibleEats = self.evaluateMovesEngine.getFilteredPossibleEats(self.getSquare(i,j))

                            for walks in self.possibleWalks:
                                print(self.findIJSquare(walks))
                        elif (len(self.clicklist) == 1):
                            if (self.getSquare(i,j).Piece.side != self.clicklist[0].Piece.side):
                                if (self.evaluateMovesEngine.evaluateMove(self.clicklist[0], self.getSquare(i,j))):
                                    self.clicklist.append(self.getSquare(i,j))

                                    # check if the move affect the ability to castling (such as rook, king moves)
                                    self.WhiteKingCastlingHandler.determineMoveEffectOnCastling(self.clicklist[0])
                                    self.BlackKingCastlingHandler.determineMoveEffectOnCastling(self.clicklist[0])

                                    # for the enpassant to be true the move should be in possibleEats and it should be empty.
                                    enpassant = self.clicklist[1] in self.possibleEats and self.clicklist[1].Piece.type == type.Empty

                                    # for the castling to be true the move should be of king and it shouldn't be adjacent to the original square
                                    firstRow,firstCol = self.findIJSquare(self.clicklist[0])
                                    secondRow,secondCol = self.findIJSquare(self.clicklist[1])
                                    castling = (self.clicklist[0].Piece.type == type.KingW or self.clicklist[0].Piece.type == type.KingB)\
                                               and abs(secondCol - firstCol) == 2

                                    # clear these two lists(walklist,eatlist) before move for aesthetic effect
                                    self.possibleWalks.clear()  # after a move we clear the walklist
                                    self.possibleEats.clear()  # same

                                    # update the chessboard in stockfish engine
                                    self.stockfishIntegrationEngine.moveFromPlayer(self.clicklist[0],self.clicklist[1])
                                    # call the function to handle walk or eat moves
                                    self.walkOrEat(enpassant,castling)

                                    # after walk we change side
                                    if(self.GameMode == mode.TwoPlayer):
                                        if(self.currentSide == side.whiteside):
                                            self.currentSide = side.blackside
                                        else:
                                            self.currentSide =side.whiteside


                                    self.detectDraw()

                                    self.clicklist.clear() # after handling the walk or eat we clear the clicklist, obviously
                                    # in every moves we need to check if there is checking in the board for both black and white.
                                    self.whiteischecked = self.evaluateCheckEngine.checkCheck(side.whiteside)
                                    self.blackischecked = self.evaluateCheckEngine.checkCheck(side.blackside)
                                    if (self.whiteischecked): # print to notify
                                        print("white is checked")
                                        if(self.evaluateCheckEngine.detect_CheckMate(side.whiteside)):
                                            self.boardActive = False
                                    elif (self.blackischecked):
                                        print("black is checked")
                                        if(self.evaluateCheckEngine.detect_CheckMate(side.blackside)):
                                            self.boardActive = False
                                    if(self.GameMode != mode.TwoPlayer):
                                        if(self.GameMode == mode.OnePlayerAlphaBeta):

                                            #self.opponentMovesEngine.findBestMovesUsingAlPhaBetaPruning()
                                            #OpponentMove = self.opponentMovesEngine.bestMove
                                            firstSquare,secondSquare = self.stockfishIntegrationEngine.moveFromOpponent()
                                            self.clicklist.append(firstSquare)
                                            self.clicklist.append(secondSquare)
                                            # for the enpassant to be true the move should be in possibleEats and it should be empty.
                                            enpassant = self.clicklist[1] in self.possibleEats and self.clicklist[
                                                1].Piece.type == type.Empty

                                            # for the castling to be true the move should be of king and it shouldn't be adjacent to the original square
                                            firstRow, firstCol = self.findIJSquare(self.clicklist[0])
                                            secondRow, secondCol = self.findIJSquare(self.clicklist[1])
                                            castling = (self.clicklist[0].Piece.type == type.KingW or self.clicklist[
                                                0].Piece.type == type.KingB) \
                                                       and abs(secondCol - firstCol) == 2
                                            self.walkOrEat(enpassant,castling)
                                            self.clicklist.clear()
                                        else:
                                            self.drawBoardAndPieces()
                                            firstSquare, secondSquare = self.opponentMovesEngine.findBestMove(self.stockfishIntegrationEngine.chessboard, opposite(self.currentSide))
                                            self.clicklist.append(firstSquare)
                                            self.clicklist.append(secondSquare)
                                            enpassant = self.clicklist[1] in self.possibleEats and self.clicklist[
                                                1].Piece.type == type.Empty

                                            # for the castling to be true the move should be of king and it shouldn't be adjacent to the original square
                                            firstRow, firstCol = self.findIJSquare(self.clicklist[0])
                                            secondRow, secondCol = self.findIJSquare(self.clicklist[1])
                                            print(firstRow, firstCol, secondRow, secondCol)
                                            castling = (self.clicklist[0].Piece.type == type.KingW or self.clicklist[
                                                0].Piece.type == type.KingB) \
                                                       and abs(secondCol - firstCol) == 2
                                            self.walkOrEat(enpassant, castling)
                                            self.clicklist.clear()

                            elif (self.getSquare(i,j).Piece != self.clicklist[0].Piece): # in case that the second click is of the same side as the Piece in the first click this is the
                                # changing chosen Piece case
                                self.clicklist.clear() # so we clear the clicklist
                                self.clicklist.append(self.getSquare(i,j)) # and change the first Piece
                                self.possibleWalks.clear() # change chosen square we clear the walklist as well
                                self.possibleEats.clear() # also clear all the possible walks and eats before evaluating the new chosen square.
                                self.possibleWalks = self.evaluateMovesEngine.getFilteredPossibleWalks(self.getSquare(i, j))# and recalculate
                                self.possibleEats = self.evaluateMovesEngine.getFilteredPossibleEats(self.getSquare(i, j))
        else: # board not active
            # if promotion is occurred
            if (self.promotion != False and self.promotionHandler.choosePromotionSquare != None): # chosen the promotion type.
                # add piece to the square
                self.promotionHandler.putInSquare.addPieces(self.promotionHandler.choosePromotionSquare.Piece)
                self.promotion = False  # update the field
                self.promotionHandler.choosePromotionSquare = None  # and the pawn promotion square
                self.boardActive = True  # after the promotion is complete set board to be active again

            elif (self.promotion != False): # still not chosen the promotion type
                '''handle promotion'''
                # keep drawing and detecting click if promotion choice is not chosen yet.
                self.promotionHandler.determinePromotionSquares(self.promotion)
                self.promotionHandler.drawChooose(self.promotion)
                self.promotionHandler.detectClick()

            self.clicklist.clear()
            self.possibleWalks.clear()
            self.possibleEats.clear()

    def walkOrEat(self,enpassant,castling):
        """
        this function handle the walk or eat moves
        :param enpassant: the condition if the move is an en passant move
        :return: None
        """
        square1 = self.clicklist[0] # first we get first square and second square from the clicklist
        square2 = self.clicklist[1]
        piece1 = square1.Piece # then the first and second piece
        piece2 = square2.Piece
        location1 = piece1.getlocation() # and location of them
        location2 = piece2.getlocation()
        # and print something just for tracking
        eatmove = False
        if (square1.Piece.type != square2.Piece.type and square1.Piece.type != type.Empty and square2.Piece.type != type.Empty):
            print(square1.Piece.type.value, "eat", square2.Piece.type.value, "at", self.toNotation(self.findIJSquare(square2)))
            eatmove = True
        else:
            print(square1.Piece.type.value, "to", self.toNotation(self.findIJSquare(square2)))
        # create an instance of Moves class to track move and pieces

        castlingVal = castlingtype.noCastling
        move = Moves(square1, piece1, square2, piece2, enpassant,castlingVal,eatmove)

        Width, Height = pygame.display.get_surface().get_size()
        drawReverseMoveButton(self.screen, Width, Height, self)  # for consistency of reverseMove button
        drawBackButton(self.screen,Width,Height,self.mainMenuFunc) # for consistency of back button

        self.doAnimation(location1,location2,square1,square2,piece1) # doAnimation function gradually updates location of piece1

        # after doing the animation we need to really change the location of the piece between two square.
        square1.addPieces(ChessPieces('Assets\Pieces\empty.png', location1, type.Empty, None, side.noside))

        square2.addPieces(piece1)

        if (enpassant):  # if en passant, remove the eaten piece.
            walkSquare = self.clicklist[1]
            (walk1,walk2) = self.findIJSquare(walkSquare)
            if (piece1.side == side.whiteside):
                eatSquare = self.getSquare(walk1 + 1, walk2)
            else:
                eatSquare = self.getSquare(walk1 - 1, walk2)
            eatSquare.addPieces(ChessPieces('Assets\Pieces\empty.png', eatSquare.Piece.getlocation(), type.Empty, None, side.noside))
            print("en passant move")

        if (castling):  # if castling, move the rook accordingly
            print("castling")
            if(self.getSquare(0,2).Piece.type == type.KingB ):
                print("black right castling")
                self.walkOrEatWithoutAnimation(self.getSquare(0,0),self.getSquare(0,3),enpassant) # actually enpassant is always false in here
                move.castling = castlingtype.blackRightCastling
            elif (self.getSquare(0,6).Piece.type == type.KingB ):
                self.walkOrEatWithoutAnimation(self.getSquare(0,7),self.getSquare(0,5),enpassant) # actually enpassant is always false in here
                print("black left castling")
                move.castling = castlingtype.blackLeftCastling
            elif (self.getSquare(7,2).Piece.type == type.KingW):
                self.walkOrEatWithoutAnimation(self.getSquare(7,0),self.getSquare(7,3),enpassant) # actually enpassant is always false in here
                print("white left castling")
                move.castling = castlingtype.whiteLeftCastling
            elif (self.getSquare(7,6).Piece.type == type.KingW):
                self.walkOrEatWithoutAnimation(self.getSquare(7,7),self.getSquare(7,5),enpassant) # actually enpassant is always false in here
                print("white right castling")
                move.castling = castlingtype.whiteRightCastling
        self.moves.append(move)  # add the move to moves list
    def walkOrEatWithoutAnimation(self,firstSquare,secondSquare,enpassant):
        # TODO make this function add move to self.moves list and another function (reverse of this function will
        #  remove it)
        """ move/eat piece from firstSquare to secondSquare
        or the purpose of doing state space searches and trials to check for checks (in filter function) """

        piece1 = firstSquare.Piece  # then the first and second piece

        location1 = piece1.getlocation()  # and location of them

        # just add the empty to the first square and the first piece to the second square.
        firstSquare.addPieces(ChessPieces('Assets\Pieces\empty.png', location1, type.Empty, None, side.noside))

        secondSquare.addPieces(piece1)

        # the enpassant need to be handled specifically
        if (enpassant): # if en passant, remove the eaten piece.
            walkSquare = secondSquare
            (walk1,walk2) = self.findIJSquare(walkSquare)
            if (piece1.side == side.whiteside):
                eatSquare = self.getSquare(walk1 + 1, walk2)
            else:
                eatSquare = self.getSquare(walk1 - 1, walk2)
            eatSquare.addPieces(ChessPieces('Assets\Pieces\empty.png', eatSquare.Piece.getlocation(), type.Empty, None, side.noside))
        firstRow, firstCol = self.findIJSquare(firstSquare)
        secondRow, secondCol = self.findIJSquare(secondSquare)
        castling = (firstSquare.Piece.type == type.KingW or firstSquare.Piece.type == type.KingB) \
                   and abs(secondCol - firstCol) == 2
        if(castling):
            castlingType = findCastlingType(self,firstSquare,secondSquare)
            if(castlingType == castlingtype.whiteRightCastling):
                self.walkOrEatWithoutAnimation(self.getSquare(7,7),self.getSquare(7,5),False)
            elif(castlingType == castlingtype.whiteLeftCastling):
                self.walkOrEatWithoutAnimation(self.getSquare(7,0),self.getSquare(7,3),False)
            elif(castlingType == castlingtype.blackRightCastling):
                self.walkOrEatWithoutAnimation(self.getSquare(0,0),self.getSquare(0,3),False)
            elif(castlingType == castlingtype.blackLeftCastling):
                self.walkOrEatWithoutAnimation(self.getSquare(0,7),self.getSquare(0,5),False)
    def checkIJInSquare(self,i,j):
        """ The function to check if the square at i,j is in the board"""
        if 0 <= i and i <= 7 and 0 <= j and j <= 7:
            return True
        else:
            return False

    def findIJSquare(self,aSquare):
        """ The function to find row(i) and column(j) of the square"""
        for i in range(8):
            for j in range(8):
                if(self.getSquare(i,j) == aSquare):
                    return (i,j)
        return False

    def doAnimation(self,firstlocation,secondlocation,square1,square2,myPiece):
        # get x and y of the two locations
        firstx = firstlocation[0]
        firsty = firstlocation[1]
        secondx = secondlocation[0]
        secondy = secondlocation[1]
        (firsti,firstj) = self.findIJSquare(square1) # and get the (i,j) of the square1
        (secondi,secondj) = self.findIJSquare(square2) # and square2
        # the difference in location will be 70 times the number of difference in square
        differencex = (secondj - firstj) * 70
        differencey = (secondi - firsti) * 70

        Width, Height = pygame.display.get_surface().get_size()
        drawBackButton(self.screen, Width, Height, self.mainMenuFunc) # for consistency of Back button

        # divide moves animation into 100 frames.
        for i in range(30):
            movementx = differencex / 30 * i # the x velocity
            movementy = differencey / 30 * i # the y velocity
            pygame.time.delay(1) # some delay
            myPiece.addlocation((firstx + movementx, firsty + movementy)) # then change the location
            self.drawBoardAndPieces() # and draw it again

            if i == 15: # play sounds at the frame 30
                moveSound = pygame.mixer.Sound('Assets/Sounds/moveSound.wav')
                moveSound.play()
            pygame.display.update() # and update the display

    def toNotation(self,pos):
        """ Name the square from tuple (i,j) """
        alphabetlist = ['A','B','C','D','E','F','G','H']
        return alphabetlist[pos[1]]+str(abs(pos[0]-8))


    def reverseMoves(self,test=False,lastmove=None):
        """ Reverse the last move from the move list """
        # if test is true it means we don't remove the move from movelist and when the lastmove is specified we'll
        # use lastmove from the variable lastmove instead of the last of self.moves list.
        if(len(self.moves) > 0): # firstly there has to be more than 0 move to do reverse, obviously
            # clear these three lists whenever going back
            self.clicklist.clear() # clear the clicklist first
            self.possibleWalks.clear() # and the two list of walks and eats
            self.possibleEats.clear()
            if(not test):
                lastMove = self.moves[-1] # get the last move
            else:
                lastMove = lastmove
            # get the squares and pieces
            square1 = lastMove.getFirstSquare()
            square2 = lastMove.getSecondSquare()
            piece1 = lastMove.getFirstPiece()
            piece2 = lastMove.getSecondPiece()

            # and location of the two square
            location1 = square1.piecelocation
            location2 = square2.piecelocation
            if(not test): # also if testing we don't do animation.
                self.doAnimation(location2,location1,square2,square1,piece1) # do animation backward


            square1.addPieces(piece1) # then really change the position of the pice.
            square2.addPieces(piece2)

            if (lastMove.enPassant): # if last move is enpassant we'll need to add the eaten pawn back
                (walk1, walk2) = self.findIJSquare(square2)
                # check if the moving piece is white or black
                if (piece1.side == side.whiteside):
                    # adding pawn back
                    self.getSquare(walk1 + 1, walk2).addPieces(
                        ChessPieces('Assets/Pieces/blackPawn.png', self.getSquare(walk1 + 1, walk2).piecelocation,
                                    type.PawnB, walk2, side.blackside))
                if (piece1.side == side.blackside):
                    # adding pawn back
                    self.getSquare(walk1 - 1, walk2).addPieces(
                        ChessPieces('Assets\Pieces\whitePawn.png', self.getSquare(walk1 - 1, walk2).piecelocation,
                                    type.PawnW, walk2, side.whiteside))

            # for reversing the castling moves we need to move Rook back
            if (lastMove.getCastling() != castlingtype.noCastling):
                if (lastMove.getCastling() == castlingtype.whiteRightCastling):
                    self.walkOrEatWithoutAnimation(self.getSquare(7,5),self.getSquare(7,7),False)
                elif (lastMove.getCastling() == castlingtype.whiteLeftCastling):
                    self.walkOrEatWithoutAnimation(self.getSquare(7,3),self.getSquare(7,0),False)
                elif (lastMove.getCastling() == castlingtype.blackRightCastling):
                    self.walkOrEatWithoutAnimation(self.getSquare(0,3),self.getSquare(0,0),False)
                elif (lastMove.getCastling() == castlingtype.blackLeftCastling):
                    self.walkOrEatWithoutAnimation(self.getSquare(0,5),self.getSquare(0,7),False)

            # if the reverse move make the king moves gone from the moves list then we allow the king to castle
            if(self.BlackKingCastlingHandler.KingMove):
                returnToNoKingMove = True
                for move in self.moves[:-1]: # not considering the last move as it's being reversed.
                    if(move.firstPiece.type == type.KingB): # if there's any king move left then no
                        returnToNoKingMove = False
                        break
                if(returnToNoKingMove): # if not then change the KingMove field
                    self.BlackKingCastlingHandler.KingMove = False
            if(self.WhiteKingCastlingHandler.KingMove):
                returnToNoKingMove = True
                for move in self.moves[:-1]: # not considering the last move as it's being reversed.
                    if(move.firstPiece.type == type.KingW): # if there's any king move left then no
                        returnToNoKingMove = False
                if(returnToNoKingMove): # if not then change the KingMove field
                    self.WhiteKingCastlingHandler.KingMove = False
            if(not test): # if not testing we remove last move.
                self.moves.pop(-1) # and lastly, remove the last move in the move list.

            # also after moving back check again for check to draw purple squares.
            self.whiteischecked = self.evaluateCheckEngine.checkCheck(side.whiteside)
            self.blackischecked = self.evaluateCheckEngine.checkCheck(side.blackside)
            # in case the board is inactive from the last move since we reverse, it's now active.

            # also after reverse move we change side
            if (self.GameMode == mode.TwoPlayer):
                if(self.currentSide == side.whiteside):
                    self.currentSide = side.blackside
                else:
                    self.currentSide = side.whiteside
            self.boardActive = True
            self.stockfishIntegrationEngine.chessboard.pop()

    def printBoard(self):
        """ for debugging purpose """
        for i in range(8):
            for j in range(8):
                print(self.getSquare(i,j).Piece.type, end=" ")
            print()