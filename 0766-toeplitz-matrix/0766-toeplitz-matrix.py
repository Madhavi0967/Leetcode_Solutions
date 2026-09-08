class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        for r in range(rows):
            for c in range(columns):
                if r>0 and c>0 and matrix[r][c]!=matrix[r-1][c-1]:
                    return False
        return True