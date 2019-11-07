class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def append(self, data):

        n = self
        d = Node(data)

        while n.next:
            n = n.next

        n.next = d

    def remove(self, data):
        pass

    def reverse(self):

        node_left = Node()
        node = self

        while node.next:
            node_right = node.next
            node.next = node_left
            # New Left, New Node
            node_left = node
            node = node_right

        node.next = node_left

        self = node

        return self

    def length(self):
        length = 0
        next = self.next
        data = self.data
        while data:
            length += 1
            if next:
                data = next.data
                next = next.next
            else:
                data = None
        return length

    def print(self):
        data = self.data
        next = self.next
        while data:
            print(data)
            if next:
                data = next.data
                next = next.next
            else:
                data = None

ll = Node(3)
ll.append(2)
ll.append(1)
ll.print()
print("length:", ll.length())
rl = ll.reverse()
print("reverse:")
rl.print()

