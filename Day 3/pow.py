class Solution:
    def myPow(self, x: float, n: int) -> float:
        pow = 1
        # if n < 0:
        #     n = abs(n)
        #     while n > 0:
        #         pow *= x
        #         n -= 1
        #     pow = 1 / pow
        # else:
        #     while n > 0:
        #         pow *= x
        #         n -= 1
        # print(pow)

        # Optimal solution
        temp_n = n
        temp_n = abs(temp_n)
        while temp_n > 0:
            if temp_n % 2 == 0:
                temp_n = temp_n // 2
                x = x * x
            else:
                pow = pow * x
                temp_n = temp_n - 1
        if n < 0:
            pow = 1 / pow
        return pow


sol = Solution()
sol.myPow(0.00001, 2147483647)
            