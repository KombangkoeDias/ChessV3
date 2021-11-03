from side import side
from type import type
from MovesHandlers.evaluateCheck import EvaluateCheck
from EvaluateMovesEngine import EvaluateMovesEngine
from Moves import Moves
import time
import numpy as np
import chess
import sys

def calculateScore(_side, board):
    pieceList = str(board).split()
    scores = {"p": 1, "b": 3, "n": 3, "r": 5, "q": 8, "k": 100}
    white_score = 0
    black_score = 0
    for piece in pieceList:
        if piece != '.':  # not empty
            if piece.upper() == piece:  # white
                white_score += scores[piece.lower()]
            elif piece.lower() == piece:  # black
                black_score += scores[piece.lower()]
    if _side == side.whiteside:
        return black_score - white_score  # opponent point of view
    else:
        return white_score - black_score

def opposite(_side):
    if _side == side.whiteside:
        return side.blackside
    else:
        return side.whiteside

class OpponentMovesEngine:
  def __init__(self, depth, chessboard):
    self.depth = depth
    self.KBDchessboard = chessboard
  def maximizer(self, board: chess.Board, depth, alpha, beta, side):
    if depth == 0:
      return calculateScore(side, board)
    else:
      moves = board.legal_moves
      for move in moves:
        move = str(move)
        board.push(chess.Move.from_uci(move))
        _side = opposite(side)
        rating = self.minimizer(board, depth-1, alpha, beta, _side )
        _side = opposite(side)
        board.pop()
        if rating > alpha:
          alpha = rating
          if (depth == self.depth):
            self.bestMove = chess.Move.from_uci(move)
        if alpha >= beta:
          return alpha
      return alpha
  def minimizer(self, board: chess.Board, depth, alpha, beta, side):
      if depth == 0:
        return calculateScore(side, board)
      else:
        moves = board.legal_moves
        for move in moves:
          move = str(move)
          board.push(chess.Move.from_uci(move))
          _side = opposite(side)
          rating = self.maximizer(board, depth-1, alpha, beta, _side)
          _side = opposite(side)
          board.pop()
          if rating <= beta:
            beta = rating
          if alpha >= beta:
            return beta
        return beta
  def getSquareFromNumber(self,number):
        j = int(number%8)
        i = int(7-((number-j)/8))
        return self.KBDchessboard.getSquare(i,j)

  def findBestMove(self, board: chess.Board, side):
    self.maximizer(board, self.depth, -sys.maxsize - 1, sys.maxsize, side)
    board.push(self.bestMove)
    firstSquare = self.getSquareFromNumber(self.bestMove.from_square)
    secondSquare = self.getSquareFromNumber(self.bestMove.to_square)
    return (firstSquare, secondSquare)

