"""
File: parserapp.py
Editor: Leigh Stauffer
Project 10
View for the infix expression parser.
Handles user interaction.
"""

from parser import Parser

class ParserView(object):

    def run(self):
        parser = Parser()
        while True:
            sourceStr = input("Enter an arithmetic expression or just enter to quit: ")
            if sourceStr == "": break
            try:
                parser.parse(sourceStr)
                print(parser.parseStatus())
            except Exception as e:
                print("Error:")
                print(e)

ParserView().run()
