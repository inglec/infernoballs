import json
import sys

# Command line args.
filename = sys.argv[1]

# Open file.
lines = open(filename).readlines()
string = "".join(lines)

# Now can parse JSON string.
data = json.loads(string)

# Get relevant fields from parsed JSON.
hashes = data['hashes']
shares = data['shares']

for i in range(0, len(hashes) - 1):
    print(shares[i] + ":" + hashes[i])
