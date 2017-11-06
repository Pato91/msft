import unittest


class Empty(Exception):
    ''' Error attempting to access an element from an empty container '''
    pass


class DequeArray():
    ''' Implementation of a Deque ADT
    uses a circular list implementation for underlying storage
    '''

    def __init__(self):
        ''' create an empty stack '''
        self._data = [None] * 2
        self._size = 0
        self._front = 0

    def __len__(self):
        ''' return number of elements in the deck'''
        return self._size

    def is_empty(self):
        ''' return True if deckis empty '''
        return self._size == 0

    def first(self):
        ''' return element at the front of deck without removing it
        raise exception if empty
        '''
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]

    def last(self):
        ''' return element at back of deck without removing it
        raise exception if empty
        '''
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front + self._size - 1]

    def add_first(self, element):
        ''' add an element to the front of the deck '''
        if self._size == len(self._data):
            self._resize( 2*len(self._data) )
        elif 0 < self._size < len(self._data) // 4:
            self._resize( len(self._data) // 2 )
        if self.is_empty():
            available = self._front
        else:
            available = self._front - 1
            # self._front = (self._front - 1 + len(self._data)) %
        self._data[available] = element
        self._size += 1

    def add_last(self, element):
        ''' add an element to the back of the deck '''
        if self._size == len(self._data):
            self._resize( 2*len(self._data) )
        elif 0 < self._size < len(self._data) // 4:
            self._resize( len(self._data) // 2 )
        available = ( self._front + self._size ) % len(self._data)
        self._data[available] = element
        self._size += 1

    def delete_first(self):
        ''' remove the element at the front of the deck '''
        if self.is_empty():
            raise Empty('Deque is empty')
        result = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return result

    def delete_last(self):
        ''' delete the element at the back of the deck '''
        if self.is_empty():
            raise Empty('Deque is empty')
        result = self._data[self._front + self._size -1]
        self._data[self._front + self._size - 1] = None
        self._size -= 1
        return result

    def _resize(self, size):
        ''' resize the capacity of the deck '''
        old = self._data
        self._data = [None]*size

        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk+1)% len(old)
        self._front = 0


class TestDeque(unittest.TestCase):

    def test_new_deque_is_empty(self):
        dq = DequeArray()
        self.assertTrue(dq.is_empty())
        self.assertEqual(len(dq), 0)

    def test_add_element_to_front_of_deque(self):
        dq = DequeArray()
        dq.add_first(1)
        self.assertFalse(dq.is_empty())
        self.assertEqual(len(dq), 1)

    def test_add_element_to_back_of_deque(self):
        dq = DequeArray()
        dq.add_last(1)
        self.assertFalse(dq.is_empty())
        self.assertEqual(len(dq), 1)

    def test_retrieve_first_element_in_deque(self):
        dq = DequeArray()
        dq.add_first(3)
        self.assertEqual(len(dq), 1)
        self.assertEqual(dq.first(), 3)
        self.assertEqual(len(dq), 1)

    def test_retrieve_last_element_in_deque(self):
        dq = DequeArray()
        dq.add_last(3)
        self.assertEqual(len(dq), 1)
        self.assertEqual(dq.last(), 3)
        self.assertEqual(len(dq), 1)

    def test_delete_first_element_in_deque(self):
        dq = DequeArray()
        dq.add_first(3)
        self.assertEqual(len(dq), 1)
        self.assertEqual(dq.delete_first(), 3)
        self.assertEqual(len(dq), 0)

    def test_delete_last_element_in_deque(self):
        dq = DequeArray()
        dq.add_last(3)
        self.assertEqual(len(dq), 1)
        self.assertEqual(dq.delete_last(), 3)
        self.assertEqual(len(dq), 0)

if __name__ == "__main__":
    unittest.main()
