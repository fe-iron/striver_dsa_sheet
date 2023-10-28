class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]

sol = Solution()
sol.findDuplicate(nums=[3,1,3,4,2])