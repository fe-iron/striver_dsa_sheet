class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # n = len(nums) // 2
        # keys = []
        # for i in nums:
        #     if i not in keys:
        #         keys.append(i)
        # values = [0 for i in keys]
        # hashmap = dict(zip(keys, values))
        # for i in nums:
        #     hashmap[i] = hashmap[i] + 1
        # for key, val in hashmap.items():
        #     if val > n:
        #         return key
        # return 0

        # Optimal solution based on MOORE'S VOTING ALGORITHM
        result, count = 0, 0
        for ele in nums:
            if count == 0:
                count = 1
                result = ele
            elif result == ele:
                count += 1
            else:
                count -= 1
        count = 0
        for i in nums:
            if i == result:
                count += 1
        if count > len(nums) // 2:
            return result
        return 0
    
sol = Solution()
sol.majorityElement([3,3,4])