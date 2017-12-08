def oneaway(first, second):
	if not isinstance(first, str) or not isinstance(second, str):
		raise Exception('Invalid Input')
	elif first == second:
		return True

	n = len(first)
	m = len(second)

	if abs(n - m) > 1:
		return False

	if m == n:
		diff = 0

		for i, c in enumerate(first):
			if second[i] != c:
				diff += 1
			if diff > 1:
				return False
		return True
	else:
		longer = first if n > m else second
		other = first if longer == second else second
		diff = 0

		for c in longer:
			if c not in other:
				diff += 1
			if diff > 1:
				return False
		return True

print(oneaway('jodom', 'konukojou'))
print(oneaway('jodom', 'konuko'))
print(oneaway('jodom', 'modoj'))
print(oneaway('jodom', 'jdom'))
print(oneaway('jodom', 'j0dom'))
print(oneaway('jodom', 'j0doms'))