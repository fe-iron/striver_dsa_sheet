"""
    OPTIMAL SOLUTION
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max = float('-inf')
        current_sum = 0
        for i in nums:
            current_sum += i
            if current_sum > max:
                max = current_sum
            if current_sum < 0:
                current_sum = 0
        return max
    
sol = Solution()
sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

