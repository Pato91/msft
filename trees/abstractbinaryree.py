from abstractree import Tree


class BinaryTree(Tree):
	""" Abstract base class representing a binary tree structure """

	# Abstract methods --------------

	def left(self, p):
		""" Return a position representing left child of p, None if p has no left child """
		raise NotImplementedError('method must be implemented by subclass')

	def right(self, p):
		""" Return a position representing right child of p, None if p has no right child """
		raise NotImplementedError('method must be implemented by subclass')

	def sibling(self, p):
		""" Return a sibling of p if it has one, None otherwise """
		parent = self.parent(p)
		if parent is None: # p is root
			return None
		else:
			if p == self.left(parent):
				return self.right(parent)
			return self.left(parent)

	def children(self, p):
		""" Generate an iteration of positions representing children of p """
		if self.left(p) is not None:
			yield self.left(p)
		if self.right(p) is not None:
			yield self.right(p)
