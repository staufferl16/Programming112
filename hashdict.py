"""
File: hashdict.py

Author: Leigh Stauffer
Project 11

A hash-based dictionary.
"""

from abstractdict import AbstractDict, Entry
from node import Node
from arrays import Array

class HashDict(AbstractDict):
    """Represents a hash-based dictionary."""

    def __init__(self, capacity = 10):
        self._array = Array(capacity)
        self._foundEntry = self._priorEntry = None
        self._index = -1
        AbstractDict.__init__(self)

    def __iter__(self):
        """Serves up the keys in the dictionary."""
        for node in self._array:
            while node != None:
                yield node.data.key
                node = node.next

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""
        if key in self:
            return self._foundEntry.data.value
        else:
            raise KeyError("Missing: " + str(key))
    
    def __setitem__(self, key, value):
        """If the key is not in the dictionary,
        adds the key and value to it and returns the value.
        Othwerise, replaces the old value with the new
        value and returns the old value."""
        if key in self:
            self._foundEntry.data.value = value
        else:
            newNode = Node(Entry(key,value),
                           self._array[self._index])
            self._array[self._index] = newNode
            self._size += 1

    def pop(self, key, defaultValue = None):
        """Removes the key and returns the associated value if the
        key in in the dictionary, or returns the default value
        otherwise."""
        if not key in self:
            raise KeyError("Missing: " + str(key))
        elif self._priorEntry == None:
            self._array[self._index] = self._foundEntry.next
        else:
            self._priorEntry.next = self._foundEntry.next
        self._size -= 1
        return self._foundEntry.data.value

    def __contains__(self, key):
        """Returns True if the key in in the dictionary
        or False otherwise."""
        self._index = abs(hash(key)) % len(self._array)
        self._priorEntry = None
        self._foundEntry = self._array[self._index]
        while self._foundEntry != None:
            if self._foundEntry.data.key == key:
                return True
            else:
                self._priorEntry = self._foundEntry
                self._foundEntry = self._foundEntry.next
        return False

def main(capacity = 10):
    """You can specify a capacity with a HashDict."""
    d = HashDict(capacity)
    for key in range(1, capacity + 1):
        d[key] = "Value" + str(key)
    print("\nLength: ", len(d))
    print("\nThe dictionary:", d)
    print("\nThe keys:", list(d.keys()))
    print("\nThe values:", list(d.values()))
    print("\nKey Value (using [])")
    for key in d:
        print(key, " ", d[key])
    print("\nKey Value (using get)")
    for key in d:
        print(key, " ", d.get(key))
    print("\nDelete all keys:")
    for key in range(1, capacity + 1):
        print(d.pop(key))
    print("\nLength: ", len(d))
    
if __name__ == "__main__":
    main(5)

