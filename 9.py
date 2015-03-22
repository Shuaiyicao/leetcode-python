class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True