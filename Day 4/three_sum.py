# below is the leetcode link of the problem
# https://leetcode.com/problems/3sum/description/

class Solution:
    def three_sum(self, nums):
        nums.sort()
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum == 0:
                    output.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
                    while nums[end] == nums[end + 1] and start < end:
                        end -= 1
                elif sum > 0:
                    end -= 1
                else:
                    start += 1
        return output
                        
                

