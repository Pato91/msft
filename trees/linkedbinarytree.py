import unittest
from abstractbinaryree import BinaryTree


class LinkedBinaryTree(BinaryTree):
	""" Linked representation os a binary tree structure """

	class _Node:
		""" Internal lightweight class for storign a node """
		__slots__ = '_element', '_parent', '_left', '_right'

		def __init__(self, element, parent=None, left=None, right=None):
			""" Create a  new node """
			self._element = element
			self._parent = parent
			self._left = left
			self._right = right

	class Position(BinaryTree.Position):
		""" Abstraction representing the location of a single element """
		def __init__(self, container, node):
			""" Constructor should never be invoked by user """
			self._container = container
			self._node = node

		def element(self):
			""" Return the element stored at this position """
			return self._node._element

		def __eq__(self, other):
			""" Return True if other is a Position representing the same location """
			return type(other) is type(self) and other._node is self._node

	def _validate(self, p):
		""" Return associated node is position is a valid one """
		if not isinstance(p, self.Position):
			raise TypeError('p must be proper Position type')
		if p._container is not self:
			raise ValueError('p does not belong to this container')
		if p._node._parent is p._node: # deprecated nodes
			raise ValueError('p is no longer valid')
		return p._node

	def _make_position(self, node):
		""" Return Position instance for given node, None if no node exists """
		return self.Position(self, node) if node is not None else node

	# Let's make a binary tree ------------------
	def __init__(self):
		""" Initialise an empty binary tree """
		self._root = None
		self._size = 0

	# Public accessor methods -------------------

	def __len__(self):
		""" Return total number of elements in binary tree """
		return self._size

	def root(self):
		""" Return the root position of tree, None if tree is empty """
		return self._make_position(self._root)

	def parent(self, p):
		""" Return the Position of p's parent, None if p is root """
		node = self._validate(p)
		return self._make_position(node._parent)

	def left(self, p):
		""" Return position of p's left child, None if no left child """
		node = self._validate(p)
		return self._make_position(node._left)

	def right(self, p):
		""" Return position of p's right child, None if no right child """
		node = self._validate(p)
		return self._make_position(node._right)

	def num_children(self, p):
		""" Return number of children of position p """
		node = self._validate(p)
		count = 0
		if node._left is not None:
			count += 1
		if node._right is not None:
			count += 1
		return count

	def _add_root(self, e):
		""" Add element e as teh root of an empty tree and return new Position """
		if self._root is not None:
			raise ValueError('Root already exists')
		self._size = 1
		self._root = self._Node(e)
		return self._make_position(self._root)

	def _add_left(self, p, e):
		""" Create a new left child with element e for position p and return its position """
		node = self._validate(p)
		if node._left is not None:
			raise ValueError('Left child already exists')
		self._size += 1
		node._left = self._Node(e, parent=node)
		return self._make_position(node._left)

	def _add_right(self, p, e):
		""" Create a new right child with element e for position p and return its position """
		node = self._validate(p)
		if node._right is not None:
			raise ValueError('Right child already exists')
		self._size += 1
		node._right = self._Node(e, parent=node)
		return self._make_position(node._right)

	def _replace(self, p, e):
		""" Replace the element at position p with e and return old element """
		node = self._validate(p)
		old = node._element
		node._element = e
		return old

	def _delete(self, p):
		"""
		Delete node at position p and replace it with its child if it has one
		Return element stores at previus p
		Raise Value Error if p is invalid or has two children
		"""
		node = self._validate(p)
		if self.num_children(p) == 2:
			raise ValueError('Position has two children')
		child = node._left if node._left else node._right
		if child is not None:
			child._parent = node._parent
		if node is self._root:
			self._root = child
		else:
			parent = node._parent
			if node is parent._left:
				parent._left = child
			else:
				parent._right = child
		self._size -= 1
		node._parent = node # make a deprecated node
		return node._element

	def _attach(self, p, tr1, tr2):
		""" Attach trees tr1 and tr2 and laft and right subtrees of external P """
		node = self._validate(p)
		if not self.is_leaf(p):
			raise ValueError('Docking position must be a leaf')
		if not type(self) is type(tr1) is type(tr2):
			raise TypeError('Tree types myst match')
		self._size += len(tr1)+len(tr2)
		if not tr1.is_empty():
			tr1._root._parent = node
			node._left = tr1._root
			tr1._root = None # deprecate instance of tr1
			tr1._size = 0
		if not tr2.is_empty():
			tr2._root._parent = node
			node._left = tr2._root
			tr2._root = None # deprecate instance of tr2
			tr2._size = 0


class TestLinkedBinaryTree(unittest.TestCase):
	bt = LinkedBinaryTree()
	root = bt._add_root('HTML')
	bt._add_left(root, 'HEAD')
	bt._add_right(root, 'BODY')

	head = bt.left(root)
	bt._add_left(head, 'META')
	bt._add_right(head, 'TITLE')

	body = bt.right(root)
	bt._add_left(body, 'HEADING')
	bt._add_right(body, 'CONTENT')

	content = bt.right(body)
	bt._add_right(content, 'WRAPPER')

	def test_root_node(self):
		self.assertEqual(self.root._node._element, 'HTML')

	def test_left_of_root(self):
		self.assertEqual(self.bt.left(self.root)._node._element, 'HEAD')

	def test_right_of_root(self):
		self.assertEqual(self.bt.right(self.root)._node._element, 'BODY')

	def test_head_node(self):
		head = self.bt.left(self.root)
		self.assertEqual(head._node._element, 'HEAD')
		self.assertEqual(self.bt.left(head)._node._element, 'META')
		self.assertEqual(self.bt.right(head)._node._element, 'TITLE')

	def test_body_node(self):
		body = self.bt.right(self.root)
		self.assertEqual(body._node._element, 'BODY')
		self.assertEqual(self.bt.left(body)._node._element, 'HEADING')
		self.assertEqual(self.bt.right(body)._node._element, 'CONTENT')

	def test_body_content(self):
		content = self.bt.right(self.body)
		self.assertEqual(content._node._element, 'CONTENT')
		self.assertEqual(self.bt.left(content), None)
		self.assertEqual(self.bt.right(content)._node._element, 'WRAPPER')

	def test_number_of_children(self):
		body = self.bt.right(self.root)
		self.assertEqual(self.bt.num_children(body), 2)
		heading = self.bt.left(self.body)
		self.assertEqual(self.bt.num_children(heading), 0)
		# content = self.bt.right(body)
		# self.assertEqual(self.bt.num_children(content), 1)

	def test_replace(self):
		pass

	def test_delete_element(self):
		body = self.bt.right(self.root)
		right_child = self.bt.right(body)
		self.assertEqual(self.bt._delete(right_child), 'CONTENT')
		right_child = self.bt.right(body) # updated
		self.assertEqual(right_child._node._element, 'WRAPPER')
		with self.assertRaisesRegex(ValueError, 'Position has two children'):
			self.bt._delete(body)

	def test_attach_subtrees(self):
		pass


if __name__ == '__main__':
	unittest.main()
