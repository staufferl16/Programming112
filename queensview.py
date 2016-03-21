"""
File: queensview.py
Author: Kenneth A. Lambert
Name: Leigh Stauffer
Project 6
"""

from breezypythongui import EasyFrame
from chesssquare import ChessSquare
from queensmodel import QueensModel
import sys

class QueensView(EasyFrame):
    """GUI-based many queens program."""

    def __init__(self, size = 8):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, "Many Queens")
        self.size = size
        self.model = QueensModel(size)
        # Add chess squares to the grid
        self.squares = list()
        background = "white"
        for row in range(0, size):
            for column in range(0, size):
                if background == "white":
                    background = "black"
                else:
                    background = "white"
                square = ChessSquare(self, width = 90, height = 90,
                                     background = background)
                square = self.addCanvas(canvas = square,
                                        row = row, column = column)
                self.squares.append(square)
            if background == "white":
                background = "black"
            else:
                background = "white"
                
        self.moveButton = self.addButton(text = "Move",
                                         row = size, column = 0,
                                         command = self.move)

        self.addButton(text = "New game", row = size, column = 1,
                       command = self.newGame)
        self.addLabel("Squares visited", row = size, column = 2)
        self.squaresField = self.addIntegerField(0, row = size,
                                                 column = 3, width = 3)
        self.addLabel("Queens placed", row = size, column = 4)
        self.queensField = self.addIntegerField(0, row = size,
                                                column = 5, width = 3)
        self.addLabel("Backtracks", row = size, column = 6)
        self.backtracksField = self.addIntegerField(0, row = size,
                                                    column = 7, width = 3)

    # Methods to handle user events.
    def move(self):
        self.model.move()
        self.draw()
        self.squaresField.setNumber(self.model.getSquaresVisitedCount())
        self.queensField.setNumber(self.model.getPlacementCount())
        self.backtracksField.setNumber(self.model.getBacktrackCount())
        if self.model.gameIsDone():
            self.moveButton["state"] = "disabled"
            self.messageBox(title = "ALERT", message = "Queens placed!")
        
    def newGame(self):
        """Clears the squares and resets the model."""
        self.model.newGame()
        for square in self.squares:
            square.eraseQueen()
        self.moveButton["state"] = "normal"
        self.squaresField.setNumber(self.model.getSquaresVisitedCount())
        self.queensField.setNumber(self.model.getPlacementCount())
        self.backtracksField.setNumber(self.model.getBacktrackCount())

    def draw(self):
        for row in range(self.size):
            for column in range(self.size):
                if self.model.getPiece(row, column) == "Q":
                    self.squares[row * self.size + column].drawQueen()
                else:
                    self.squares[row * self.size + column].eraseQueen()
        
def main(size = 8):
    """Starting point for the app."""
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    QueensView(size).mainloop()

# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
