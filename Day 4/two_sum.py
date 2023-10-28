class SolutionBetter:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        # creating hashmap with nums value as key and indices as value
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        index = 0
        for i in range(len(nums)):
            try:
                index = hash_map[target - nums[i]]
                if index != i:
                    return [i, index]
            except KeyError:
                pass
        return []
        
class SolutionOptimal:
    def merge_sort(self, nums, low, high, mid):
        right = mid + 1
        left = low
        temp = []
        while left <= mid and right <= high:
            if nums[left][1] <= nums[right][1]:
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

    def call_merge(self, nums, low, high):
        if low >= high:
            return 0
        mid = (low + high) // 2
        self.call_merge(nums, low, mid)
        self.call_merge(nums, mid+1, high)
        self.merge_sort(nums, low, high, mid)


    def twoSum(self, nums: list[int], target: int):
        for i in range(len(nums)):
            nums[i] = [i, nums[i]]
        self.call_merge(nums, 0, len(nums)-1)
        low, high = 0, len(nums) - 1
        for i in range(len(nums)):
            if nums[low][1] + nums[high][1] == target:
                return [nums[low][0], nums[high][0]]
            elif nums[low][1] + nums[high][1] > target:
                high -= 1
            else:
                low += 1
            if low >= high:
                return []

sol = SolutionOptimal()
sol.twoSum([3,2,4], 6)
