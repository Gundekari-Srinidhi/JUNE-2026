class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        val = abs(30*(hour)-5.5*(minutes))
        return min(val,360-val)
        