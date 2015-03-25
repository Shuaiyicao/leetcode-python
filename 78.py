class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        n = len(S)
        res = set()
        for i in range(1<<n):
            tmp = []
            for j in range(n):
                if (1<<j) & i > 0:
                    tmp.append(S[j])
            res.add(tuple(tmp))
        ret = []
        for item in res:
            ret.append(list(item))
        return ret