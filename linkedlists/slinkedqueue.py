import unittest

class Empty:
    ''' Error attempting to access an element from an empty container '''
    pass


class LinkedQueue:
    '''
    FIFO Implementation of a queue ADT
    uses a single linked list for underlying storage
    '''
    class _Node:
        """ A non-public nested store for a singly linked list """
        __slots__ = '_element', '_next' # streamline memory
        def __init__(self, element, next_):
            """Initialize a nodes fields
            element: reference to a users object
            next: reference to the next node in linked list
            """
            self._element = element
            self._next = next_

    def __init__(self):
        """ Create an empty queue """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """ Return the number of elements in the queue """
        return self._size

    def is_empty(self):
        """ Return True if queue is empty """
        return self._size == 0

    def first(self):
        """ Return the first element in the queue without removing it """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        """ Remove and return the first element in the queue """
        if self.is_empty():
            raise Empty('Queue is empty')
        element = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.is_empty(): # removed head was also the tail
            self._tail = None
        return element

    def enqueue(self, e):
        """ Add element to the back of the queue """
        newest = self._Node(e, None)

        if self.is_empty(): # new tail is also the head
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1


class TestQueue(unittest.TestCase):

    def test_new_queue_is_empty(self):
        q = LinkedQueue()
        self.assertTrue(q.is_empty())
        self.assertEqual(len(q), 0)

    def test_add_element_to_queue(self):
        q= LinkedQueue()
        q.enqueue(1)
        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 1)

    def test_queue_is_strictly_FIFO(self):
        q = LinkedQueue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(len(q), 2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(len(q), 1)

    def test_retrieve_first_element_in_queue(self):
        q= LinkedQueue()
        q.enqueue(3)
        self.assertEqual(len(q), 1)
        self.assertEqual(q.first(), 3)
        self.assertEqual(len(q), 1)

if __name__ == "__main__":
    unittest.main()
