# Definition for a  binary tree node
#class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param inorder, a list of integers
	# @param postorder, a list of integers
	# @return a tree node

	def buildTree(self, inorder, postorder):
		n = len(inorder)
		if n == 0:
			return None
		if n == 1:
			return TreeNode(inorder[0])

		root = TreeNode(postorder[-1])
		k = inorder.index(postorder[-1])
		root.left = self.buildTree(inorder[:k], postorder[:k])
		root.right = self.buildTree(inorder[k+1:], postorder[k:-1])
		return root
