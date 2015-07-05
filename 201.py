class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def judge(self, k, m, n):
        sum = 0
        for i in range(30, -1, -1):
            if i == k or (1<<i) + sum > n:
                continue
            sum += 1<<i
            if sum >= m and sum <= n:
                return True
        return False
        
    def rangeBitwiseAnd(self, m, n):
        sum = 0
        for i in range(30, -1, -1):
            if self.judge(i, m, n):
                sum += 1<<i
        return sum

so = Solution()
print so.rangeBitwiseAnd(2147483647, 2147483647)
