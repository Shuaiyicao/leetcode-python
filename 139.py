
class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a boolean
	def match(self, a, b):
		if len(a) > len(b):
			return []
		x = len(a)
		y = len(b)
		res = []
		for i in range(y):
			if a == b[i:i+x]:
				res.append((i, i + x - 1))
		return res

	def wordBreak(self, s, dict):
		seg = []
		for word in dict:
			seg.extend(self.match(word, s))
		#seg.sort()
		got = {}
		got[-1] = 1
		l = len(s)
		for i in range(l):
			for sub in seg:
				if sub[1] == i and got.get(sub[0] - 1) == 1:
					got[i] = 1
					break

		return got.get(l-1) == 1
