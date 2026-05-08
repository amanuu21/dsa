1from typing import List
2
3class Solution:
4    def generateMatrix(self, n: int) -> List[List[int]]:
5        # Initialize matrix with zeros
6        matrix = [[0] * n for _ in range(n)]
7        
8        # Define boundaries
9        top, bottom = 0, n - 1
10        left, right = 0, n - 1
11        
12        num = 1
13        
14        while top <= bottom and left <= right:
15            # Fill top row (left to right)
16            for col in range(left, right + 1):
17                matrix[top][col] = num
18                num += 1
19            top += 1
20            
21            # Fill right column (top to bottom)
22            for row in range(top, bottom + 1):
23                matrix[row][right] = num
24                num += 1
25            right -= 1
26            
27            # Fill bottom row (right to left)
28            if top <= bottom:
29                for col in range(right, left - 1, -1):
30                    matrix[bottom][col] = num
31                    num += 1
32                bottom -= 1
33            
34            # Fill left column (bottom to top)
35            if left <= right:
36                for row in range(bottom, top - 1, -1):
37                    matrix[row][left] = num
38                    num += 1
39                left += 1
40        
41        return matrix