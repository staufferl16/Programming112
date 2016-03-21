"""
Author: Leigh Stauffer
Program 1
Filename: ninecells.py

Creates a program that displays a window with nine cells on a 3 by 3 grid.
The label of each cell is centered in the  middle of its respective cell.
"""

from breezypythongui import EasyFrame

class NineCells(EasyFrame):
    """Displays the nine cells and their respective labels."""
    
    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self, "NineCells")
        for x in range (0,3):
            for y in range (0,3):
                labelText = "(" + str(x) + "," + str(y) + ")"
                self.addLabel (text = labelText, row = y , column = x,
                               sticky = "NSEW")
def main():
    """The starting point for launching the program."""
    NineCells().mainloop()

#Instantiates and pops up the window.
if __name__ == "__main__":
        main()
                
                
