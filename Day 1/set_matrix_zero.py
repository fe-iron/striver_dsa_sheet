"""
    OPTIMAL SOLUTION
"""

def set_zero_matrix(matrix):
    col_zero = 1
    m = len(matrix)
    n = len(matrix[0])
    # marking first row and column as zero whenever finds 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0

                if j != 0:
                    matrix[0][j] = 0
                else:
                    col_zero = 0

    # marking all numbers zero  other than 0,0 index, if first place if zero
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] != 0:
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

    # marking 0 to first place also
    # marking 0 to coumns only because first row would automatically come in column
    if matrix[0][0] == 0:
            for i in range(n):
                matrix[0][i] = 0
                
    if not col_zero:
        for i in range(m):
            matrix[i][0] = 0
            
if "__main__" == __name__:
        # Write your code here.
    matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    for i in matrix:
        for j in i:
            if j == -1:
                j = 0
            print(j, end=" ")
        print()
    
    set_zero_matrix(matrix)
    
    for i in matrix:
        for j in i:
            if j == -1:
                j = 0
            print(j, end=" ")
        print()