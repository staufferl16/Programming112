"""
File: arrayqueue.py
Author: Leigh Stauffer
Project 7
"""

from arrays import Array
from abstractcollection import AbstractCollection

class ArrayQueue(AbstractCollection):
    """An array-based queue implementation."""

    # Simulates a circlular queue within an array

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._front = self._rear = -1
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._front
        if self._front <= self._rear:
            while cursor <= self._rear:
                yield self._items[cursor]
                cursor += 1
        else:
            while cursor < len(self._items):
                yield self._items[cursor]
                cursor += 1
            while cursor <= self._rear:
                cursor = 0
                yield self._items[cursor]
                cursor += 1
            
    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        if self.isEmpty():
            raise KeyError("Queue is empty")
        return self._items[len(self) - 1]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._front = self._rear = -1
        self._size = 0
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
    
    def add(self, item):
        """Inserts item at rear of the queue."""
        if len(self) == len(self._items):
            tempArray = Array(len(self) * 2)
            i = 0
            for otherItem in self:
                tempArray[i] = otherItem
                i += 1
            self._items = tempArray
            self._front = 0
            self._rear = len(self) - 1
        if self.isEmpty():
            self._front = self._rear = 0
        elif self._rear == len(self._items) - 1:
            self._rear = 0
        else:
            self._rear += 1
        self._items[self._rear] = item
        self._size += 1

    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("Queue is empty")
        data = self._items[self._front]
        self._size -= 1
        if self.isEmpty(): self._front = self._rear = -1                  
        elif self._front == len(self._items) - 1:
            self._front = 0
        else:
            self._front += 1
        if len(self) == len(self._items) / 4 and len(self) / 4 > ArrayQueue.DEFAULT_CAPACITY :
            tempArray = Array(len(self) / 2)
            i = 0
            for otherItem in self:
                tempArray[i] = otherItem
                i += 1
            self._items = tempArray
            self._front = 0
            self._rear = len(self._items) - 1
        return data
        
         
