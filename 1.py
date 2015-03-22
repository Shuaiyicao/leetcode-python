class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        mapper = {}
        n = len(num)
        for i in range(n):
            mapper[num[i]] = i
        for i in range(n):
            if target - num[i] in mapper and mapper[target - num[i]] != i:
                return (i + 1, mapper[target - num[i]] + 1)
        return (-1, -1)