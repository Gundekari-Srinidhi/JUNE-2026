class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ls = [0]
        for i in gain:
            ls.append(ls[-1]+i)
        return max(ls)