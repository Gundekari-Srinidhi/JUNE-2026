class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        
        n = len(candyType)
        k = n//2
        val = set(candyType)
        if len(val) > k:
            return k
        return len(val)
        