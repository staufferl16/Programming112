"""
File: expressiontree.py

Author: Leigh Stauffer
Project 10

Defines nodes for expression trees.
"""

from tokens import Token

class LeafNode(object):
    """Represents an integer."""

    def __init__(self, data):
        """Creates a leaf node with the given datum (an integer)."""
        self.data = data

    def value(self):
        """Returns the value of the expression."""
        return self.data
      
    def prefix(self):
        """Returns the expression in prefix form."""
        return str(self.data)

    def infix(self):
        """Returns the expression in infix form."""
        return str(self.data)

    def postfix(self):
        """Returns the expression in postfix form."""
        return str(self.data)

    def __str__(self):
        """Returns the string rep of the expression."""
        return str(self.data)

class InteriorNode(object):
    """Represents an operator and its two operands."""

    def __init__(self, opToken, leftOper, rightOper):
        """Creates an interior node with the given operator (a token),
        and left and right operands (other nodes)."""
        self.operator = opToken
        self.leftOperand = leftOper
        self.rightOperand = rightOper

    def value(self):
        """Returns the value of the expression."""
        return self.computeValue(self.operator,
                                 self.leftOperand.value(),
                                 self.rightOperand.value())

    def computeValue(self, op, value1, value2):
        """Routine to compute a value."""
        result = 0
        theType = op.getType()
        if theType == Token.PLUS:
            result = value1 + value2
        elif theType == Token.MINUS:
            result = value1 - value2
        elif theType == Token.MUL:
            result = value1 * value2
        elif theType == Token.EXPO:
            result = value1 ** value2
        elif theType == Token.DIV:
            if value2 == 0:
                raise ZeroDivisionError("Attempt to divide by 0")
            else:
                result = value1 // value2
        return result
      
    def prefix(self):
        """Returns the expression in prefix form."""
        return str(self.operator) + " " + \
               self.leftOperand.prefix() + " " + \
               self.rightOperand.prefix()

    def infix(self):
        """Returns the expression in infix form (fully parenthesized)."""
        return "(" + self.leftOperand.infix() + " " + \
               str(self.operator) + " " + \
               self.rightOperand.infix() + ")"

    def postfix(self):
        """Returns the expression in postfic form."""
        return self.leftOperand.postfix() + " " + \
               self.rightOperand.postfix() + " " + \
               str(self.operator)

    def __str__(self):
        """Returns the string rep of the expression (as infix)."""
        return str(self.infix())

def main():
    a = LeafNode(4)
    b = InteriorNode(Token('+'), LeafNode(2), LeafNode(3))
    c = InteriorNode(Token('*'), a, b)
    c = InteriorNode(Token('-'), c, b) 
    print("Expect ((4 * (2 + 3)) - (2 + 3)) :", c.infix())
    print("Expect - * 4 + 2 3 + 2 3         :", c.prefix())
    print("Expect 4 2 3 + * 2 3 + -         :", c.postfix())
    print("Expect 15                        :", c.value())
    print(b)

if __name__ == "__main__":
    main()




