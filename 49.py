class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        if len(strs) == 0:
            return []
        a = []
        for i in range(len(strs)):
            a.append((''.join(sorted(list(strs[i]))), i))
        a.sort(key=lambda t:t[0])
        n = len(strs)
        i = 0
        res = []
        while i < n:
            if i < n - 1 and a[i][0] == a[i+1][0]:
                while i < n - 1 and a[i][0] == a[i+1][0]:
                    res.append(strs[a[i][1]])
                    i += 1
                res.append(strs[a[i][1]])
                i += 1
            else:
                i += 1
        return res