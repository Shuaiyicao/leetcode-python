class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    
    def strStr(self, haystack, needle):
        k = haystack.find(needle)
        if k == -1:
            return None
        return haystack[k:]