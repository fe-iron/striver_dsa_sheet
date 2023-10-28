class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # to solve in one line
        # matrix[:]=list(zip(*matrix[::-1]))
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for i, row in enumerate(matrix):
            matrix[i] = row[::-1]
        # for priniting matrix        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print(matrix[i][j], end=' ')
            print()


sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol.rotate(matrix)