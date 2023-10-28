class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) == 1:
            return 1
        count1, temp1 = [], []
        k = 0
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                temp1.append(nums[i])
                if i+1 == len(nums) - 1:
                    temp1.append(nums[i])
                    count1.append(temp1)    
            else:
                temp1.append(nums[i])
                count1.append(temp1)
                temp1 = []
                k += 1
        count = 0
        for i in count1:
            if len(i) > count:
                count = len(i)
        return count



sol = Solution()
sol.longestConsecutive(nums=[0,0])
        