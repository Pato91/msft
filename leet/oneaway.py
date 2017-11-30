def oneaway(first, second):
	if not isinstance(first, str) or not isinstance(second, str):
		raise Exception('Invalid Input')
	elif first == second:
		return True
	else:
		n = len(first)
		m = len(second)

		if abs(n - m) > 1:
			return False

		smallest = first if n < m else second
		other = first if smallest == second else second

		diff = 0

		for c in smallest:
			if c not in other:
				diff += 1
			if diff > 1:
				return False
		return True


print(oneaway('jodom', 'konukojou'))
print(oneaway('jodom', 'modoj'))
print(oneaway('jodom', 'konuko'))