# lowercase charset
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letters = consonants + vowels

digits = '0123456789'

charset = letters + digits

def numberCount(word):
    count = 0
    for c in word:
        if c in digits:
            count += 1
    return count

def numberIndex(word):
    for i in range(0, len(word)):
        if word[i] in digits:
            return i
    return -1

def hasVowel(word):
    for c in word:
        if c in vowels:
            return True
    return False

# Modify this function to reduce the size of the wordlist.
def satisfiesConstraint(word):
    return hasVowel(word) and numberCount(word) == 1 and numberIndex(word) >= 2

def next(prefix, remaining):
    if remaining == 0:
        # We may only want to retain certain words.
        if satisfiesConstraint(prefix):
            print(prefix)
    else:
        for c in charset:
            next(prefix + c, remaining - 1)

next("", 5)
