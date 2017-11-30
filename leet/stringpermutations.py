def permutationCheck(s1, s2):
	""" check if the two strings are permutations """
	if len(s1) != len(s2):
		return False
	return ''.join(sorted(s1)) == ''.join(sorted(s2))

# def permutationCheck(s1, s2):
# 	""" check if the two strings are permutations """
# 	if len(s1) != len(s2):
# 		return False
# 	else:
# 		count1 = dict()
# 		count2 = dict()
# 		for i in range(len(s1)):
# 			count1[s1[i]] = count1.get(s1[i], 0) + 1
# 			count2[s2[i]] = count2.get(s2[i], 0) + 1

# 		return count1 == count2

print(permutationCheck('bee', 'ebe'))
print(permutationCheck('bee', 'ebee'))
print(permutationCheck('bee', 'eBe'))