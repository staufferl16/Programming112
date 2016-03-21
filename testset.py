"""
Author: Leigh Stauffer
Project 5
File: testset.py
A tester program for set implementations.
"""

from arrayset import ArraySet
from linkedset import LinkedSet
from arraysortedset import ArraySortedSet

def test(setType):
    """Expects a set type as an argument and runs some tests
    on objects of that type."""
    lyst = [2013, 61, 1973, 1973]
    print("The list of items added is:", lyst)
    s1 = setType(lyst)
    print("Length, expect 3:", len(s1))
    print("Expect the set's string:", s1)
    print("2013 in s1, expect True:", 2013 in s1)
    print("2012 in s1, expect False:", 2012 in s1)
    print("Expect the items on separate lines:")
    for item in s1:
        print(item)
    s1.clear()
    print("Clearing, expect {}:", s1)
    s1.add(25)
    s1.remove(25)
    print("Add and remove 25, expect {}:", s1)
    s1 = setType(lyst)
    s2 = setType(s1)
    print("Clone with ==, expect True:", s1 == s2)
    print("Clone with is, expect False:", s1 is s2)
    for item in lyst:
        if item in s1:
            s1.remove(item)
    print("Removed each, expect {}:", s1)
    print("Expect crash with KeyError:")
    s2.remove(99)

def testSetSpecific(setType):
    """Expects a set type as an argument and runs some tests
    on objects of that type with the |, &, and - operators."""
    s1 = setType([2013, 61, 1973, 1973])
    s2 = setType([61, 44, 2013])
    print("s1:", s1, "s2:", s2)
    print("s1 | s2:", s1 | s2)
    print("s1 & s2:", s1 & s2)
    print("s1 - s2:", s1 - s2)
    print("s2 - s1:", s2 - s1)

def main():
    """Starting point for the application."""
##    test(ArraySet)
##    test(LinkedSet)
##    test(ArraySortedSet)
    testSetSpecific(ArraySet)
##    testSetSpecific(LinkedSet)
##    testSetSpecific(ArraySortedSet)

if __name__ == "__main__":
    main()
