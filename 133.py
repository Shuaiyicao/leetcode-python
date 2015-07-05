# Definition for a undirected graph node
#class UndirectedGraphNode:
#	def __init__(self, x):
#		self.label = x
#		self.neighbors = []

class Solution:
	# @param node, a undirected graph node
	# @return a undirected graph node
	def __init__(self):
	    self.vis = {}
	    self.mp = {}
	def dfs(self, node):
		if node is None:
			return
		self.vis[node.label] = True
		tmp = UndirectedGraphNode(node.label)
		self.mp[node.label] = tmp
		for son in node.neighbors:
			if self.vis.get(son.label) == None:
				self.dfs(son)
	def clone(self, node):
		if node is None:
			return
		#print 'dfs', node.label
		t_node = self.mp[node.label]
		self.vis[node.label] = True
		for son in node.neighbors:
			t_son = self.mp[son.label]
			t_node.neighbors.append(t_son)
			if self.vis.get(son.label) == None:
				self.clone(son)

	def cloneGraph(self, node):
		if node is None:
			return None
		self.dfs(node)
		self.vis = {}
		self.clone(node)
		return self.mp[node.label]

