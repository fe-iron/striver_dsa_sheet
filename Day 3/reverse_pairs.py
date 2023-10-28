class Solution:
    def merge_sort(self, nums, low, high, mid):
        left = low
        right = mid + 1
        temp = []
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1
        for i in range(low, high+1):
            nums[i] = temp[i - low]


    def calculate(self, nums, low, high, mid):
        right = mid + 1
        count = 0
        for i in range(low, mid+1):
            right = mid + 1
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1
            count += right - (mid + 1)
        return count

    def call_merge(self, nums, low, high):
        if low >= high:
            return 0
        count = 0
        mid = (low + high) // 2
        count += self.call_merge(nums, low, mid)
        count += self.call_merge(nums, mid+1, high)
        count += self.calculate(nums, low, high, mid)
        self.merge_sort(nums, low, high, mid)
        return count

    def reversePairs(self, nums: list[int]) -> int:
        count = self.call_merge(nums, 0, len(nums)-1)
        print(count)


sol = Solution()
sol.reversePairs([2,4,3,5,1])