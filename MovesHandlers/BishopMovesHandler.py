from type import type

class BishopMovesHandler:
    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.possibleEats = list()
        self.possibleWalks = list()

    def findAllPossibleWalks(self,firstSquare):
        self.possibleWalks.clear() # clear the results before evaluating
        (row,col) = self.chessboard.findIJSquare(firstSquare)
        northEast = (row-1,col+1)
        northWest = (row-1,col-1)
        southEast = (row+1,col+1)
        southWest = (row+1,col-1)
        while(self.chessboard.checkIJInSquare(northEast[0],northEast[1]) and
              self.chessboard.getSquare(northEast[0],northEast[1]).Piece.type == type.Empty):
            self.possibleWalks.append(self.chessboard.getSquare(northEast[0],northEast[1]))
            northEast = (northEast[0]- 1,northEast[1]+ 1)
        while (self.chessboard.checkIJInSquare(northWest[0], northWest[1]) and
               self.chessboard.getSquare(northWest[0], northWest[1]).Piece.type == type.Empty):
            self.possibleWalks.append(self.chessboard.getSquare(northWest[0], northWest[1]))
            northWest = (northWest[0] -1, northWest[1] - 1)
        while (self.chessboard.checkIJInSquare(southEast[0], southEast[1]) and
               self.chessboard.getSquare(southEast[0], southEast[1]).Piece.type == type.Empty):
            self.possibleWalks.append(self.chessboard.getSquare(southEast[0], southEast[1]))
            southEast = (southEast[0] + 1, southEast[1] + 1)
        while (self.chessboard.checkIJInSquare(southWest[0], southWest[1]) and
               self.chessboard.getSquare(southWest[0], southWest[1]).Piece.type == type.Empty):
            self.possibleWalks.append(self.chessboard.getSquare(southWest[0], southWest[1]))
            southWest = (southWest[0] + 1, southWest[1] - 1)
        return self.possibleWalks
    def findAllPossibleEats(self,firstSquare):
        self.possibleEats.clear() # clear the results before evaluating
        (row, col) = self.chessboard.findIJSquare(firstSquare)
        northEast = (row - 1, col + 1)
        northWest = (row - 1, col - 1)
        southEast = (row + 1, col + 1)
        southWest = (row + 1, col - 1)
        while (self.chessboard.checkIJInSquare(northEast[0], northEast[1])):
               if(self.chessboard.getSquare(northEast[0], northEast[1]).Piece.type != type.Empty):
                   northEastSquare = self.chessboard.getSquare(northEast[0], northEast[1])
                   if (northEastSquare.Piece.side != firstSquare.Piece.side):
                       self.possibleEats.append(northEastSquare)
                   break
               northEast = (northEast[0]-1, northEast[1]+1)


        while (self.chessboard.checkIJInSquare(northWest[0], northWest[1])):
            if (self.chessboard.getSquare(northWest[0], northWest[1]).Piece.type != type.Empty):
                northWestSquare = self.chessboard.getSquare(northWest[0], northWest[1])
                if (northWestSquare.Piece.side != firstSquare.Piece.side):
                    self.possibleEats.append(northWestSquare)
                break
            northWest = (northWest[0] - 1, northWest[1] - 1)

        while (self.chessboard.checkIJInSquare(southEast[0], southEast[1])):
            if (self.chessboard.getSquare(southEast[0], southEast[1]).Piece.type != type.Empty):
                southEastSquare = self.chessboard.getSquare(southEast[0], southEast[1])
                if (southEastSquare.Piece.side != firstSquare.Piece.side):
                    self.possibleEats.append(southEastSquare)
                break
            southEast = (southEast[0] + 1, southEast[1] + 1)

        while (self.chessboard.checkIJInSquare(southWest[0], southWest[1])):
            if(self.chessboard.getSquare(southWest[0], southWest[1]).Piece.type != type.Empty):
                southWestSquare = self.chessboard.getSquare(southWest[0], southWest[1])
                if (southWestSquare.Piece.side != firstSquare.Piece.side):
                    self.possibleEats.append(southWestSquare)
                break
            southWest = (southWest[0] + 1, southWest[1] - 1)
        return self.possibleEats
