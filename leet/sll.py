import unittest

class SinglyLinkedList:
	""" implementation of a simple singly linked list """
	class _Node:
		""" non public node for storing elements in the sll """
		def __init__(self, data_, next_=None):
			self.data = data_
			self.next =  next_

	def __init__(self):
		""" Initialise an empty sll """
		self.head = None
		self.tail = None
		self._n = 0

	def __len__(self):
		""" returns the length of sll """
		return self._n

	def empty(self):
		""" check whether list is empty """
		return len(self) == 0

	def addFront(self, data):
		""" add a node to the front of list, O(1) time """
		new = self._Node(data, self.head)
		if self.empty():
			self.head = self.tail = new
		else:
			self.head = new
		self._n += 1

	def addTail(self, data):
		""" add a node to the back of list, O(1) time """
		new = self._Node(data)
		if self.empty():
			self.head = self.tail = new
		else:
			self.tail.next = new
			self.tail = new
		self._n += 1

	def getHead(self):
		""" return the element at the front of the list """
		return self.head.data if self.head else None

	def getTail(self):
		""" return the element at the back of the list """
		return self.tail.data if self.tail else None

	def delete(self, e):
		""" remove node e from list """
		node = self.head
		if self.head.data == e: # special case, deleting the head
			self.head = self.head.next
			node.next = None
			if len(self) == 1:
				self.tail = None
			self._n -= 1
			return
		while node.next != None:
			if node.next.data != e:
				node = node.next
			else: # standing just before node to be deleted
				E = node.next # node of interest to be deleted
				node.next = E.next # bypass element node
				E.next = None
				self._n -= 1
				return
		# next node is the tail node
		if self.tail.data == e: # special case, deleting the tail
			E = self.tail
			self.tail = node # move tail a step behind
			self.tail.next = E.next = None  # bypass current tail
			self._n -= 1
		else:
			raise ValueError('Value not in linked list')



class TestList(unittest.TestCase):

	def test_list_empty_on_creation(self):
		ll = SinglyLinkedList()
		self.assertEqual(len(ll), 0)
		self.assertTrue(ll.empty())

	def test_add_element(self):
		ll = SinglyLinkedList()
		ll.addFront(3)
		self.assertEqual(len(ll), 1)
		self.assertFalse(ll.empty())
		self.assertEqual(ll.getHead(), 3)
		self.assertEqual(ll.getTail(), 3)

	def test_delete_element(self):
		ll = SinglyLinkedList()
		ll.addFront(3)
		ll.delete(3)
		self.assertEqual(len(ll), 0)
		self.assertEqual(ll.getHead(), None)
		self.assertEqual(ll.getTail(), None)
		ll.addTail(3)
		ll.addTail(4)
		ll.addTail(5)
		ll.delete(4)
		self.assertEqual(len(ll), 2)
		self.assertEqual(ll.getHead(), 3)
		self.assertEqual(ll.head.next.data, 5)
		self.assertEqual(ll.getTail(), 5)

if __name__ == '__main__':
	unittest.main()