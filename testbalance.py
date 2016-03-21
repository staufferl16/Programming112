"""
File: testbalance.py
Tester program for rebalancing a BST.
Editor: Leigh Stauffer
Project 9
"""

from linkedbst import LinkedBST

def main():
    tree = LinkedBST()
    print("Adding D B A C F E G")
    tree.add("D")
    tree.add("B")
    tree.add("A")
    tree.add("C")
    tree.add("F")
    tree.add("E")
    tree.add("G")

    print("\nString:\n" + str(tree))
    print("\nLength:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())
    
    tree = LinkedBST(range(1, 16))
    print("\nAdded 1..15:\n" + str(tree))
    print("\nLength:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())
    tree.rebalance()
    print("\nAfter rebalance:\n" + str(tree))
    print("\nLength:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())
    
    lyst = list(range(1, 16))
    import random
    random.shuffle(lyst)
    tree = LinkedBST(lyst)
    print("\nAdded ", lyst, "\n" + str(tree))
    print("\nLength:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())

    
if __name__ == "__main__":
    main()




