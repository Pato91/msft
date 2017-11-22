class Tree:
	""" Abstract base class representing a tree structure """
	class Position:
		""" Abstraction representing the location of a single element in a tree """
		def element(self):
			""" Return element stored at this position """
			raise NotImplementedError('method must be implemented by subclass')

		def __eq__(self, other):
			""" Return True if other position represents same location """
			raise NotImplementedError('method must be implemented by subclass')

		def __ne__(self, other):
			""" Return True if other position does not represents same location """
			return not( self == other)

		# Abstract methods to be implemented by subclass -----

		def root(self):
			""" Return Position representing thre  trees root, None if tree is empty """
			raise NotImplementedError('method must be implemented by subclass')

		def parent(self, p):
			""" Return Position representing the parent of p, None if p is root """
			raise NotImplementedError('method must be implemented by subclass')

		def num_children(self, p):
			""" Return the number of children that Position p has """
			raise NotImplementedError('method must be implemented by subclass')

		def children(self, p):
			""" Generate an iteration of Positions representing p's children """
			raise NotImplementedError('method must be implemented by subclass')

		def __len__(self):
			""" Return the total number of elements in the tree """
			raise NotImplementedError('method must be implemented by subclass')

		# Concrete methods implemented by class -------------

		def is_root(self, p):
			""" Return True if position p represents the root of tree """
			return self.root() == p

		def is_leaf(self, p):
			""" Return True if position p has no children """
			return self.num_children(p) == 0

		def is_empty(self, p):
			""" Return True if tree is empty """
			return len(self) == 0

		def depth(self, p):
			""" Return the number of levels separating p from the root """
			if self.is_root(p):
				return 0
			else:
				return 1 + self.depth(self.parent(p))

		def height(self, p=None):
			"""
			Return the height of the subtree rooted at position P,
			By default, return the height of the entire tree
			"""
			if p is None:
				p = self.root()
				return self.height(p)
			elif self.is_leaf(p):
				return 0
			else:
				return 1 + max(self.height(c) for c in self.children(p))
