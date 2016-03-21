"""
Author: Ken Lambert
Edited By: Leigh Stauffer
Project: 2-1
File: tictactoeapp.py

Uses a model to display X or O on a square when it's clicked.
"""

from breezypythongui import EasyFrame
from tttsquare import TTTSquare
from tictactoe import TicTacToe

class TicTacToeApp(EasyFrame):
    """Displays a tictactoe board in the window."""

    def __init__(self):
        """Sets up the window and the panels."""
        EasyFrame.__init__(self, title = "TicTacToe")
        self.model = TicTacToe()
        self.addButton("New Game", row = 3, column = 0,
                        columnspan = 3,
                        command = self.newGame)
        color = "black"
        number = 0
        self.squares = list()
        for row in range(3):
            for column in range(3):
                square = TTTSquare(parent = self, width = 50,
                                   height = 50,
                                   background = color,
                                   number = number,
                                   model = self.model)
                self.addCanvas(square, row = row, column = column)
                number += 1
                if color == "black":
                    color = "white"
                else:
                    color = "black"
                self.squares.append(square)
                
    def newGame(self):
        """Re-starts a new Tic Tac Toe game."""
        self.model.newGame()
        for square in self.squares:
            square.clear()
        
def main():
    """The starting point for launching the program."""
    TicTacToeApp().mainloop()

# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
