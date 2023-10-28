class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # i = 0
        # target_row = -1
        # for row in matrix:
        #     if target <= row[-1]:
        #         target_row = i
        #         break
        #     i += 1
        # if target_row == -1:
        #     return False
        # for i in range(len(matrix[target_row])):
        #     if matrix[target_row][i] == target:
        #         return True
        # return False

        # Binary search
        low = 0,
        m = len(matrix)
        n = len(matrix[0])
        high = m * n -1
        while low <= high:
            mid = (low + high) // 2
            row = mid / m
            col = mid % m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid -1
        return False
        
sol = Solution()
sol.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=13)