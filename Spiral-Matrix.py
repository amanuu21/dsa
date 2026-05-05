1from typing import List
2
3class Solution:
4    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
5        if not matrix or not matrix[0]:
6            return []
7        
8        result = []
9        top, bottom = 0, len(matrix) - 1
10        left, right = 0, len(matrix[0]) - 1
11        
12        while top <= bottom and left <= right:
13            # Traverse from left to right along the top row
14            for col in range(left, right + 1):
15                result.append(matrix[top][col])
16            top += 1
17            
18            # Traverse from top to bottom along the right column
19            for row in range(top, bottom + 1):
20                result.append(matrix[row][right])
21            right -= 1
22            
23            # Traverse from right to left along the bottom row (if still within bounds)
24            if top <= bottom:
25                for col in range(right, left - 1, -1):
26                    result.append(matrix[bottom][col])
27                bottom -= 1
28            
29            # Traverse from bottom to top along the left column (if still within bounds)
30            if left <= right:
31                for row in range(bottom, top - 1, -1):
32                    result.append(matrix[row][left])
33                left += 1
34        
35        return result