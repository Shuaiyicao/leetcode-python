
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        left = []
        p = 0
        min_left = 1<<20
        for i in range(n):
            min_left = min(min_left, p)
            left.append(p)
            p += gas[i] - cost[i]
        left.append(p)
        min_left = min(min_left, p)
        
        if min_left >= 0:
            return 0
        
        fr = n - 1
        p = 0
        while fr > 0:
            p += gas[fr] - cost[fr]
            if p + min_left >= 0:
                return fr
            fr -= 1
        return -1
