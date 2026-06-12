class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro = 1
        sum1 = 0
        while n > 0:
            rem = n%10
            pro *= rem
            sum1 += rem
            n //= 10
        return pro - sum1
        