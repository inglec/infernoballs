import re
import sys

lines = open(sys.argv[1]).readlines()

uniqueWords = set()

for line in lines:
    line = line.strip()
    # words = re.findall(r"[\w']+", line)
    words = line.split(" ")
    for word in words:
        uniqueWords.add(word)

uniqueWords = list(uniqueWords)
uniqueWords.sort()

for word in uniqueWords:
    print(word)
