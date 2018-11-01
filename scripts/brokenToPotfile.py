import sys

broken = open(sys.argv[1]).readlines()
shares = open(sys.argv[2]).readlines()

sharesToHashes = {}

for share in shares:
    split = share.strip().split(':')
    share = split[0]
    hash = split[1]
    sharesToHashes[share] = hash

for b in broken:
    split = b.strip().split(':')
    share = split[0]
    word = split[1]
    hash = sharesToHashes[share]
    print(hash + ":" + word)
