"""
Author: Leigh Stauffer
Project 1
File: layoutdemo.py 

"""

from breezypythongui import EasyFrame

class LayoutDemo(EasyFrame):
    """Displays labels in the window's quadrants."""

    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self)
        self.addLabel(text = "(0, 0)", row = 0, column = 0, sticky = "NSEW")
        self.addLabel(text = "(0, 1)", row = 0, column = 1, sticky = "NSEW")
        self.addLabel(text = "(1, 0)", row = 1, column = 0, sticky = "NSEW")
        self.addLabel(text = "(1, 1)", row = 1, column = 1, sticky = "NSEW")

def main():
    """The starting point for launching the program."""
    LayoutDemo().mainloop()

# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
