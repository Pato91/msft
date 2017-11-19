import unittest
import queue


class BinaryTree:
	""" A binary tree data structure """
	def __init__(self, value):
		""" Initialise a Binary tree with a value """
		self.value = value
		self.left_node = None
		self.right_node = None

	def insertLeft(self, value):
		"""
		Create a value on the left node of tree
		Rules:
		If the left node has no value, create a new node with value
		else replace left node with new value,
		add current value of left node as the left node of the new node created
		"""
		if self.left_node == None:
			self.left_node = BinaryTree(value)
		else:
			current_value= self.left_node.value
			self.left_node = BinaryTree(value)
			self.left_node.insertLeft(current_value)

	def insertRight(self, value):
		"""
		Create a value on the right node of tree
		Rules:
		If the right node has no value, create a new node with value
		else replace right node with new value,
		add current value of right node as the right node of the new node created
		"""
		if self.right_node == None:
			self.right_node = BinaryTree(value)
		else:
			current_value= self.right_node.value
			self.right_node = BinaryTree(value)
			self.right_node.insertRight(current_value)

	def pre_order(self):
		""" Perform a pre-order Depth First Search (DFS) on tree """
		print(self.value)

		if self.left_node:
			self.left_node.pre_order()

		if self.right_node:
			self.right_node.pre_order()

	def in_order(self):
		""" Perform an in-order DFS on tree """
		if self.left_node:
			self.left_node.in_order()

		print(self.value)

		if self.right_node:
			self.right_node.in_order()

	def post_order(self):
		""" Perform a post-order DFS on tree """
		if self.left_node:
			self.left_node.post_order()

		if self.right_node:
			self.right_node.post_order()

		print(self.value)

	def bfs(self):
		""" Perform a Breadth First Search (BFS) on the tree """
		q = queue.Queue()
		q.put(self)

		while not q.empty():
			current_node = q.get()
			print(current_node.value)

			if current_node.left_node:
				q.put(current_node.left_node)

			if current_node.right_node:
				q.put(current_node.right_node)


class TestTree(unittest.TestCase):
	root = BinaryTree('HTML')
	root.insertLeft('HEAD')
	root.insertRight('BODY')

	head = root.left_node
	head.insertLeft('META')
	head.insertRight('TITLE')

	body = root.right_node
	body.insertLeft('HEADING')
	body.insertRight('CONTENT')

	content = body.right_node
	content.insertRight('WRAPPER')

	def test_create_tree(self):
		self.assertTrue(BinaryTree('HTML'))

	def test_root_node(self):
		self.assertEqual(self.root.value, 'HTML')

	def test_left_of_root(self):
		self.assertEqual(self.root.left_node.value, 'HEAD')

	def test_right_of_root(self):
		self.assertEqual(self.root.right_node.value, 'BODY')

	def test_head_node(self):
		head = self.root.left_node
		self.assertEqual(head.value, 'HEAD')
		self.assertEqual(head.left_node.value, 'META')
		self.assertEqual(head.right_node.value, 'TITLE')

	def test_body_node(self):
		body = self.root.right_node
		self.assertEqual(body.value, 'BODY')
		self.assertEqual(body.left_node.value, 'HEADING')
		self.assertEqual(body.right_node.value, 'CONTENT')

	def test_body_content(self):
		content = self.root.right_node.right_node
		self.assertEqual(content.right_node.value, 'WRAPPER')
		self.assertEqual(content.left_node, None)


if __name__ == '__main__':
	unittest.main()
