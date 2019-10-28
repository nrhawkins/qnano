from collections import deque

# put 5, 4, 3, 2, 1 on the stack
stack = [5, 4, 3, 2, 1]
# put 1, 2, 3, 4, 5 in the queue
queue = deque(range(1,6))

def print_stack(stack):
    while len(stack):
        print(stack.pop())

def print_queue(queue):
    while len(queue):
        print(queue.popleft())

print("print stack:")
print_stack(stack)

print("print queue")
print_queue(queue)
