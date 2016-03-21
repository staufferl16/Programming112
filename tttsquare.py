"""
Author: Ken Lambert
Edited By: Leigh Stauffer
Project: 2-1
File: tttsquare.py 

Displays an X or an O if the square is unoccupied.
"""

from breezypythongui import EasyCanvas

class TTTSquare(EasyCanvas):
    """Represents a tictactoe square."""

    def __init__(self, parent, width, height, background, number,
                 model):
        """Sets up the tictactoe square."""
        EasyCanvas.__init__(self, parent, width = width,
                            height = height, background = background)
        self.model = model
        self.number = number
        self.parent = parent
        self.width = width
        self.height = height
        self.letter = ""            # No letter in the square yet
        self.letterID = None
    
    def mousePressed(self, event):
        """Displays an X or an O if the square is unoccupied."""
        if not self.letter:
            self.letter = self.model.nextLetter()   
            self.letterID = self.drawText(self.letter,
                                          self.width // 2,
                                          self.height // 2,
                                          fill = "red")
            self.model.setLetter(self.number, self.letter)
            if self.model.hasWinner():
                self.parent.messageBox (title = "Alert",
                                        message = "Winner: " + self.letter + "!" + " The user must click 'New Game' to do anything else." ,
                                        width = 25, height = 5)
            
            

    def clear(self):
        """Clears each square of its displayed letter so it's no
        longer labeled."""
        if self.letterID != None:
             self.delete(self.letterID)
             self.letter = ""
             self.letterID = None
