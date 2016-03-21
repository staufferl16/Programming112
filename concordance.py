"""
File: concordance.py
Editor: Leigh Stauffer
Project 11

Prints a table of the unique words in a text file and their frequencies,
as well as the number of lines, words, unique words, and running time
in seconds.
"""

from arraydict import ArrayDict
from arraysorteddict import ArraySortedDict
from hashdict import HashDict
import time

def main(dictType, fileName = None):
    if fileName is None: return
    file = open(fileName, 'r')
    t1 = time.time()
    table = dictType(1000)
    wordCount = 0
    uniqueWordCount = 0
    lineCount = 0
    for line in file:
        lineCount += 1
        line = line.upper()
        for word in line.split():
            wordCount += 1
            word = normalize(word)
            freq = table.get(word, None)
            if freq:
                table[word] = freq + 1
            else:
                uniqueWordCount += 1
                table[word] = 1
    file.close()
    t2 = time.time()
    print(lineCount, "lines.")
    print(wordCount, "words.")
    print(uniqueWordCount, "unique words.")
    print("Running time was", t2 - t1, "seconds.")
    print("%25s    %-30s" % ("Word", "Frequency"))
    for key in table:
        print("%25s%6d" % (key, table[key]))

def normalize(word):
    """Strips out punctuation and converts to uppercase."""
    word = word.upper()
    if len(word) > 2:
        if word[-1] == "\"":
            word = word[:-1]
        if word[-1] in (",", ".", "?", "!", ":", ";", ")", "]"):
            word = word[:-1]
        if word[0] in ("[", "(", "\""):
            word = word[1:]
    return word


if __name__ == "__main__":
    """Entry point of the program."""
    main(HashDict, "command.txt")
