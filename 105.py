# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        n = len(preorder)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        k = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:k+1], inorder[:k])
        root.right = self.buildTree(preorder[k+1:], inorder[k+1:])
        return root
