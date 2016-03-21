"""
Author: Leigh Stauffer
Program 2-2
Filename: calculatorapp.py

This program displays a calculator similar to a MacOS's.  It can perform
rudimental calculator actions.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
from calculator import Calculator

class CalculatorApp (EasyFrame):
    """Displays the calculator app."""

    def __init__(self):
        """Sets up the calculator app."""
        
        EasyFrame.__init__(self, "Calculator App", background = "black",
                           resizable = False)
        self.calculator = Calculator()
        self.operatorEntered = False
        self.mainLabel = self.addLabel ("0", row = 0, column = 0,
                                        columnspan = 4, sticky = "E",
                                        background = "black", foreground = "white")
        self.clearButton = self.addButton ("AC", row = 1, column = 0,
                                           command = self.clearLabel)
        self.signButton = self.addButton ("+/-", row = 1, column = 1,
                                          command = self.changeSign)
        self.percentButton = self.addButton ("%", row = 1, column = 2)
        self.divideButton = self.addButton ("/", row = 1, column = 3,
                                            command = self.makeOperatorCommand("/"))
        self.multiplyButton = self.addButton ("x", row = 2, column = 3,
                                              command = self.makeOperatorCommand("*"))
        self.subtractButton = self.addButton ("-", row = 3, column = 3,
                                              command = self.makeOperatorCommand("-"))
        self.additionButton = self.addButton ("+", row = 4, column = 3,
                                              command = self.makeOperatorCommand("+"))
        self.equalsButton = self.addButton ("=", row = 5, column = 3,
                                            command = self.makeOperatorCommand("="))
        self.decimalButton = self.addButton (".", row = 5, column = 2,
                                             command = self.addDecimal)
        self.zeroButton = self.addButton ("0", row = 5, column = 0,
                                          command = self.addZero)
        digit = 9
        for row in range (2,5):
            for column in range (0,3):
                numberButton = self.addButton(str(digit), row, column)
                numberButton["command"] = self.makeCommand(str(digit))
                digit -= 1

    def makeCommand(self, buttonText):
        """Define and return the event handler for buttons 1 - 9. AC will turn to C button."""
        def addDigit():
            if self.operatorEntered or self.mainLabel["text"] == "0":
                self.mainLabel["text"] = ""
                self.operatorEntered = False
            self.mainLabel["text"] += buttonText
            if buttonText != "0":
                self.clearButton ["text"] = "C"
        return addDigit

    def makeOperatorCommand(self, buttonText):
        """Define and return the event handler for a button."""
        def applyOperator():
            number = self.mainLabel["text"]
            if "." in number:
                number = float(number)
            else:
                number = int(number)
            self.calculator.applyOperator(buttonText, number)
            self.mainLabel["text"] = str(self.calculator)
            self.operatorEntered = True
        return applyOperator

    def addZero(self):
        """Appends a zero to the end of calculator's label."""
        if self.mainLabel ["text"] == "0":
            self.mainLabel ["text"] = ""
        self.mainLabel["text"] += "0"

    def clearLabel(self):
        """Returns main label to its original state: text = "0" and AC/C button = "AC"."""
        self.calculator = Calculator()
        self.operatorEntered = False
        self.mainLabel ["text"] = "0"
        self.clearButton ["text"] = "AC"

    def addDecimal(self):
        """Appends a decimal to the end of numeric label if decimal hasn't already been added."""
        if "." in self.mainLabel["text"]:
            self.mainLabel["text"] += ""
        else:
            self.mainLabel["text"] += "."

    def changeSign(self):
        """Changes the sign of number represented in the main label."""
        if float(self.mainLabel["text"]) != 0:
           self.mainLabel ["text"] = float(self.mainLabel ["text"]) * -1
           if self.mainLabel ["text"] == int(self.mainLabel["text"]):
               self.mainLabel ["text"] = int(self.mainLabel["text"])
           self.mainLabel["text"] = str(self.mainLabel ["text"])                
                                                        
def main():
    """The starting point for launching the program."""
    CalculatorApp().mainloop()

#Instantiates and pops up the window.
if __name__ == "__main__":
    main()
