import json
import sys

# Command line args.
filename = sys.argv[1]

# Open file.
lines = open(filename).readlines()
string = "".join(lines)

# Now can parse JSON string.
data = json.loads(string)

# Get field from parsed JSON.
print(data['ciphertext'])
