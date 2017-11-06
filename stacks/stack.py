import unittest

class Empty(Exception):
    ''' Error attempting to access an element from an empty container '''
    pass


class ArrayStack():
    ''' LIFO stack implementation
    uses a Python List as an underlying storage

    space usage is O(n)
    all operations are O(1)
        :- push() and pop() are amortiized i.e O(n) worst case when they cause resizing of list
    '''
    def __init__(self):
        ''' create an empty stack '''
        self._data = []

    def __len__(self):
        ''' return number of elements in the stack '''
        return len(self._data)

    def is_empty(self):
        ''' return True if stack is empty '''
        if len(self._data) == 0:
            return True
        return False

    def push(self, e):
        ''' add element e to top of stack '''
        self._data.append(e)

    def top(self):
        ''' return element at the top of the stack '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        '''remove and return the top most element on stack '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


class TestArrayStack(unittest.TestCase):
    def test_stack_empty_when_created(self):
        stack = ArrayStack()
        self.assertTrue(stack.is_empty())

    def test_get_length_of_stack(self):
        stack = ArrayStack()
        self.assertEqual(len(stack), 0)

    def test_push_to_stack(self):
        stack = ArrayStack()
        stack.push(1)
        self.assertEqual(len(stack), 1)

    def test_get_top_of_stack(self):
        stack = ArrayStack()
        stack.push(1)
        self.assertEqual(stack.top(), 1)

    def test_pop_on_stack(self):
        stack = ArrayStack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())
        self.assertEqual(len(stack), 0)

    def test_error_on_pop_empty_stack(self):
        stack = ArrayStack()
        with self.assertRaisesRegex(Empty, 'Stack is empty'):
            stack.pop()

    def test_error_on_get_top_of_empty_stack(self):
        stack = ArrayStack()
        with self.assertRaisesRegex(Empty, 'Stack is empty'):
            stack.top()


if __name__ == '__main__':
    unittest.main()
