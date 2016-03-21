"""
Author: Leigh Stauffer
Project: 3
File Name: tools.py

A Counter object allows the programmer to create, increment (by 1),
and reset (to 0) a counter.  When a Counter object is printed, its
current value (an integer) is displayed.

The getRandomList function returns a list of random numbers
between 1 and n.
"""

import random

class Counter(object):
    """Represents a counter object."""

    def __init__(self):
        """Sets up the counter."""
        self.counter = 0

    def __str__(self):
        """Returns a string representation of the counter."""
        return str(self.counter)

    def increment(self):
        """Increases the count."""
        self.counter += 1

    def reset(self):
        """Resets the counter to initial state of zero."""
        self.counter = 0

def getRandomList(n):
    """Returns a list of unique random numbers in the
    range 1..n"""
    lyst = list()
    for count in range (n):
        lyst.append(random.randint(1, n))
    return lyst

# Test functions

def testCounter():
    """Runs some tests on a Counter object."""
    c = Counter()
    print("Expect 0: ", c)
    for i in range(5):
        c.increment()
    print("Expect 5: ", c)
    c.reset()
    print("Expect 0: ", c)

def testGetRandomList():
    """Prints some random lists."""
    for n in range(1, 10):
        print("n: ", n, "   List:", getRandomList(n))

def main():
    """Tests the resources."""
##    testCounter() 
    testGetRandomList()

if __name__ == "__main__":
    main()
