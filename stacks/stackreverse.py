from stack import ArrayStack as Stack

def reverse():
    ''' replace the text in a file by a reverse of itself '''

    stack = Stack()

    # read original data into stack
    with open('text.txt', 'r') as original:
        for line in original:
            stack.push(line.rstrip('\n'))
        original.close()

    # write data from stack to file
    with open('text.txt', 'w') as output:
        while not stack.is_empty():
            output.write(stack.pop() + '\n')
        output.close()


if __name__ == '__main__':
    reverse()
