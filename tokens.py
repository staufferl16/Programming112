"""
Author: Leigh Stauffer
Project 6
File: tokens.py
Tokens for processing expressions.
"""

class Token(object):
    """Represents a word in the language."""

    UNKNOWN  = 0        # unknown
    
    LPAR     = 2       # open parentheses
    RPAR     = 3       # closed parentheses
    INT      = 4        # integer
       
    MINUS    = 5        # minus    operator
    PLUS     = 6        # plus     operator
    MUL      = 7        # multiply operator
    DIV      = 8        # divide   operator
    REMDR    = 9        # remainder operator
    EXPO     = 10       # exponentiation operator

    FIRST_OP = 5        # first operator code

    def __init__(self, value):
        """Sets the type and the value, depending on
        the value argument (either an integer or a string)."""
        if type(value) == int:
            self._type = Token.INT
        else:
            self._type = self._makeType(value)
        self._value = value

    def isOperator(self):
        """Returns True if the token is an operator,
        or False otherwise."""
        return self._type >= Token.FIRST_OP

    def getPrecedence(self):
        """Returns the precedence number of the operator."""
        if self._type == Token.EXPO:
            return 2
        elif self._type in (Token.MUL, Token.DIV, Token.REMDR):
            return 1
        elif self._type in (Token.PLUS, Token.MINUS):
            return 0
        else:
            return -1

    def __str__(self):
        """Returns the string rep of the token."""
        return str(self._value)
    
    def getType(self):
        """Returns the token's type."""
        return self._type
    
    def getValue(self):
        """Returns the token's value."""        
        return self._value

    def _makeType(self, string):
        """Returns the token's type, given its
        string value."""
        if   string == '*': return Token.MUL
        elif string == '/': return Token.DIV
        elif string == '+': return Token.PLUS
        elif string == '-': return Token.MINUS
        elif string == '%': return Token.REMDR
        elif string == '^': return Token.EXPO
        elif string == '(': return Token.LPAR
        elif string == ')': return Token.RPAR
        else:               return Token.UNKNOWN;

def main():
    """A simple tester program."""
    plus = Token("+")
    minus = Token("-")
    mul = Token("*")
    div = Token("/")
    remdr = Token("%")
    expo = Token("^")
    unknown = Token("#")
    anInt = Token(34)
    print(plus, minus, mul, div, remdr, expo, unknown, anInt)

if __name__ == '__main__': 
    main()

