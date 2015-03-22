class Solution:
    # @return a boolean
    def isValid(self, s):
        if s == '':
            return True
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if s[i] == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif s[i] == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0