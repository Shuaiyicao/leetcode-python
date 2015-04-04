# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def copy_tree(self, node):
        if node is None:
            return None
        t_node = TreeNode(node.val)
        t_node.left = self.copy_tree(node.left)
        t_node.right = self.copy_tree(node.right)
        return t_node
        
    def dfs(self, st, ed):
        if st > ed:
            return [ None ]
        res = []
        for i in range(st, ed + 1):
            all_left = self.dfs(st, i - 1)
            all_right = self.dfs(i + 1, ed)
            for left in all_left:
                for right in all_right:
                    root = TreeNode(i)
                    root.left = self.copy_tree(left)
                    root.right = self.copy_tree(right)
                    res.append(root)
        return res
    def generateTrees(self, n):
        return self.dfs(1, n)