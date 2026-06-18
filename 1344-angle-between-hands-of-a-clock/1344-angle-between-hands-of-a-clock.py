class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #hour hand moves 30 degree per hour and 0.5 degree per minute and minute hand moves 6 degree per minute  30(H) + 0.5(M) - 6(M)
        val = abs(30*(hour)-5.5*(minutes))
        return min(val,360-val)
        