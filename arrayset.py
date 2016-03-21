"""
Author: Leigh Stauffer
Project 5
File Name: arrayset.py
"""
from arraybag import ArrayBag
from abstractset import AbstractSet

class ArraySet(ArrayBag, AbstractSet):
    """An array-based set implementation."""

    #Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the contents
        of sourceCollection, if it's present."""
        ArrayBag.__init__(self, sourceCollection)

    def __eq__(self, other):
        """Returns True if self equals other, or False otherwise."""
        if self is other:
            return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True

    #Mutator method
    def add(self, item):
        """Adds item to self."""
        if item not in self:
            ArrayBag.add(self, item)
