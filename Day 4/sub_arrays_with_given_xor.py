from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        max_len = 0
        xor = 0
        hash_map = defaultdict(int)
        hash_map[xor] = 1
        for i in range(len(A)):
            # prefix XOR till index i:
            xor = xor ^ A[i]

            # By formula: x = xr^k:
            x = xor ^ B

            # add the occurrence of xr^k
            # to the count:
            max_len += hash_map[x]

            # Insert the prefix xor till index i
            # into the dictionary:
            hash_map[xor] += 1
            
        return max_len
    

sol = Solution()
sol.solve(A=[5, 6, 7, 8, 9], B=5)