#!/bin/bash

PBK="PBKDF2-HMAC-SHA256"
SHA1="sha1crypt"
SHA512="sha512crypt"
ARGON="argon2i"

INFERNOBALLS_DIR="$HOME/infernoballs"
JOHN_DIR="$HOME/jtr"
LEVEL=9

HASHTYPE=$SHA1
HASHES="$INFERNOBALLS_DIR/hashes/infernoball$LEVEL.hashes"
BROKEN="$INFERNOBALLS_DIR/broken/level$LEVEL/$HASHTYPE.broken"

$JOHN_DIR/run/john --format=$HASHTYPE --show $HASHES > john.txt

# Remove status lines from output.
head -n -2 john.txt > temp.txt
mv temp.txt john.txt

cat john.txt

# Add new hashes into duplicate.
cat john.txt $BROKEN | sort | uniq > temp.txt
mv temp.txt $BROKEN
rm john.txt
