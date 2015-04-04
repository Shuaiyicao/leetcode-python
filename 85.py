class Solution:
	# @param matrix, a list of lists of 1 length string
	# @return an integer
	def gao(self, line):
		stack = []
		n = len(line)
		res = 0
		for i in range(n):
			if len(stack) == 0 or line[i] > stack[-1][0]:
				stack.append((line[i], i))
				continue
			while len(stack) > 0 and line[i] <= stack[-1][0]:
				height, idx = stack.pop()
				res = max(res, height * (i - idx))
			stack.append((line[i], idx))

		while len(stack) > 0:
			height, idx = stack.pop()
			res = max(res, height * (n - idx))
		return res

	def maximalRectangle(self, matrix):
		if len(matrix) == 0:
			return 0

		m = len(matrix)
		n = len(matrix[0])
		a = [ [ 0 for j in range(n) ] for i in range(m) ]

		for i in range(n):
			for j in range(m):
				if j == 0:
					a[j][i] = int(matrix[j][i])
				elif int(matrix[j][i]) == 1:
					a[j][i] = a[j-1][i] + 1

		res = 0
		for i in range(m):
			res = max(res, self.gao(a[i]))

		#print res
					
		return res

#a = Solution()
#a.maximalRectangle([['010100'], ['011001'], ['111010'], ['000001']])