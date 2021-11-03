from UserInterface.Button import button
from UserInterface.Color import vegasgold, gold



def drawReverseMoveButton(screen,Width,Height,ChessBoard):
    button(screen, "Reverse Move", Width // 2 - 450, Height // 2 + 50, 150, 40, vegasgold, gold,ChessBoard.reverseMoves)

def drawBackButton(screen,Width,Height,func):
    button(screen, "Back", Width // 2 - 450, Height // 2 + 100, 150, 40, vegasgold, gold, func)
