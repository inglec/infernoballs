# lowercase charset
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letters = consonants + vowels

digits = '0123456789'

charset = letters + digits

def hasNumber(word):
    for c in word:
        if c in digits:
            return True
    return False

def hasVowel(word):
    for c in word:
        if c in vowels:
            return True
    return False

# Modify this function to reduce the size of the wordlist.
def satisfiesConstraint(word):
    return hasVowel(word) and hasNumber(word)

def next(prefix, remaining):
	if remaining == 0:
        # We may only want to retain certain words.
		if satisfiesConstraint(prefix):
                    print(prefix)
	else:
		for c in charset:
			next(prefix + c, remaining - 1)

next("", 5)
