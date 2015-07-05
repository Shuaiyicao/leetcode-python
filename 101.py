# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def __init__(self):
        self.mapper = {}
    
    def dfs(self, node, depth):
        if node is None:
            if depth in self.mapper:
                self.mapper[depth].append(None)
            else:
                self.mapper[depth] = [ None ]
            return 
        if depth in self.mapper:
            self.mapper[depth].append(node.val)
        else:
            self.mapper[depth] = [ node.val ]
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)
    
    def check(self, level):
        n = len(level)
        fr = 0
        ed = n - 1
        while fr <= ed:
            if level[fr] != level[ed]:
                return False
            fr += 1
            ed -= 1
        return True
    def isSymmetric(self, root):
        self.dfs(root, 0)
        levels = list(self.mapper.values())
        for level in levels:
            if not self.check(level):
                return False
        return True
