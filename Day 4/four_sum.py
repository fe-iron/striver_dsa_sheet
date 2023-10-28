# below is the leetcode link of the problem
# https://leetcode.com/problems/3sum/description/

class Solution:
    def four_sum(self, nums, target):
        nums.sort()
        output = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                start = j + 1
                end = n - 1
                while start < end:
                    sum = nums[i] + nums[j] + nums[start] + nums[end]
                    if sum == target:
                        output.append([nums[i], nums[j], nums[start], nums[end]])
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
                        
                

