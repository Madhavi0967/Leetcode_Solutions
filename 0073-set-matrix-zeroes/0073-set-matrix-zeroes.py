class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        for j in range(n):
            if matrix[0][j]==0:
                first_row_has_zero=True
                break
        for i in range(m):
            if matrix[i][0]==0:
                first_col_has_zero=True
                break
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,m):
            if matrix[i][0]==0:
                for j in range(1,n):
                    matrix[i][j]=0
        for j in range(1,n):
            if matrix[0][j]==0:
                for i in range(1,m):
                    matrix[i][j]=0
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j]=0
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0]=0
        