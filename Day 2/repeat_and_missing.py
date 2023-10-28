class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        A.sort()
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                a = A[i]
                break
        for i in range(len(A)-1):
            if A[i] + 1 != A[i + 1]:
                b = A[i] + 1
                break
        return [a, b]
            

sol = Solution()
sol.repeatedNumber(A=[3, 1, 2, 5, 3])