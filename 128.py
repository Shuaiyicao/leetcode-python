class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        sted = {}
        n = len(num)
        for item in num:
            if item in sted:
                continue
            sted[item] = item
            if item-1 in sted:
                sted[item] = sted[item-1]
                sted[sted[item-1]] = item
            if item+1 in sted:
                tmp = sted[item+1]
                sted[tmp] = sted[item]
                sted[sted[item]] = tmp
        
        res = 0
        for item in sted:
            res = max(res, sted[item] - item)
        return res + 1