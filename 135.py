class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        n = len(ratings)
        if n == 1:
            return 1
        res = 1
        last = 1
        i = 0
        while i < n:
            if ratings[i] == ratings[i+1]:
                len_t = 1
                while i + 1 < n and ratings[i] == ratings[i+1]:
                    len_t += 1
                    i += 1
                res += len_t - 1
                last = 1
                
            elif ratings[i] > ratings[i+1]:
                len_t = 1
                while i + 1 < n and ratings[i] > ratings[i+1]:
                    i += 1
                    len_t += 1
                if last >= len_t:
                    res += (len_t - 1) * len_t / 2
                else:
                    res += (len_t + 1) * len_t / 2 - last
                last = 1
                
            else:
                len_t = 1
                while i + 1 < n and ratings[i] < ratings[i+1]:
                    i += 1
                    len_t += 1
                res += (len_t + 1) * len_t / 2 - 1
                last = len_t
            if i == n - 1:
                break
        return res