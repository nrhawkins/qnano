
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)
        else:
            pass

    def pre_order(self, root):
        if root:
            print(root.data)
            self.pre_order(root.left)
            self.pre_order(root.right)
        else:
            pass

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data)
        else:
            pass

root = Node(4)
root.right = Node(5)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)

root.in_order(root)
print()
root.pre_order(root)
print()
root.post_order(root)
