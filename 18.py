class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        n = len(num)
        if n < 4:
            return []
        num.sort()
        mapper = {}
        for i in range(n):
            for j in range(i + 1, n):
                if num[i] + num[j] not in mapper:
                    mapper[num[i] + num[j]] =[ (i, j) ]
                else:
                    mapper[num[i] + num[j]].append( (i, j) )
        ret = set()
        for i in range(n):
            for j in range(i + 1, n):
                need = target - num[i] - num[j]
                if need not in mapper:
                    continue
                for k, l in mapper[need]:
                    if k <= j:
                        continue
                    ret.add( (num[i], num[j], num[k], num[l]) )
        res = []
        for item in ret:
            res.append(list(item))
        return res