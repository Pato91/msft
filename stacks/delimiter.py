import unittest
from stack import ArrayStack as Stack


def balanced(expr):
    ''' checks if all the delimiters in an expression, expr, are balanced '''
    lefts = '({[' # opening delimiters
    rights = ')}]' # respective closing delimiters
    stack = Stack()

    for d in expr:
        if d in lefts:
            stack.push(d) # first left delimiter, save for later check
        elif d in rights:
            if stack.is_empty(): # closing delimiter with no matching opening delimiter
                return False
            if rights.index(d) != lefts.index(stack.pop()): #compare match
                return False
    return stack.is_empty() # check if all symbols were matched


class TestMatched(unittest.TestCase):
    def test_balanced_delimiters(self):
        self.assertTrue(balanced('( )'))
        self.assertTrue(balanced('{([])}'))
        self.assertTrue(balanced('( )(( )){([( )])}'))
        self.assertTrue(balanced('((( )(( )){([( )])}))'))

    def test_imbalanced_delimiters(self):
        self.assertFalse(balanced(')'))
        self.assertFalse(balanced('('))
        self.assertFalse(balanced('({[ ])}'))
        self.assertFalse(balanced(')(( )){([( )])}'))

if __name__ == '__main__':
    unittest.main()
