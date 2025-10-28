"""
        1
       / \
      2   3
     / \
    4   5
a DFS Traversal(Pre-Order): 1->2->4->5->3

a typical recursive DFS pattern:

def dfs(node):
  if not node:
    return
1. Visit Node(process it)
print(node.val)
2. recurse left
dfs(node.left)
3. recurse right
dfs(node.right)



DFS on a graph...
#for graphs, we need a visited set to avoid infinite loops
def dfs(node, visited, graph):
  if node in visited:
    return
  visited.add(node)
  print(node)
  for neighbor in graph[node]:
    dfs(neighbor, visited, graph)

    

typical input structure

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}


#DFS IMPLEMENTATION
1. Recursive - easy to write, uses the call stack,
   watch for recursion depth in large graphs
2. Iterative(manual stack)

stack = [start]
visited = set()
while stack:
  node = stack.pop()
  if node in visited:
    continue
  visited.add(node)
  print(node)
  for neighbor in graph[node]:
    stack.append(neighbor)
"""
#Problem 1: Number of Islands (DFS - Easy)
"""
given a 2d grid of '1's (land) and '0's (water)
an island is formed by connecting adjacent lands horizontally/vertically

return the number of islands

Example:
Input:
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Output: 3
"""

#Traverse the grid cell by cell, when you see a '1' (unvisited, means you found a island)
#launch a dfs from that cell to mark the entire island as visited
#counter how many times you launched dfs
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
def dfs(r, c):
  if r < 0 or r >= rows or c < 0 or c >= cols:
    return
  if grid[r][c] != "1":
    return
  
  grid[r][c] = "0" #marked visited

  #recursive calls in 4 directions
  dfs(r-1,c)
  dfs(r+1,c)
  dfs(r,c-1)
  dfs(r,c+1)

def numIslands(grid):
  count = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == "1":
        dfs(r,c)
        count += 1
  return count

#Tree Node DFS
"""
Maximum Depth of Binary Tree
given root fo a binary tree, return its maximum depth (number of nodes along path)
example:
input[3,9,20,null,null,15,7] -> output:3
input [] -> 0
input [1] = 1
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    # Option A: recursive DFS
    # if root is None: ...
    # left_depth  = ...
    # right_depth = ...
    # return 1 + max(left_depth, right_depth)

    # Option B: iterative DFS with a stack
    # stack = [(root, 1)] if root else []
    # ans = 0
    # while stack:
    #     node, depth = stack.pop()
    #     # update ans
    #     # push children with depth+1
    # return ans

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countLeaves(root):
  if not root:
    return 0
  
  count = 0
  stack = [(root,1)]

  while stack:
    node, depth = stack.pop()

    if node.left == None and node.right == None:
      count += 1
    
    if node.right:
      stack.append((node.right, depth + 1))
    if node.left:
      stack.append((node.left, depth + 1))

  return count