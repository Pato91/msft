import unittest

class Empty(Exception):
    ''' Error attempting to access an element from an empty container '''
    pass

class QueueArray():
    ''' FIFO Implementation of a queue ADT
    uses a circular list implementation for underlying storage
    '''
    def __init__(self):
        ''' create an empty queue '''
        self._data = [None]*2
        self._size = 0
        self._front = 0

    def __len__(self):
        ''' return number of elements in the queue '''
        return self._size

    def is_empty(self):
        ''' return True if queue is empty '''
        return self._size == 0

    def first(self):
        ''' return element at the top of queue without removing it
        raise exception if empty
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        ''' remove and return the first element in the queue, FIFO
        raise exception if empty
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data) # circular array semantics
        self._size -= 1
        return answer

    def enqueue(self, element):
        ''' add element e to back of queue '''
        if self._size == len(self._data):
            self._resize(2*len(self._data)) # double array size
        elif 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2) # cut size by half
        available = (self._front + self._size) % len(self._data) # circular array semantics
        self._data[available] = element
        self._size += 1

    def _resize(self, size):
        ''' resize to a new list with capacity greater than len(self) '''
        old = self._data # copy old data
        self._data = [None] * size
        walk = self._front
        # copy back old data into the new queue, realign the old data
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk+1) % len(old)
        self._front = 0


class TestQueue(unittest.TestCase):

    def test_new_queue_is_empty(self):
        q = QueueArray()
        self.assertTrue(q.is_empty())
        self.assertEqual(len(q), 0)

    def test_add_element_to_queue(self):
        q= QueueArray()
        q.enqueue(1)
        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 1)

    def test_queue_is_strictly_FIFO(self):
        q = QueueArray()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(len(q), 2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(len(q), 1)

    def test_retrieve_first_element_in_queue(self):
        q= QueueArray()[]
        q.enqueue(3)
        self.assertEqual(len(q), 1)
        self.assertEqual(q.first(), 3)
        self.assertEqual(len(q), 1)

if __name__ == "__main__":
    unittest.main()
