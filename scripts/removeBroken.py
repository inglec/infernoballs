import sys

hashes = open(sys.argv[1]).readlines()
broken = open(sys.argv[2]).readlines()
shares = list(map(lambda b: b.split(':')[0], broken))

for h in hashes:
    share = h.split(':')[0]
    if share not in shares:
       print(h.strip())
