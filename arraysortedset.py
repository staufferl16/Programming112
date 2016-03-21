"""
Author: Leigh Stauffer
Project 5
File Name: arraysortedset.py
"""
from arraySortedBag import ArraySortedBag
from abstractset import AbstractSet

class ArraySortedSet(ArraySortedBag, AbstractSet):
    """A sorted array-based set implementation."""

    #Constructor method
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the contents
        of sourceCollection, if it's present."""
        ArraySortedBag.__init__(self, sourceCollection)

    def __eq__(self, other):
        """Returns True if self equals other, or False otherwise."""
        return ArraySortedBag.__eq__(self, other)

    #Mutator method
    def add(self, item):
        """Adds item to self."""
        if item not in self:
            ArraySortedBag.add(self, item)
