from binarytree import BinaryTree

# create a sample tree, bt

bt = BinaryTree(1)
bt.insertLeft(2)
bt.insertRight(5)

l1 = bt.left_node
l1.insertLeft(3)
l1.insertRight(4)

r1 = bt.right_node
r1.insertLeft(6)
r1.insertRight(7)


bt.bfs()
