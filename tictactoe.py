"""
Author: Ken
Edited By: Leigh Stauffer
Project: 2-1
File: tictactoe.py

Model for tictactoe.  Simply provides the next player's letter.
"""
#Your last stopping point was at step 1-6-D.
import random

class TicTacToe(object):
    """Models a tictactoe game."""

    def __init__(self):
        """Sets up the model."""
        self.newGame()

    def __str__(self):
        """Returns the string rep of the model."""
        result = ""
        index = 0
        for row in range (3):
            for column in range (3):
                if self.squares[index]:
                    result += self.squares[index] + " "
                else:
                    result += " "
                index += 1
            result += "\n"
        return result
            
                
    def newGame(self):
        """Resets the game to its initial state."""
        self.letter = random.choice(("X", "O"))
        self.winner = ""
        self.squares = list()
        for count in range (9):
            self.squares.append("")

    def nextLetter(self):
        """Returns the next letter for play."""
        if self.letter == "X":
            self.letter = "O"
        else:
            self.letter = "X"
        return self.letter

    def setLetter(self, index, letter):
        """Replaces the empty string at the indicated index with the
        specified letter."""
        if self.squares[index] == "":
            self.squares[index] = letter

    def checkWin(self, one, two, three):
        """Checks to see if there are 'three in a row.'"""
        return self.squares[one] == self.squares[two] and\
               self.squares[two] == self.squares[three] and\
               self.squares[one] != ""

    def hasWinner(self):
        """Checks if a player has won the game."""
        if self.winner:
            return True
        else:
           return self.checkWin(0,1,2) or \
                  self.checkWin(3,4,5) or self.checkWin(6,7,8) or \
                  self.checkWin(0,3,6) or self.checkWin(1,4,7) or \
                  self.checkWin(2,5,8) or self.checkWin(2,4,6) or \
                  self.checkWin(0,4,8)
            
    def setLetter(self, index, letter):
        """This method replaces the empty string at the index in self.squares
        with a letter."""
        self.squares[index] = letter

def main():
    """Starting point for the application."""
    model = TicTacToe()
    print(model)
    for count in range(9):
        model.setLetter(count, model.nextLetter())
        print(model)
        print(model.hasWinner())
    
if __name__ == "__main__":
    main()
 
