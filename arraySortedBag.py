"""
Author: Leigh Stauffer
Project 4
File: arraySortedBag.py
"""

from arrays import Array
from arraybag import ArrayBag
from abstractcollection import AbstractCollection

class ArraySortedBag(ArrayBag):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ArrayBag.__init__(self, sourceCollection)

    def __eq__(self, other):
        """Returns True if self equals other, or False otherwise."""
        AbstractCollection.__eq__(self,other)

    # Accessor methods
    def __contains__(self, item):
        """Allows the user to visit its items in ascending order with
        the for loop."""
        left = 0
        right = len(self) - 1
        while left <= right:
            midpoint = (left + right) // 2
            if item == self._items[midpoint]:
                return True
            elif item < self._items[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return False


    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        if len(self._items) == len(self):
            tempArray = Array(len(self)*2)
            for i in range(len(self)):
                tempArray[i] = self._items[i]
            self._items = tempArray
        if self.isEmpty() or item >= self._items[len(self) - 1]:
            self._items[len(self)] = item
        else:
            targetPosition = 0
            for i in range(len(self)):
                if item <= self._items[i]:
                    targetPosition = i
                    break
            for i in range(len(self),targetPosition, -1):
                self._items[i] = self._items[i-1]
            self._items[targetPosition] = item
        self._size += 1
