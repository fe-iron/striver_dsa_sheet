class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_pro = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_pro = max(max_pro, prices[i]-min_price)
        return max_pro

    
sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))

            
