class Solution:
	# @return a boolean
	def isInterleave(self, s1, s2, s3):
		if s1 == "":
			return s2 == s3
		if s2 == "":
			return s1 == s3
		if len(s3) != len(s1) + len(s2):
			return False
		n = len(s3)
		m = len(s1)
		dp = [ [ False for i in range(m + 1) ] for j in range(n + 1) ]
		dp[0][0] = True
		for i in range(1, n + 1):
			for j in range(0, min(i + 1, m + 1)):
				if j == 0 :
					dp[i][j] = i - 1 < len(s2) and dp[i-1][j] and s3[i-1] == s2[i-1]
					continue
				if s3[i-1] == s1[j-1] and dp[i-1][j-1]:
					dp[i][j] = True

				if i > j and i - j - 1 < len(s2) and s3[i-1] == s2[i-j-1] and dp[i-1][j]:
					dp[i][j] = True
				#print 'dp[%d][%d] = %d' % (i, j, dp[i][j])
		return dp[n][m]
