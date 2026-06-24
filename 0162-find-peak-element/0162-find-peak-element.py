class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        ind = 0
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                ind = i+1
            else:
                return ind
        return ind
        