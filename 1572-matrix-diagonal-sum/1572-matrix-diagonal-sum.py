class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total_sum = 0
        for i in range(n):
            total_sum += mat[i][i]
            if i != n-1-i:
                total_sum += mat[i][n-1-i]
        return total_sum