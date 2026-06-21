class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs.sort()
        sum1 = 0
        for i in costs:
            sum1 += i
            count +=1
            if sum1 > coins:
                sum1 -= i
                count -= 1
                break
            if sum1 == coins:
                break
        return count
                

            

        