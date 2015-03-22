class Solution:
	# @return an integer


	def threeSumClosest(self, num, target):
		n = len(num)
		ret = 1<<30
		num.sort()
		for i in range(n):
			j = i + 1
			k = n - 1
			while j < k:
				sum = num[i] + num[j] + num[k];
				if abs(sum - target) < abs(ret - target):
					ret = sum
				if sum > target:
					k -= 1
				else:
					j += 1
			if ret == target:
				return target
		#print ret
		return ret