import json
import sys

# Command line args.
filename = sys.argv[1]
fieldname = sys.argv[2]

# Open file.
lines = open(filename).readlines()
string = "".join(lines)

# Now can parse JSON string.
data = json.loads(string)

# Get relevant field from parsed JSON.
field = data[fieldname]

if isinstance(field, list):
    for entry in field:
        print(entry)
else:
    print field
