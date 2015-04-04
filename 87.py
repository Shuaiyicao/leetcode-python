class Solution:
	# @return a boolean
	def isScramble(self, s1, s2):
		n = len(s1)
		if sorted(s1) != sorted(s2):
			return False
		if n <= 2 or s1 == s2:
			return sorted(s1) == sorted(s2)
		for i in range(1, n):
			if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
				return True
			if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:n-i]):
				return True
		return False
