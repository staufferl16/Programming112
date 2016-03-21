"""
File: testhashing.py
Editor: Leigh Stauffer
Project 11
"""

def testHash(arrayLength = 10, numberOfItems = 5):
    print("\nArray length:    ", arrayLength)
    print("Number of items: ", numberOfItems)
    print(" Item          hash code      array index")
    for i in range(1, numberOfItems + 1):
        item = "Item" + str(i)
        code = hash(item)
        index = abs(code) % arrayLength
        print("%7s %20d%8d" % (item, code, index))

def main():
    """Entry point for the application."""
    testHash(10, 5)
    testHash(10, 7)
    testHash(10, 10)
    testHash(20, 10)
    testHash(40, 10)


if __name__ == "__main__":
    main()
