import pygame
from ChessBoard import Board
from UserInterface.DrawButtons import drawReverseMoveButton
from UserInterface.Background import BackgroundPhoto
from UserInterface.Button import button
from UserInterface.Color import gold,vegasgold,red,darkred, darkgreen
from Mode import mode
from side import side
import os
import threading
from type import type


pygame.init() # initiate the pygame library

# screen width and height
Width = 1000
Height = 600

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Chess Game')
clock = pygame.time.Clock()

Gamemode = None
PlayerSide = None

def mainMenu():
    GameplayBackground = BackgroundPhoto(os.path.join("Assets","Background","Chessbackground.png"), [0, 0])
    mainMenu = True
    print("Main Menu starting")
    buttonWidth = 150
    buttonHeight = 50

    while mainMenu:
        screen.blit(GameplayBackground.image,GameplayBackground.rect)
        button(screen,"Start",Width/2-buttonWidth/2,Height/2,buttonWidth,buttonHeight,vegasgold,gold,chooseMode)
        button(screen,"Quit", Width/2-buttonWidth/2,Height/2+100,buttonWidth,buttonHeight,red,darkred,pygame.quit)
        pygame.display.update()  # update the screen every cycle for hover effects on button.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def chooseMode():
    GameplayBackground = BackgroundPhoto(os.path.join("Assets","Background","Chessbackground.png"), [0, 0])
    chosen = False
    print("chosen Menu Starting")
    buttonWidth = 150
    buttonHeight = 50
    def TwoPlayer():
        global Gamemode
        Gamemode = mode.TwoPlayer
        start_game()
    def OnePlayer():
        global Gamemode
        Gamemode = mode.OnePlayerAlphaBeta
        chooseSide()
    def OnePlayerAI():
        global Gamemode
        Gamemode = mode.OnePlayerAI
        chooseSide()
    while not chosen:
        screen.blit(GameplayBackground.image, GameplayBackground.rect)
        button(screen, "Two Player", Width / 2-buttonWidth/2, Height / 2-200, buttonWidth, buttonHeight, vegasgold, gold,
               TwoPlayer)
        button(screen, "One Player (Normal)", Width / 3 - buttonWidth*1.5 / 2, Height / 2 -100, buttonWidth*1.5, buttonHeight, red, darkred,
               OnePlayer)
        button(screen, "One Player (AI)", 2*Width / 3 - buttonWidth*1.5 / 2, Height / 2 -100, buttonWidth * 1.5,
               buttonHeight, red, darkred,
               OnePlayerAI)
        button(screen, "Back", Width / 2-buttonWidth/2, Height -100, buttonWidth, buttonHeight, vegasgold, gold,mainMenu)
        pygame.display.update()  # update the screen every cycle for hover effects on button.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def chooseSide():
    GameplayBackground = BackgroundPhoto(os.path.join("Assets","Background","Chessbackground.png"), [0, 0])
    chosen = False
    print("chosen side menu Starting")
    buttonWidth = 150
    buttonHeight = 50
    def chooseWhiteSide():
        global PlayerSide
        PlayerSide = side.whiteside
        start_game()
    def chooseBlackSide():
        global PlayerSide
        PlayerSide = side.blackside
        start_game()

    while not chosen:
        screen.blit(GameplayBackground.image, GameplayBackground.rect)
        button(screen, "White", Width / 3 - buttonWidth*1.5 / 2, Height / 2, buttonWidth*1.5, buttonHeight, darkgreen, darkgreen,
               chooseWhiteSide)
        button(screen, "Black", 2 * Width / 3 - buttonWidth * 1.5 / 2, Height / 2 , buttonWidth * 1.5,
               buttonHeight, red, darkred,
               chooseBlackSide)
        button(screen, "Back", Width / 2-buttonWidth/2, Height -100, buttonWidth, buttonHeight, vegasgold, gold,mainMenu)
        pygame.display.update()  # update the screen every cycle for hover effects on button.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
def start_game():
    GameplayBackground = BackgroundPhoto(os.path.join("Assets","Background","Horses.jpg"), [0, 0])
    gamePlay: bool = True
    print("Starting the game now!")
    print("Game Mode:",Gamemode)
    if(Gamemode != mode.TwoPlayer):
        print("Player chosen side:", PlayerSide)
    ChessBoard = Board(screen,Gamemode,mainMenu,PlayerSide)
    screen.blit(GameplayBackground.image, GameplayBackground.rect)
    print(PlayerSide == side.blackside)
    if Gamemode != mode.TwoPlayer and PlayerSide == side.blackside:
        print('in1')
        if Gamemode == mode.OnePlayerAlphaBeta:
            print("in2")
        elif Gamemode == mode.OnePlayerAI:
            print("in3")
            ChessBoard.drawBoardAndPieces()
            firstSquare, secondSquare = ChessBoard.opponentMovesEngine.findBestMove(
                ChessBoard.stockfishIntegrationEngine.chessboard, side.whiteside)
            ChessBoard.clicklist.append(firstSquare)
            ChessBoard.clicklist.append(secondSquare)
            enpassant = ChessBoard.clicklist[1] in ChessBoard.possibleEats and ChessBoard.clicklist[
                1].Piece.type == type.Empty

            # for the castling to be true the move should be of king and it shouldn't be adjacent to the original square
            firstRow, firstCol = ChessBoard.findIJSquare(ChessBoard.clicklist[0])
            secondRow, secondCol = ChessBoard.findIJSquare(ChessBoard.clicklist[1])
            print(firstRow, firstCol, secondRow, secondCol)
            castling = (ChessBoard.clicklist[0].Piece.type == type.KingW or ChessBoard.clicklist[
                0].Piece.type == type.KingB) \
                       and abs(secondCol - firstCol) == 2
            ChessBoard.walkOrEat(enpassant, castling)
            ChessBoard.clicklist.clear()

    while gamePlay:
        screen.blit(GameplayBackground.image, GameplayBackground.rect)
        '''
        thread = threading.Thread(target=ChessBoard.detectClick())
        thread.start()
        '''
        ChessBoard.detectClick()
        ChessBoard.drawBoardAndPieces()
        drawReverseMoveButton(screen,Width,Height,ChessBoard)
        button(screen, "Back", Width // 2 - 450, Height // 2 + 100, 150, 40, vegasgold, gold,mainMenu)
        ChessBoard.promotionHandler.findPromotionSquare()
        pygame.display.update()  # update the screen every cycle for hover effects on button.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

mainMenu()