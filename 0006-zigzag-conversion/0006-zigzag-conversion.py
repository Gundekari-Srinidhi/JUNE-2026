class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = []
        for i in range(numRows):
            l.append([])
        n = len(s)
        j = 0
        i = 0
        while i <= n:
            while j < numRows and i < n:
                l[j].append(s[i])
                j += 1
                i += 1
            j = numRows-2
            if i == n:
                break
            while j >= 1 and i < n:
                l[j].append(s[i])
                j -= 1
                i += 1
            j = 0
        s1 = ""
        for i in l:
            s1+= "".join(i)
        return s1
        