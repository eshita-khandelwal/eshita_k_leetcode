"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        if not node:
            return node
        
        def dfs(node):
            if node in visited:
                return visited[node]
            clone_node = Node(node.val,[])
            visited[node] = clone_node
            for n in node.neighbors:
                clone_node.neighbors.append(dfs(n))
            return clone_node
        
        return dfs(node)