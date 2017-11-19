import unittest


class Empty(Exception):
    ''' Error attempting to access an element from an empty container '''
    pass


class LinkedStack:
	"""
	Implementation of the Stack ADT using a Singly Linked List
	A stack is a LIFO data structure - SLL perfectly suits it!
	"""
	class _Node:
		""" A non-public nested store for a singly linked list """
		__slots__ = '_element', '_next' # streamlining memory

		def __init__(self, element, next_):
			"""
			Initialize a nodes fields
			element: reference to a users object
			next: reference to the next node in linked list
			"""
			self._element = element
			self._next = next_

	def __init__(self):
		""" Create an empty stack """
		self._head = None
		self._size = 0

	def __len__(self):
		""" Return number of elements in stack """
		return self._size

	def is_empty(self):
		""" Return True if stack is empty """
		return self._size == 0

	def push(self, e):
		""" Add element to top of stack """
		self._head = self._Node(e, self._head)
		self._size += 1

	def top(self):
		""" Return element at top of stack without removing it """
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._head._element

	def pop(self):
		""" Remove and return element at top of stack """
		if self.is_empty():
			raise Empty('Stack is empty')
		element = self._head._element
		self._head = self._head._next
		self._size -= 1
		return element


class TestLinkedStack(unittest.TestCase):
    def test_stack_empty_when_created(self):
        stack = LinkedStack()
        self.assertTrue(stack.is_empty())

    def test_get_length_of_stack(self):
        stack = LinkedStack()
        self.assertEqual(len(stack), 0)

    def test_push_to_stack(self):
        stack = LinkedStack()
        stack.push(1)
        self.assertEqual(len(stack), 1)

    def test_get_top_of_stack(self):
        stack = LinkedStack()
        stack.push(1)
        self.assertEqual(stack.top(), 1)

    def test_pop_on_stack(self):
        stack = LinkedStack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())
        self.assertEqual(len(stack), 0)

    def test_error_on_pop_empty_stack(self):
        stack = LinkedStack()
        with self.assertRaisesRegex(Empty, 'Stack is empty'):
            stack.pop()

    def test_error_on_get_top_of_empty_stack(self):
        stack = LinkedStack()
        with self.assertRaisesRegex(Empty, 'Stack is empty'):
            stack.top()


if __name__ == '__main__':
    unittest.main()
