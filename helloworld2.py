"""
Author: Leigh Stauffer
Project 1
File: helloworld2.py

"""

from breezypythongui import EasyFrame
from tkinter.font import Font

class HelloWorld(EasyFrame):
    """Displays a greeting in a window."""

    def __init__(self):
        """Sets up the window and the label."""
        EasyFrame.__init__(self)
        textLabel = self.addLabel(text = "Hello world!", row = 0, column = 0,
                      sticky = "NSEW")

        # Set font and color of the caption.
        font = Font(family = "Verdana", size = 24, weight = "bold")
        textLabel["font"] = font
        textLabel["foreground"] = "red"

def main():
    """The starting point for launching the program."""
    HelloWorld().mainloop()

# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
