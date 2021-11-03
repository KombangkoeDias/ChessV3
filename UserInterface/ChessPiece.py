import pygame
import os
import enum
from side import side
from type import type

class ChessPieces:
    def __init__(self, image_file, location,type,order,side):
        pygame.sprite.Sprite.__init__(self)
        self.imagefile = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.type = type
        self.side = side
        self.order = order
    def addlocation(self,location):
        self.rect.left,self.rect.top = location
        return self
    def drawPieces(self,screen,Square):
        screen.blit(Square.Piece.image, Square.Piece.rect)
    def getlocation(self):
        return (self.rect.left,self.rect.top)

EmptyPiece = ChessPieces(os.path.join('Assets','Pieces','empty.png'), (0, 0), type.Empty, None, side.noside)