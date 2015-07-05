# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        res = []
        stk = []
        vis = {}
        now = root
        while not now is None or len(stk) > 0:
            while not now is None:
                stk.append(now)
                vis[now] = 1
                now = now.left
            if len(stk) > 0:
                top = stk[-1]
                stk.pop()
                if vis[top] == 1:
                    stk.append(top)
                    vis[top] += 1
                    now = top.right
                else:
                    res.append(top.val)
                    now = None
        return res
                    
