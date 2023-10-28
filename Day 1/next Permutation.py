"""
    
"""

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break
        if index == -1:
            return nums[::-1]
        for i in range(n-1, index, -1):
            if nums[i] > nums[index]:
                nums[index], nums[i]  = nums[i], nums[index]
        return nums[:index+1] + nums[n:index:-1]

sol = Solution()
print(sol.nextPermutation([1,3,2]))