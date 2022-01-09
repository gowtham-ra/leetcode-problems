"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        
        self.nodes = {}
        self.dfs(node)
        return self.nodes[1]
        
    def dfs(self, node):
        u = Node(node.val)
        self.nodes[node.val] = u
        
        for v in node.neighbors:
            if v.val in self.nodes:
                u.neighbors.append(self.nodes[v.val])
            else:
                u.neighbors.append(self.dfs(v))
        
        return u
        
        
        
        
        
        
        
        
        
        
        
        
        
#         nodes = {}
        
#         if not node:
#             return
        
        
#         def dfs(node):
#             new_node = Node(node.val)
#             nodes[node.val] = new_node
            
#             for adj_node in node.neighbors:
#                 if adj_node.val in nodes:
#                     new_node.neighbors.append(nodes[adj_node.val])
#                 else:
#                     new_node.neighbors.append(dfs(adj_node))
            
#             return new_node
        
#         dfs(node)
        
#         return nodes[1]
            
        
        
        