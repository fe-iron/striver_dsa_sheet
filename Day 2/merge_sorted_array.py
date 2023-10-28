import math

# optimal solution 1

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            left = 0
        else:
            left = m-1
        right = 0
        nums1 = [i for i in nums1 if i != 0]
        for i in range(m+n):
            if nums1[left] > nums2[right]:
                nums1[left], nums2[right] = nums2[right], nums1[left]
                left -= 1
                right += 1
            elif nums1[left] <= nums2[right]:
                break
        nums1 = nums1 + nums2
         
# this is optimal solution 2 by GAP METHOD

class SoltionGap():
    def merge(self, nums1, m, nums2, n):
        nums1 = [i for i in nums1 if i != 0]
        nums1 = nums1 + nums2
        gap = math.ceil((m+n)/2)
        l = m + n
        while gap > 0:
            left, right = 0, gap
            while right < l:
                if nums1[left] > nums1[right]:
                    nums1[left], nums1[right] = nums1[right], nums1[left]
                left += 1
                right += 1
            if gap == 1:
                break
            gap = math.ceil(gap/2)
        nums1



sol = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
sol.merge()