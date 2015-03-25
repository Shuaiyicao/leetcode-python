class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        n = len(words)
        res = []
        i = 0
        while i < n:
            space = 0
            used = len(words[i])
            j = i + 1
            while j < n:
                if used + space + len(words[j]) + 1 <= L:
                    used += len(words[j])
                    space += 1
                    j += 1
                else:
                    break
            j -= 1  # [i,j]
            left = L - used - space
            if i == j:
                s = words[i] + ' '*left
                res.append(s)
                i = j + 1
                continue
            if j == n - 1:  # last line
                s = words[i]
                for k in range(i + 1,j + 1):
                    s += ' ' + words[k]
                s += ' '*left
                res.append(s)
                i = j + 1
                continue
            s = words[i]
            avg = left / (j - i)
            extr = left % (j - i)
            for k in range(j - i):
                s += ' '*(avg + 1)
                if k < extr:
                    s += ' '
                s += words[i + 1 + k]
            res.append(s)
            i = j + 1
        return res