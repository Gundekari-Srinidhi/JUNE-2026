class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        count = 0
        while i < n - 1:
            if nums[i] + i >= n-1:
                return count+1 
            j = i + 1
            max1 = 0
            while j <= min(i + nums[i], n - 1):
                if max1 < nums[j] + j:
                    max1 = nums[j] + j
                    val = j 
                j += 1
            count += 1
            i = val
        return count
        


