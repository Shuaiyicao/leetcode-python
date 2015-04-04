class Solution:
    # @param s, a string
    # @return a list of strings
    def get_ip(self, s, i, j, k):
        return s[:i+1] + '.' + s[i+1:j+1] + '.' + s[j+1:k+1] + '.' + s[k+1:]
        
    def restoreIpAddresses(self, s):
        n = len(s)
        if n > 12 or n < 4:
            return []
        res = []
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n - 1):
                    ip = self.get_ip(s, i, j, k)
                    t_ip = ip.split('.')
                    ok = True
                    for item in t_ip:
                        if str(int(item)) != item or int(item) > 255:
                            ok = False
                            break
                        
                    if ok:
                        res.append(ip)
        return res