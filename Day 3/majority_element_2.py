class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Optimal
        result1, result2, count1, count2 = 0, 0, 0, 0
        for ele in nums:
            if count1 == 0 and ele != result2:
                count1 = 1
                result1 = ele
            elif count2 == 0 and ele != result1:
                count2 = 1
                result2 = ele
            elif result1 == ele:
                count1 += 1
            elif result2 == ele:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        for i in nums:
            if i == result1:
                count1 += 1
            elif i == result2:
                count2 += 1
        result = []
        if count1 > len(nums) // 3:
            result.append(result1)
        if count2 > len(nums) // 3:
            result.append(result2)
        return result
    
sol = Solution()
sol.majorityElement([3,2,3])