"""
File: arraydict.py

Author: Leigh Stauffer
Project 11

An array-based dictionary.
"""

from abstractdict import AbstractDict, Entry

class ArrayDict(AbstractDict):
    """Represents an array-based dictionary."""

    def __init__(self):
        """Initializes the collection."""
        self._items = list()
        AbstractDict.__init__(self)

    def __iter__(self):
        """Serves up the keys in the dictionary."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor].key
            cursor += 1    

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""
        index = self._index(key)
        if index == -1: raise KeyError("Missing: " + str(key))
        return self._items[index].value

    def __setitem__(self, key, value):
        """If the key is not in the dictionary,
        adds the key and value to it and returns the value.
        Othwerise, replaces the old value with the new
        value and returns the old value."""
        index = self._index(key)
        if index == -1:
            self._items.append(Entry(key, value))
            self._size += 1
        else:
            self._items[index].value = value

    def pop(self, key, defaultValue = None):
        """Removes the key and returns the associated value if the
        key in in the dictionary, or returns the default value
        otherwise."""
        index = self._index(key)
        if index == -1: return defaultValue
        self._size -= 1
        return self._items.pop(index).value

    def _index(self, key):
        """Helper method for key search."""
        index = 0
        for entry in self._items:
            if entry.key == key:
                return index
            index += 1
        return -1       

def main(dictionaryType = ArrayDict):
    d = dictionaryType()
    for key in range(1, 6):
        d[key] = "Value" + str(key)
    print("\nLength: ", len(d))
    print("\nThe dictionary:", d)
    print("\nThe keys:", end = " ")
    for key in d.keys(): print(key, end = " ")
    print("\n\nThe values:", end = " ")
    for key in d.values(): print(key, end = " ")
    print("\n\nKey Value (using [])")
    for key in d:
        print(key, " ", d[key])
    print("\nKey Value (using get)")
    for key in d:
        print(key, " ", d.get(key))
    print("\nDelete all keys:")
    for key in range(1, 6):
        print(d.pop(key))
    print("\nLength: ", len(d))
    
# Include your dictionary type as an argument to main
if __name__ == "__main__":
    main()

