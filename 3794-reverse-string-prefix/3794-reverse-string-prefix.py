class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        s1 =""
        val = s[:k]
        s1 = val[::-1] + s[k:]
        return s1
        