class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = [ '/' ]
        a = path.split('/')
        for f in a:
            if f == '' or f == '.':
                continue
            if f == '..':
                if len(stack) > 1:
                    stack.pop()
            else:
                stack.append(f)
        res = ''
        for f in stack[1:]:
            res += '/' + f
        if res == '':
            res = '/'
        return res