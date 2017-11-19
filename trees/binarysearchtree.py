import unittest
import queue


class BinarySearchTree:
	""" A Binary Search Tree (BST) data structure """
	def __init__(self, value):
		"""Initialise a BST with value """
		self.value = value
		self.left_child = None
		self.right_child = None

	def insertNode(self, value):
		"""
		Insert a new node to the tree
		Rules:
		1. Is value of new node greater or smaller than the current node?
		2. If greater - Go to the right subtree.
			If current node has no right subtree, insert it there, else repeat 1.
		3. If smaller - Go to the left subtree.
			If current node has no left subtree, insert it there, else repeat 1.
		4. If value equal to current node, use rule 3. to always insert it on the left
		"""
		if value <= self.value and self.left_child:
			self.left_child.insertNode(value)
		elif value < self.value:
			self.left_child = BinarySearchTree(value)
		elif value > self.value and self.right_child:
			self.right_child.insertNode(value)
		else:
			self.right_child = BinarySearchTree(value)

	def findNode(self, value):
		"""
		Determine if a node is in the tree
		Rules:
		If value equal current node, return True
		If value if greater that current node, search right of current node
		If value is less than current node, search left of current node
		If current node has no children, return False
		"""
		if value < self.value and self.left_child:
			return self.left_child.findNode(value)
		elif value > self.value and self.right_child:
			return self.right_child.findNode(value)

		return value == self.value

	def clearNode(self):
		""" Clear a node """
		self.value = None
		self.left_child = None
		self.right_child = None

	def findMinimumValue(self):
		""" Get the smallest node in a subtree """
		if self.left_child:
			return self.left_child.findMinimumValue()
		else:
			return self.value


	def removeNode(self, value, parent):
		"""
		Remove a node of the tree
		returns True if a node if found and removed
		otherwise return a  False
		"""
		if value < self.value and self.left_child:
			return self.left_child.removeNode(value, self)
		elif value < self.value:
			return False
		elif value > self.value and self.right_child:
			return self.right_child.removeNode(value, self)
		elif value > self.value:
			return False
		else:
			if self.left_child is None  and self.right_child is None and self == parent.left_child:
				parent.left_child = None
				self.clearNode()
			elif self.left_child is None and self.right_child is None and self == parent.right_child:
				parent.right_child = None
				self.clearNode()
			elif self.left_child and self.right_child is None and self == parent.left_child:
				parent.left_child = self.left_child
				self.clearNode()
			elif self.left_child and self.right_child is None and self == parent.right_child:
				parent.right_child = self.left_child
				self.clearNode()
			elif self.left_child is None and self.right_child and self == parent.left_child:
				parent.left_child = self.right_child
				self.clearNode()
			elif self.left_child is None and self.right_child and self == parent.right_child:
				parent.right_child = self.right_child
				self.clearNode()
			else:
				self.value = self.right_child.findMinimumValue()
				self.right_child.removeNode(self.value, self)
			return True

	def pre_order(self):
		""" Perform a pre-order DFS on tree """
		print(self.value)

		if self.left_child:
			self.left_child.pre_order()

		if self.right_child:
			self.right_child.pre_order()

	def in_order(self):
		""" Perform an in-order DFS on tree """
		if self.left_child:
			self.left_child.in_order()

		print(self.value)

		if self.right_child:
			self.right_child.in_order()

	def post_order(self):
		""" Perform a post-order DFS on tree """
		if self.left_child:
			self.left_child.post_order()

		if self.right_child:
			self.right_child.post_order()

		print(self.value)


	def bfs(self):
		""" Perform a BFS on tree """
		q = queue.Queue()
		q.put(self)

		while not q.empty():
			current_node = q.get()
			print(current_node.value)

			if current_node.left_child:
				q.put(current_node.left_child)

			if current_node.right_child:
				q.put(current_node.right_child)


class TestBST(unittest.TestCase):
	""" Test sequence : 50, 76, 21, 4, 32, 100, 64, 54 """
	tree = BinarySearchTree(50)
	tree.insertNode(76)
	tree.insertNode(21)
	tree.insertNode(4)
	tree.insertNode(31)
	tree.insertNode(100)
	tree.insertNode(64)
	tree.insertNode(54)

	def test_create_bst(self):
		self.assertTrue(BinarySearchTree(50))

	def test_tree_level_zero(self):
		self.assertEqual(self.tree.value, 50)

	def test_level_one(self):
		self.assertEqual(self.tree.left_child.value, 21)
		self.assertEqual(self.tree.right_child.value, 76)

	def test_left_level_two(self):
		parent = self.tree.left_child
		self.assertEqual(parent.left_child.value, 4)
		self.assertEqual(parent.right_child.value, 31)

	def test_right_level_two(self):
		parent = self.tree.right_child
		self.assertEqual(parent.left_child.value, 64)
		self.assertEqual(parent.right_child.value, 100)

	def test_level_three(self):
		parent = self.tree.right_child.left_child
		self.assertEqual(parent.left_child.value, 54)
		self.assertEqual(parent.right_child, None)

	# Test search for a value in tree
	def test_find_node(self):
		self.assertTrue(self.tree.findNode(50))
		self.assertTrue(self.tree.findNode(31))
		self.assertTrue(self.tree.findNode(76))
		self.assertTrue(self.tree.findNode(4))
		self.assertTrue(self.tree.findNode(100))
		self.assertTrue(self.tree.findNode(54))
		self.assertFalse(self.tree.findNode(52))
		self.assertFalse(self.tree.findNode(70))

if __name__ == '__main__':
	unittest.main()
