class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        n = len(s)
        if n == 0:
            return 0
        res = 0
        st = 0
        stack = []
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    st = i + 1
                else:
                    t = stack.pop()
                    if len(stack) == 0:
                        res = max(res, i - st + 1)
                    else:
                        res = max(res, i - stack[-1])
        return res