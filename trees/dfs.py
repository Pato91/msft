from binarytree import BinaryTree

# Create a test tree: bt
bt = BinaryTree('HTML')
bt.insertLeft('HEAD')
bt.insertRight('BODY')
head = bt.left_node
head.insertLeft('META')
head.insertRight('TITLE')
body = bt.right_node
body.insertLeft('HEADING')
body.insertRight('CONTENT')
content = body.right_node
content.insertRight('WRAPPER')


bt.pre_order()

print()

bt.in_order()

print()

bt.post_order()
