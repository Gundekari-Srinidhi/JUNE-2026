class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max1 = max(nums)
        min1 = min(nums)
        return (max1 - min1)*k
        