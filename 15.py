class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        n = len(num)
        if n < 3:
            return [  ]
        num.sort()
        res = set()
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == 0:
                    res.add( (num[i], num[j], num[k]) )
                    j += 1
                    k -= 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1
        ret = []
        for item in res:
            ret.append(list(item))
        return ret