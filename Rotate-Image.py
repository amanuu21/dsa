1from typing import List
2
3class Solution:
4    def rotate(self, matrix: List[List[int]]) -> None:
5        """
6        Do not return anything, modify matrix in-place instead.
7        """
8        n = len(matrix)
9        
10        # Step 1: Transpose the matrix (swap rows with columns)
11        for i in range(n):
12            for j in range(i + 1, n):
13                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
14        
15        # Step 2: Reverse each row
16        for i in range(n):
17            matrix[i].reverse()