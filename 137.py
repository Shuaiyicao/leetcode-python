class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = twos = threes = 0
        for x in A:
            twos |= ones & x
            ones ^= x
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones
