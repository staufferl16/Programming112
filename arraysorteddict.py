"""
File: sortedarraydict.py
Author: Leigh Stauffer
Project 11

A sorted array-based dictionary.
"""

from abstractdict import Entry
from arraydict import ArrayDict

class ArraySortedDict(ArrayDict):
    """Represents a sorted array-based dictionary."""

    def __init__(self):
        """Initializes the collection."""
        ArrayDict.__init__(self)

    def __contains__(self, key):
        """Allows the user to visit its items in ascending order with
        the for loop."""
        return self._index(key) != -1
        

    def __setitem__(self, key, value):
        """Adds item to self."""
        index = self._index(key)
        if index != -1:
            oldValue = self._items[index].value
            self._items[index].value = value
            return oldValue
        else:
            if self.isEmpty() or key >= self._items[len(self) - 1].key:
                self._items.append(Entry(key, value))
            else:
                targetPosition = 0
                for i in range(len(self)):
                    if key <= self._items[i].key:
                        targetPosition = i
                        break
                self._items.insert(targetPosition, Entry(key, value))
            self._size += 1
            return value
            

    def _index(self, key):
        """Helper method for key search."""
        left = 0
        right = len(self) - 1
        while left <= right:
            midpoint = (left + right) // 2
            if key == self._items[midpoint].key:
                return midpoint
            elif key < self._items[midpoint].key:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return -1


        
def main(dictionaryType):
    d = dictionaryType()
    for key in range(1, 6):
        d[key] = "Value" + str(key)
    print("Length:", len(d))
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
    for key in range(1, 6):
        print(d.pop(key))
    print("\nLength: ", len(d))
    
if __name__ == "__main__":
    main(ArraySortedDict)

