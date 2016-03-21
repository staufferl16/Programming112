"""
Name: Leigh Stauffer
Project 6
File: queensview.py
Author: Kenneth A. Lambert
"""

from breezypythongui import EasyFrame
from chesssquare import ChessSquare

class TestSquare(EasyFrame):
    """GUI-based many queens program."""

    def __init__(self, size = 8):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, "Testing")
        self.square = ChessSquare(self, width = 70, height = 70,
                                  background = "white")
        self.addCanvas(canvas = self.square,
                       row = 0, column = 0, columnspan = 2)
        self.addButton(text = "Draw", row = 1, column = 0,
                       command = self.draw)

        self.addButton(text = "Erase", row = 1, column = 1,
                       command = self.erase)

    # Methods to handle user events.
    def draw(self):
        self.square.drawQueen()
        
    def erase(self):
        """Clears the squares and resets the model."""
        self.square.eraseQueen()


# Instantiates and pops up the window.
if __name__ == "__main__":
    TestSquare().mainloop()
