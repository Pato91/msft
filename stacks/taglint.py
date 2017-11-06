import unittest
from stack import ArrayStack as Stack


def closetags(html):
    ''' checks if all tags in a html block are closed '''
    stack = Stack()

    # is there an opening angle? find it
    i = html.find('<')

    while i != -1:
        j = html.find('>', i+1) # finding the next > character
        if j == -1:
            return False # invalid tag
        tag = html[i+1: j] # slice of the tag from html
        if not tag.startswith('/'):
            stack.push(tag) # its an opening tag, store in stack
        else:
            if stack.is_empty():
                return False # closing tag found without an opening tag
            if tag[1:] != stack.pop():
                return False # mismatched tag
        i = html.find('<', j+1)
    return stack.is_empty()

class TestLint(unittest.TestCase):
    def test_closed_tags(self):
        html = '''
            <html>
                <head>Something heady</head>
                <body>
                    <ul>
                        <li>Fleshed</li>
                        <li>out</li>
                        <li>body</li>
                        <li>parts</li>
                    </ul>
                </body>
            </html>
            '''
        self.assertTrue(closetags(html))

    def test_open_tags(self):
        html = '''
            <html>
                <head>Something heady</head>
                <body>
                    <ul>
                        <li>Fleshed</li>
                        <li>out<li>
                        <li>body</li>
                        <li>parts</li>
                    </ul>
                </body>
            </html>
            '''
        self.assertFalse(closetags(html))

if __name__ == '__main__':
    unittest.main()
