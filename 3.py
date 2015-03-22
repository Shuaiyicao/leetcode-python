class Solution:
    # @return an integer
    def check(self, s, k):
        n = len(s)
        for i in range(n):
            mapper = {}
            ok = True
            #[i, i + k)
            if i + k > n:
                break
            for j in range(i, i + k):
                if s[j] in mapper:
                    ok = False
                    break
                mapper[s[j]] = 1
            if ok:
                return True
        return False
        
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n == 0:
            return 0
        first = 1
        last = min(95, n) + 1
        while first + 1 < last:
            mid = (first + last) / 2
            if self.check(s, mid):
                first = mid
            else:
                last = mid
        return first