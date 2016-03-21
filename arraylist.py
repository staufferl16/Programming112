"""
File: arraylist.py
Author: Leigh Stauffer
Project 8
"""

from arrays import Array
from abstractlist import AbstractList

class ArrayList(AbstractList):
    """Represents an array-based list."""

    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArrayList.DEFAULT_CAPACITY)
        AbstractList.__init__(self, sourceCollection)

    # Accessor methods
    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexError if i is out of range."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self._items[i]

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayList.DEFAULT_CAPACITY)
        self.incModCount()

    def __setitem__(self, i, item):
        """Precondition: 0 <= i < len(self)
        Replaces the item at position i.
        Raises: IndexError if i is out of range."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self._items[i] = item

    def _resize(self):
        """Private helper method to resize the array if necessary."""
        temp = None
        if len(self) == len(self._items):
            temp = Array(2 * len(self._items))
        elif len(self) <= len(self._items) // 4 and \
             len(self._items) >= 2 * ArrayList.DEFAULT_CAPACITY:
            temp = Array(len(self.items) // 2)
        if temp:
            for i in range(len(self)):
                temp[i] = self._items[i]
            self._items = temp

    def insert(self, i, item):
        """Inserts the item at position i."""
        self._resize()
        if i < 0: i = 0
        elif i > len(self): i = len(self)
        if i < len(self):
            for j in range(len(self), i, -1):
                 self._items[j] = self._items[j - 1]
        self._items[i] = item
        self._size += 1
        self.incModCount()

    def pop(self, i = None):
        """Precondition: 0 <= i < len(self)
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError if i is out of range."""
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        item = self._items[i]
        for j in range(i, len(self) - 1):
            self._items[j] = self._items[j + 1]
        self._size -= 1
        self._resize()
        self.incModCount()
        return item

    def listIterator(self):
        """Returns a list iterator."""
        return ArrayList.ListIterator(self)

            


