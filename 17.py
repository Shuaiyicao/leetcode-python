class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        a = [ [], [], ['a', 'b', 'c' ], [ 'd', 'e', 'f' ], [ 'g', 'h', 'i'], [ 'j', 'k', 'l' ], [ 'm', 'n', 'o' ], [ 'p', 'q', 'r', 's' ], [ 't', 'u', 'v' ], [ 'w', 'x', 'y', 'z' ] ]
        res = [ '' ]
        for d in digits:
            k = int(d)
            tmp = []
            for word in res:
                for w in a[k]:
                    tmp.append(word + w)
            res = tmp
        return res