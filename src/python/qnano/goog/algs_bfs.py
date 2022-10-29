from collections import namedtuple
from pprint import pprint

Size = namedtuple('Size', ['rows', 'cols'])

class Maze:

    number_of_steps = -1
    matrix = []
    target_symbol = "J"
    blocked_symbol = "X"

    def __init__(self, size=Size(4,3), start=(1,1), target=(3,3), blocked=[(1,2)]):
        self.start = (start[0]-1, start[1]-1)
        self.size = size
        self.matrix = [ ([0] * size.cols) for i in range(size.rows) ]
        self.matrix[self.start[0]][self.start[1]] = "S"
        self.matrix[target[0]-1][target[1]-1] = self.target_symbol

        for block in blocked:
            self.matrix[block[0]-1][block[1]-1] = self.blocked_symbol

        pprint(self.matrix)

    def find_number_of_steps_to_target(self):
        queue = []
        queue.append(self.start)
        visited = set()
        node_parent = dict()
        found_target = ()

        while (queue):
            current = queue.pop(0)

            # check current
            if self.matrix[current[0]][current[1]] == self.target_symbol:
                print("Found target", current)
                found_target = current
                break

            # add neighbors to queue
            else:
                visited.add(current)

                # add neighbors - right
                right = (current[0],current[1]+1)
                if right not in visited and right[1] < self.size.cols and self.matrix[right[0]][right[1]] != self.blocked_symbol:
                    queue.append(right)
                    node_parent[right] = current

                # add neighbors - left
                left = (current[0], current[1] - 1)
                if left not in visited and left[1] >= 0 and self.matrix[left[0]][left[1]] != self.blocked_symbol:
                    queue.append(left)
                    node_parent[left] = current

                # add neighbors - above
                above = (current[0] - 1, current[1])
                if above not in visited and above[0] >= 0 and self.matrix[above[0]][above[1]] != self.blocked_symbol:
                    queue.append(above)
                    node_parent[above] = current

                # add neighbors - below
                below = (current[0] + 1, current[1])
                if below not in visited and below[0] < self.size.rows and self.matrix[below[0]][below[1]] != self.blocked_symbol:
                    queue.append(below)
                    node_parent[below] = current

        parent = found_target

        print("parent: ", parent)

        self.number_of_steps = 0
        while parent != self.start:
            self.number_of_steps += 1
            parent = node_parent[parent]

        return self.number_of_steps


m = Maze()

print("Number of Steps: ", m.find_number_of_steps_to_target())

#m.matrix[0][3] = 5
#pprint(m.matrix)

