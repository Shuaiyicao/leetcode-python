class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if s == '':
            return s
        
        a = s.split()
        words = []
        first = True
        for item in reversed(a):
           words.append(item)
        return ' '.join(words)
