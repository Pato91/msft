from binarysearchtree import BinarySearchTree

# create a test bst as bst: sequence 50, 76, 21, 4, 32, 100, 64, 54

bst = BinarySearchTree(50)
bst.insertNode(76)
bst.insertNode(21)
bst.insertNode(4)
bst.insertNode(31)
bst.insertNode(100)
bst.insertNode(64)
bst.insertNode(54)

bst.pre_order() # 50, 21, 4, 31, 76, 64, 54, 100

print()

bst.in_order() # 4, 21, 31, 50, 54, 64, 76, 100

print()

bst.post_order() # 4, 31, 21, 54, 64, 100, 76, 50

print()

bst.bfs() # 50, 21, 76, 4, 31, 64, 100, 54

print()

# Test node deletion

bst.removeNode(54, None)

bst.bfs() # 50, 21, 76, 4, 31, 64, 100

print()

bst.removeNode(21, None)

bst.bfs() # 50, 31, 76, 4, 64, 100

print()

bst.removeNode(10, None)

bst.bfs() # 50, 31, 76, 4, 64, 100