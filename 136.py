class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for x in A:
            res ^= x
        return res