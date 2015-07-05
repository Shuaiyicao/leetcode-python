class Node:
	def __init__(self):
		self.next = [ None for i in range(26) ]
		self.mark = False

class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a list of strings
	def insert(self, word):
		p = self.root
		for s in word:
			k = ord(s) - ord('a')
			if p.next[k] == None:
				p.next[k] = Node()
			p = p.next[k]
		p.mark = True

	def build(self, s, st):
		n = len(s)
		p = self.root
		for i in range(st, n):
			if p == None:
				return 
			k = ord(s[i]) - ord('a')
			if p.next[k] == None:
				return
			p = p.next[k]
			if p.mark:
				self.g[st].append(i + 1)    # [st, i + 1) is a word in dict
	def path(self, st):
		if st == self.n:
			self.v[st] = 1
			return 1
		if self.v[st] != -1:
			return self.v[st]
		for ed in self.g[st]:
			if self.path(ed):
				self.v[st] = 1
		if self.v[st] == -1:
			self.v[st] = 0
		return self.v[st]

	def get(self, st):
		if st == self.n:
			return []
		res = []
		for ed in self.g[st]:
			if self.v[ed] == 1:
				tmp = self.get(ed)
				ss = self.s[st:ed]
				for sp in tmp:
					res.append(ss + ' ' + sp)
				if tmp == []:
					res.append(ss)
		return res

	def wordBreak(self, s, dict):
		n = len(s)
		self.root = Node()
		self.n = n
		self.s = s
		#self.dict = dict
		self.g = [ [] for i in range(n + 1) ]
		self.v = [ -1 for i in range(n + 1) ]
		for word in dict:
			self.insert(word)
		for i in range(n):
			self.build(s, i)
		ok = self.path(0)
		ret = []
		if ok == 1:
			ret = self.get(0)
		return ret
