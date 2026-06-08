class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lf  = []
        mid = []
        rf = []
        for i in nums:
            if i < pivot:
                lf.append(i)
            elif i > pivot:
                rf.append(i)
            else:
                mid.append(i)
        lf.extend(mid)
        lf.extend(rf)
        return lf
        