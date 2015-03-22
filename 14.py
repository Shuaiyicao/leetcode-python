class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
            
        i = 0
        while True:
            if i >= len(strs[0]):
                return strs[0][:i]
            pre = strs[0][i]
            for s in strs:
                if i >= len(s):
                    return strs[0][:i]
                if s[i] != pre:
                    return strs[0][:i]
            i += 1