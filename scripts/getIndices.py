import sys

broken = open(sys.argv[2]).readlines()
broken = list(map(lambda x: x.split(':')[1].strip(), broken))

with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        line = line.strip()
        if line in broken:
            print(str(i) + ": " + line)
