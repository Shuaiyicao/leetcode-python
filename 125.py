class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) == 0:
            return True
            
        a = []
        for c in s:
            if c.isalpha():
			    a.append(c.lower())
            elif c.isdigit():
                a.append(c)
        
        n = len(a)
        fr = 0
        ed = n - 1
        while fr <= ed:
            if a[fr] != a[ed]:
                return False
            fr += 1
            ed -= 1
        return True


