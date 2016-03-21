"""
Name: Leigh Stauffer
Project 6
Author: Kenneth A. Lambert
File: mazeview.py
"""

from breezypythongui import EasyFrame
from mazesquare import MazeSquare
from mazemodel import MazeModel
from grid import Grid
import sys

class MazeView(EasyFrame):
    """GUI-based maze program."""

    def __init__(self, model):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, "An Amazin' Maze")
        self.model = model
        # Add maze squares to the grid
        self.squares = Grid(self.model.getHeight(), self.model.getWidth())
        for row in range(0, self.squares.getHeight()):
            for column in range(0, self.squares.getWidth()):
                square = MazeSquare(self, width = 20, height = 20,
                                   letter =  self.model.getLetter(row, column))
                square = self.addCanvas(canvas = square,
                                        row = row, column = column)
                self.squares[row][column] = square
        self.moveButton = self.addButton(text = "Move",
                                         row = self.model.getHeight(),
                                         column = 0, columnspan = self.model.getWidth(),
                                         command = self.move)

    def move(self):
        row, column = self.model.move()
        self.squares[row][column].setLetter(self.model.getLetter(row, column))
        if self.model.isSolved():
            self.moveButton["state"] = "disabled"
            self.messageBox(title = "ALERT", message = "Maze solved")
        elif not self.model.canMove():
            self.moveButton["state"] = "disabled"
            self.messageBox(title = "ALERT", message = "Maze can't be solved")


def main(fileName = "maze1.txt"):
    """Starting point for the app."""
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    model = MazeModel(fileName)
    MazeView(model).mainloop()
    
# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
