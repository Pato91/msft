

def compress(string):
	if not isinstance(string, str) or any(not c.isalpha() for c in string):
		raise Exception('Invalid input')
	else:
		n = len(string)

		if n <= 2: # trivial case, no compression
			return string

		cp = []

		i = 0
		while i < n:
			count = 1
			for j in range(i+1, n+1):
				if j == n:
					cp.extend([string[i], str(count)])
					i = j
				elif string[i] == string[j]:
					count += 1
					j+=1
					continue
				else:
					cp.extend([string[i], str(count)])
					i = j
					break

		return ''.join(cp) if len(cp) < n else string


# print(compress('jodom'))
print(compress('jooodooooom'))
