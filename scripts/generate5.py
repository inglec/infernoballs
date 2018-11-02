letters = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiouh"

def isConsonant(c):
	return c not in vowels

def hasAdjacentConsonants(word):
	for i in range(0, len(word)-1):
		if isConsonant(word[i]) and isConsonant(word[i+1]):
			return True
	return False

def next(prefix, remaining):
	if remaining == 0:
		if hasAdjacentConsonants(prefix):
			print(prefix)
	else:
		for l in letters:
			next(prefix + l, remaining - 1)

next("", 5)
