class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def in_order(root):
    if root:
        in_order(root.left)
        print (root.data)
        in_order(root.right)

def pre_order(root):
    if root:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data)

# Make the tree
bt = Node(4)
bt.left = Node(2)
bt.right = Node(5)
bt.left.left = Node(1)
bt.left.right = Node(3)

print("in order:")
in_order(bt)
print("pre order:")
pre_order(bt)
print("post order:")
post_order(bt)
