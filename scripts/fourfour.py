import sys

lines = open(sys.argv[1]).readlines()

for l1 in lines:
    for l2 in lines:
        print(l1.strip() + l2.strip())
