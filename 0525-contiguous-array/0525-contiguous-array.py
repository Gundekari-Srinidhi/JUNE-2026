class Solution:
    def findMaxLength(self, nums: List[int]):

        n = len(nums)
        s = [-1] * n

        for i in range(n):
            if nums[i] == 1:
                s[i] = 1

        for i in range(1, n):
            s[i] += s[i-1]

        d = {0: -1}
        max1 = 0

        for i in range(n):
            if s[i] in d:
                max1 = max(max1, i - d[s[i]])
            else:
                d[s[i]] = i

        return max1