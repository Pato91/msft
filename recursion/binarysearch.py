def binarysearch(needle, haystack, start, end):
	''' performs a recursive binary search on a list,
	find needle in haystack
	Runtime is O(log n)
	'''

	if start > end:
		return 'Needle not in haystack :('
	else:
		pick = (start + end )//2
		if haystack[pick] == needle:
			return '{0} found at index {1} !'.format(needle, pick)
		elif needle > haystack[pick]:
			return binarysearch(needle, haystack, pick+1, end)
		else:
			return binarysearch(needle, haystack, start, pick-1)

print( binarysearch(20, [12, 45, 1, 4, 345, 20, 12, 43, 7], 0, 7) )
print( binarysearch(200, [12, 45, 1, 4, 345, 20, 12, 43, 7], 0, 7) )