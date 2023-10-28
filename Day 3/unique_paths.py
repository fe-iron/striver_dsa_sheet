# Brute Force
class SolutionBruteForce:
    def recursive_paths(self, i, j, m, n):
        if i >= m or j >= n:
            return 0
        elif i == m-1 and j == n-1:
            return 1
        return self.recursive_paths(i+1, j, m, n) + self.recursive_paths(i, j+1, m, n)


    def uniquePaths(self, m: int, n: int) -> int:
        # brute force
        print(self.recursive_paths(0, 0, m, n))

# Better Solution by Dynamic programming
class SolutionBetter:
    def recursive_paths(self, i, j, m, n, hash_table):
        if i >= m or j >= n:
            return 0
        if i == m-1 and j == n-1:
            return 1
        if hash_table[i][j] != -1:
            return hash_table[i][j]
        else:
            hash_table[i][j] = self.recursive_paths(i+1, j, m, n, hash_table) + self.recursive_paths(i, j+1, m, n, hash_table)
            return hash_table[i][j]


    def uniquePaths(self, m: int, n: int) -> int:
        hash_table = [[-1]*n]*m
        print(self.recursive_paths(0, 0, m, n, hash_table))

# Optimal Solution
class SolutionOptimal:
    def uniquePaths(self, m: int, n: int) -> int:
        N = n + m - 2 # total no of steps i.e., total_steps = rows + cols - 2
        R = m - 1 
        # In steps me se down steps kitne lene hai. (No. of ways to select down steps from total steps)
        # due to that using nCr
        result = 1
        for i in range(1, R+1):
            result = result * (N - R + i) / i
        return int(result)




sol = SolutionOptimal()
sol.uniquePaths(3, 7)
