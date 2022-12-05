class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        d = {'c':0,'r':0,'o':0,'a':0,'k':0}
        ans = 0
        for c in croakOfFrogs:
            d[c] += int(1)
            if not (d['c'] >= d['r'] >= d['o'] >= d['a'] >= d['k']):
                return -1
            dv = d.values()
            ans = max(ans, max(dv) - min(dv))
        if len(set(d.values())) != 1:
            return -1
        return ans

s = Solution()
print(s.minNumberOfFrogs("croakcrook"))
