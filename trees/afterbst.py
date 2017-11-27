
Algorithm first(p):
	"""
	Algorithm for finding the least value in a BST
	Return None if BST is empty
	p is root of a BST
	"""
	walk = p
	while walk.left_child() is not None: # position has a left child which is not None
		walk = walk.left_child()
	return walk


Algorithm last(p):
	"""
	Algorithm for finding the largest value in a BST
	Return None if BST is empty
	p is root of a BST
	"""
	walk = p
	while walk.right_child(): # position has a right child which is not None
		walk = walk.right_child()
	return walk


Algorithm before(p):
	"""Algorithm for finding the immediate position smaller than position p in a BST """
	if left_child(p) is not None:
		walk = left_child(p)
		last(walk) # get to the largest value in subtree
	else:
		walk = p
		ancestor = parent(walk)
		while ancestor is not None and walk == left_child(ancestor):
			walk = ancestor
			ancestor = parent(ancestor)
		return ancestor


Algorithm after(p):
	""" Algorithm for finding the immediate position larger than position p in a BST """
	if right_child(p) is not None:
		# case: immediate larger value is right child of p
		walk = right_child(p)
		first(walk) # get to the smallest value in subtree
	else:
		# case: immediate larger position is ancestor of p
		walk = p
		ancestor = parent(walk)
		while ancestor is not None and walk == right_child(ancestor):
			walk = ancestor
			ancestor = parent(ancestor)
		return ancestor

Algorithm search(p, v):
	"""
	Algorithm for searching for a value v in a BST
	p is root of BST
	O(log n) upper bound for a balanced tree : h height of tree == log(n)
	"""
	if v < p._value and p.left_child() is not None:
		return search(p.left_child(), v)
	elif v > p._value and p.right_child() is not None:
		return search(p.right_child(), v)
	else:
		return p._value == v