# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    
    def __init__(self):
        self.mapper = {}
        
    def dfs(self, node, depth):
        if node is None:
            return
        if depth in self.mapper:
            self.mapper[depth].append(node.val)
        else:
            self.mapper[depth] = [ node.val ]
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)
        
    def zigzagLevelOrder(self, root):
        self.dfs(root, 0)
        res = []
        for key, level in self.mapper.items():
            if key % 2 == 0:
                res.append(level)
            else:
                res.append(list(reversed(level)))
        return res
