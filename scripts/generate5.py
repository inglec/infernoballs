# lowercase charset
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letters = consonants + vowels

digits = '0123456789'

charset = letters + digits

def hasVowel(word):
    for c in word:
        if c in vowels:
            return true
    return false

# Modify this function to reduce the size of the wordlist.
def satisfiesConstraint(word):
    return hasVowel(word) and hasNumber(word)

def next(prefix, remaining):
	if remaining == 0:
<<<<<<< HEAD
        # We may only want to retain certain words.
		if satisfiesConstraint(prefix):
            print(prefix)
=======
		if hasAdjacentConsonants(prefix):
			print(prefix)
>>>>>>> b01db906c4de59f06f4b097b990bbd3c45ca321f
	else:
		for c in charset:
			next(prefix + c, remaining - 1)

next("", 5)
