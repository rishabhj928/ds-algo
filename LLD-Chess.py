
# Chess LLD

from enum import Enum
from abc import ABC, ABCMeta, abstractmethod

class Chess:
    def __init__(self):
        self.chessBoard = ChessBoard()
        self.player = Player()
        self.curPlayer = Player()
        self.movesList = []
        self.gameStatus = Enum("GameStatus", "ACTIVE, PAUSED, FORFEIT, BLACK_WIN, WHITE_WIN")
    
    def playerMove(self, fromPos: str, toPos: str, piece):
        pass

    def endGame(self):
        pass

    def changeTurn(self):
        pass

class Player:
    def __init__(self):
        self.account = Account()
        self.color = Enum("Color", "BLACK, WHITE")
        self.timeLeft = Time(0, 0)

class Account:
    def __init__(self):
        self.userName = ""
        self.password = ""
        self.name = ""
        self.email = ""
        self.phone = ""

class Time:
    def __init__(self, mins: int, sec: int):
        self.mins = mins
        self.sec = sec

class ChessBoard:
    def __init__(self):
        self.board = [[Cell()]*8 for _ in range(8)]
    
    def resetBoard(self):
        pass

    def updateBoard(move: 'Move'):
        pass

class Cell:
    def __init__(self):
        self.color = Enum("Color", "BLACK, WHITE")
        self.piece = Piece()
        self.position = Position()

class CellPosition:
    def __init__(self):
        self.ch = ""
        self.i = 0

class Move:
    def __init__(self):
        self.turn = Player()
        self.piece = Piece()
        self.killed = Piece()
        self.startPos = 0
        self.endPos = 0

class Piece(ABC):
    def __init__(self):
        self.color = Enum("Color", "BLACK, WHITE")
    
    @abstractmethod
    def move(self, fromPos, toPos):
        pass

    @abstractmethod
    def possibleMoves(self, fromPos, toPos):
        pass

    @abstractmethod
    def validate(self, fromPos, toPos):
        pass

class Bishop(Piece):
    @abstractmethod
    def move(self, fromPos, toPos):
        pass

    @abstractmethod
    def possibleMoves(self, fromPos, toPos):
        pass

    @abstractmethod
    def validate(self, fromPos, toPos):
        pass

class Rook(Piece):
    @abstractmethod
    def move(self, fromPos, toPos):
        pass

    @abstractmethod
    def possibleMoves(self, fromPos, toPos):
        pass

    @abstractmethod
    def validate(self, fromPos, toPos):
        pass

class King(Piece):
    @abstractmethod
    def move(self, fromPos, toPos):
        pass

    @abstractmethod
    def possibleMoves(self, fromPos, toPos):
        pass

    @abstractmethod
    def validate(self, fromPos, toPos):
        pass

class Queen(Piece):
    @abstractmethod
    def move(self, fromPos, toPos):
        pass

    @abstractmethod
    def possibleMoves(self, fromPos, toPos):
        pass

    @abstractmethod
    def validate(self, fromPos, toPos):
        pass

class Pawn(Piece):
    @abstractmethod
    def move(self, fromPos, toPos):
        pass

    @abstractmethod
    def possibleMoves(self, fromPos, toPos):
        pass

    @abstractmethod
    def validate(self, fromPos, toPos):
        pass

class Knight(Piece):
    @abstractmethod
    def move(self, fromPos, toPos):
        pass

    @abstractmethod
    def possibleMoves(self, fromPos, toPos):
        pass

    @abstractmethod
    def validate(self, fromPos, toPos):
        pass



