class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        a = s.split(' ')
        for word in reversed(a):
            if word != '':
                return len(word)
        return 0