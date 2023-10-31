from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 0
        count = 0
        for i in nums:
            if i == 1:
                k += 1
                if k > count:
                    count = k
            else:
                k = 0
        return count