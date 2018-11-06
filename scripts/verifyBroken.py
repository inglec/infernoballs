import sys, json

infernoball = "".join(open(sys.argv[1]).readlines())
infernoball = json.loads(infernoball)

shares = list(map(lambda x: x.encode('ascii'), infernoball['shares']))
hashes = list(map(lambda x: x.encode('ascii'), infernoball['hashes']))

sharesToHashes = {}
for i in range(0, len(shares)):
    sharesToHashes[shares[i]] = hashes[i]

broken = open(sys.argv[2]).readlines()

prefix_PBKDF2 = '$pbkdf2-sha256$29000$'
prefix_sha1 = '$sha1$480000$'
prefix_sha512 = '$6$rounds=656000$'
prefix_argon2i = '$argon2i$v=19$m=102400,t=2,p=8$'

# Work out hash type of file.
hash = sharesToHashes[broken[0].split(":")[0]]
hashType = 'undefined'
if prefix_PBKDF2 in hash:
    hashType = prefix_PBKDF2
elif prefix_sha1 in hash:
    hashType = prefix_sha1
elif prefix_sha512 in hash:
    hashType = prefix_sha512
elif prefix_argon2i in hash:
    hashType = prefix_argon2i
else:
    print("Cannot determine hash type" + hash + " of " + broken[0])
    sys.exit(1)

hashesSeen = set()

# Check for invalid types / duplicates in file.
print("Detected hash type " + hashType)
for b in broken:
    b = b.strip()
    hash = sharesToHashes[b.split(":")[0]]

    if hashType not in hash:
        print(hash + "(" + b + ") does not match type " + hashType)

    if hash in hashesSeen:
        print("Duplicate " + b)
    hashesSeen.add(hash)
print("Complete")
