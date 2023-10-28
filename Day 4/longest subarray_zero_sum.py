from typing import List
def maxLen(A: List[int], n: int) -> int:
    mpp = {}
    maxi = 0
    sum = 0
    for i in range(len(A)):
        sum += A[i]
        if sum == n:
            maxi = i + 1
        else:
            if sum in mpp:
                maxi = max(maxi, i - mpp[sum])
            else:
                mpp[sum] = i
    return maxi


maxLen([10, 5, 2, 7, 1, 9], 15)