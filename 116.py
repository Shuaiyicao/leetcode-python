# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def dfs(self, node):
        if node is None:
            return
        if not node.left is None:
            node.left.next = node.right
            if not node.next is None:
                node.right.next = node.next.left
        self.dfs(node.left)
        self.dfs(node.right)
    def connect(self, root):
        self.dfs(root)
