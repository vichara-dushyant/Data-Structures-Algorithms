from collections import deque

class BreadthFirstSearch:  # Level Order Traversal (traverse level by level)
    def __init__(self):
        self.root = None

    def traverse(self, root):
        bfs = []

        if root is None:
            return bfs

        queue = deque([])
        queue.append(root)

        while len(queue) != 0:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                current = queue.popleft()

                current_level.append(current.data)

                if current.left is not None:
                    queue.append(current.left)

                if current.right is not None:
                    queue.append(current.right)

            bfs.append(current_level)

        return bfs

# Output: Traverse Order: A → B → C → D → E → F
# [
#  ['A'],
#  ['B', 'C'],
#  ['D', 'E', 'F']
# ]

#--------------------------------------------------------------------------------------------------

# DFS (Preorder Traversal)
# Root → Left → Right (DLR)
class DepthFirstSearch:
    def __init__(self):
        self.root = None

    def traverse(self, root):
        dfs = []

        def preorder(node):
            if node is None:
                return

            dfs.append(node.data)

            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return dfs


# Output: DFS
# ['A', 'B', 'D', 'E', 'C', 'F']

#A → B → D → back → E → back → C → F

#         A
#       /   \
#      B     C
#     / \     \
#    D   E     F


# | BFS (Breadth First Search)                  | DFS (Depth First Search)           |
# | ------------------------------------------- | ---------------------------------- |
# | Visits nodes level by level                 | Goes as deep as possible first     |
# | Uses **Queue (FIFO)**                       | Uses **Stack (LIFO)** or Recursion |
# | Level Order Traversal                       | Preorder, Inorder, Postorder       |
# | Good for shortest path in unweighted graphs | Good for exploring all paths       |
# | Space: O(W) (max width)                     | Space: O(H) (tree height)          |


#DFS using Stack (LIFO)

class DepthFirstSearch:
    def __init__(self):
        self.root = None

    def traverse(self, root):
        dfs = []

        if root is None:
            return dfs

        stack = []
        stack.append(root)

        while len(stack) != 0:
            current = stack.pop()

            dfs.append(current.data)

            if current.right is not None:
                stack.append(current.right)

            if current.left is not None:
                stack.append(current.left)

        return dfs