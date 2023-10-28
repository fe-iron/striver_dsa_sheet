class Solution:
    def find_factorial(self, num):
        if num == 1:
            return 1
        else:
            return num * self.find_factorial(num-1)
    def generate_next_num(self, current_num):
        new_nums = [1]
        for i in range(len(current_num)-1):
            new_nums.append(current_num[i] + current_num[i+1])
        new_nums.append(1)
        return new_nums

    def generate(self, numRows: int):
        pascal_triangle = [[1], [1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            for i in range(2, numRows):
                new_nums = self.generate_next_num(pascal_triangle[i-1])
                pascal_triangle.append(new_nums)
        return pascal_triangle
    def find_at_rc(self, row, col):
        # using nCr formula which is nCr = !n / (!r * !(n-r)), find r-1Cc-1 to get the reult.
        # r-1 is n and c-1 is r
        n = row-1
        r = col-1
        res = 1
        for i in range(r):
            res = res * (n-i)
            res = res * (i+1)
        
        return res


sol = Solution()
# to print the n number of rows from pascal triagle
print(sol.generate(5))
# to print the nth row
print(sol.generate(5)[-1])
# to print the element at r row and c column
print(sol.find_at_rc(2, 3))