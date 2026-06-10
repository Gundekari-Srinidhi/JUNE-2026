class Solution:
    def maxFreqSum(self, s: str) -> int:
        d1 = ['a','e','i','o','u']
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        vol = 0
        con = 0
        for k,v in d.items():
            if k in d1:
                vol = max(vol,v)
            else:
                con = max(con,v)
        return vol+con
        