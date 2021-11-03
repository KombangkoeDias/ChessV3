
import chess
import chess.engine

class stockfishIntegrationEngine:
    def __init__(self,chessboard):
        self.chessboard = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci("/Users/Kombangkoe Dias/PycharmProjects/ChessV2/Engine/stockfish")
        self.KBDchessboard = chessboard
    def getNumberOfSquareFromIJ(self,IJ):
        i = IJ[0]
        j = IJ[1]
        return (7-i)*8 + j

    def moveFromPlayer(self,firstSquare,secondSquare):
        IJ1 = self.KBDchessboard.findIJSquare(firstSquare)
        IJ2 = self.KBDchessboard.findIJSquare(secondSquare)
        firstnum = self.getNumberOfSquareFromIJ(IJ1)
        secondnum = self.getNumberOfSquareFromIJ(IJ2)
        self.chessboard.push(chess.Move(firstnum,secondnum))

    def getSquareFromNumber(self,number):
        j = int(number%8)
        i = int(7-((number-j)/8))
        return self.KBDchessboard.getSquare(i,j)

    def moveFromOpponent(self):
        result = self.engine.play(self.chessboard,chess.engine.Limit(time=0.1,depth=0))
        self.chessboard.push(result.move)
        firstSquare = self.getSquareFromNumber(result.move.from_square)
        secondSquare = self.getSquareFromNumber(result.move.to_square)

        return (firstSquare,secondSquare)