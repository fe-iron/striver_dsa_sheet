"""
    OPTIMAL SOLUTIONS
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for j in range(len(nums)-1):
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums
    

sol = Solution()
print(sol.sortColors([2,0,2,1,1,0]))

