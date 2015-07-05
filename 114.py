# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def dfs(self, node):
        if node is None:
            return (None, None)
        if node.left is None and node.right is None:
            return (node, node)
            
        l_head, l_tail = self.dfs(node.left)
        r_head, r_tail = self.dfs(node.right)
        
        if not l_head is None:
            node.right = l_head
            l_tail.right = r_head
            l_tail.left = None
        node.left = None
        return (node, r_tail if not r_tail is None else l_tail)
        
    def flatten(self, root):
        if root is None:
            return 
        self.dfs(root)
