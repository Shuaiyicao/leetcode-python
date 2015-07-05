def cal(x, y, op):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        else:
            return (int)(1.0 * x / y)
            
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        res = 0
        stk = []
        for item in tokens:
            if item == '+' or item == '-' or item == '*' or item == '/':
                x = stk.pop()
                y = stk.pop()
                stk.append(cal(int(y), int(x), item))
            else:
                stk.append(item)
        return int(stk[0])
