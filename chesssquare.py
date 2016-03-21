"""
Name: Leigh Stauffer
Project 6
File: chesssquare.py
"""

from breezypythongui import EasyCanvas
from tkinter import PhotoImage

class ChessSquare(EasyCanvas):
    """Represents a square in a chess board."""

    IMAGE = None

    def __init__(self, parent, width, height, background):
        """Sets up the canvas."""
        EasyCanvas.__init__(self, parent, width = width,
                            height = height, background = background)
        self.parent = parent
        self.x = width / 2
        self.y = height / 2
        if not ChessSquare.IMAGE:
            ChessSquare.IMAGE = PhotoImage(file = "Queen.gif")
        self.queenExists = False

    def isOccupied(self):
        return self.queenExists

    def drawQueen(self):
        """Draws the queen on the square."""
        if self.isOccupied(): return
        self.item = self.drawImage(ChessSquare.IMAGE, self.x, self.y)
        self.queenExists = True

    def eraseQueen(self):
        """Erases the queen from the square."""
        if not self.isOccupied(): return
        self.delete(self.item)
        self.queenExists = False
        
