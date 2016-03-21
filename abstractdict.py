"""
File: abstractdict.py

Author: Leigh Stauffer
Project 11

Common data and method implementations for dictionaries.
"""
from abstractcollection import AbstractCollection

class AbstractDict(AbstractCollection):
    """Represents an abstract dictionary."""

    def __init__(self, sourceCollection = None):
        """Initialize the collection."""
        AbstractCollection.__init__(self, None)
        if sourceCollection:
            for key, value in sourceCollection:
                self[key] = value

    def __str__(self):
        return " {" + ", ".join(map(lambda entry: str(entry.key) + \
                                    ":" + str(entry.value), self.entries())) + "}"

    def get(self, key, defaultValue = None):
        """Returns the associated value if the key is in the
        dictionary, or returns the default value otherwise."""
        try:
            return self[key]
        except: return defaultValue

    def keys(self):
        """Returns an iterator on the keys in the dictionary."""
        return iter(self)

    def values(self):
        """Returns an iterator on the values in the dictionary."""
        return iter(map(lambda key: self[key], self))

    def entries(self):
        """Returns an iterator on the entries in the dictionary."""
        return iter(map(lambda key: Entry(key, self[key]), self))
    
    def __add__(self, otherDict):
        """Returns a dictionary containing the entries of self and
        otherDict.  When keys are equal, the entries in otherDict
        are ignored."""
        result = type(self)(map(lambda item: (item.key, item.value),
                                self.items()))
        for key in other:
            result[key] = other[key]
        return result

class Entry(object):
    """Represents a dictionary entry.  Supports comparisons by key."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

    def __eq__(self, other):
        if type(self) != type(other): return False
        return self.key == other.key

    def __lt__(self, other):
        if type(self) != type(other): return False
        return self.key < other.key

    def __le__(self, other):
        if type(self) != type(other): return False
        return self.key <= other.key

    def __hash__(self):
        return hash(self.key)
