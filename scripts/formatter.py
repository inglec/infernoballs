import sys

# Command line args
hashes = open(sys.argv[1]).readlines()
broken = open(sys.argv[2]).readlines()

# Create dict from hashes to shares
hashesToShares = {}
for entry in hashes:
    split = entry.strip().split(':')
    share = split[0]
    hash = split[1]

    hashesToShares[hash] = share

for entry in broken:
    split = entry.strip().split(':')
    hash = split[0]
    word = split[1]

    share = hashesToShares[hash]
    print(share + ":" + word)
