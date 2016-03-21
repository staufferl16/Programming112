"""
Author: Leigh Stauffer
Project 2-2
File Name: calculator.py

This is the data model for calculatorapp.py.  It tracks the current total (a
number), the previous operator (a string), and a previous operand (a number).

"""

class Calculator(object):
    """Models a calculator."""

    def __init__(self):
        """Sets up the model."""
        self.currentTotal = None
        self.previousOperator = None
        self.previousOperand = None

    def __str__(self):
        """Returns the string of the current total."""
        return str(self.currentTotal)

    def clear(self):
        """Restores the model's initial state."""
        self.currentTotal = None
        self.previousOperator = None
        self.previousOperand = None

    def computeTotal(self, operator, operand):
        """Resets the current total based on the specified operation and the
        operand."""
        if operator == "+":
            self.currentTotal += operand
        elif operator == "-":
            self.currentTotal -= operand
        elif operator == "*":
            self.currentTotal *= operand
        elif operator == "/":
            self.currentTotal /= operand
            
    def applyOperator(self, operator, operand):
        """Applies some rules that govern the behavior of the calculator."""
        if self.currentTotal == None:
            self.currentTotal = operand
        elif operator == "=":
            self.equalsOp(operand)
        elif self.previousOperand:
            self.previousOperand = None
        else:
            self.computeTotal(operator, operand)
        if operator != "=":
            self.previousOperator = operator

    def equalsOp(self, operand):
        """What to do if the operator in applyOperator is '='."""
        if self.previousOperator:
                if self.previousOperand == None:
                    self.previousOperand = operand
                self.computeTotal(self.previousOperator, self.previousOperand)

def main():
    """Starting point for the application."""
    model = Calculator()

if __name__ == "__main__":
    main()
                    
