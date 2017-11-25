def frequent():
	""" Determines the most frequent word in a passage """
	freq = {}
	for section in open('passage.txt', 'r').read().lower().split(): # read, convert and split
		word = ''.join(c for c in section if c.isalpha()) # filter out punctuation marks
		if word:
			freq[word] = 1 + freq.get(word, 0)

	popular = ''
	occurence = 0
	for (word, count) in freq.items():
		if freq[word] > occurence:
			popular = word
			occurence = count

	return (popular, occurence)


print(frequent()) # ('shizzle', 13)