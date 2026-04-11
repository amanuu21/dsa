1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        if numRows == 1 or numRows >= len(s):
4            return s
5        
6        rows = [""] * numRows
7        current_row = 0
8        going_down = False
9        
10        for char in s:
11            rows[current_row] += char
12            
13            if current_row == 0 or current_row == numRows - 1:
14                going_down = not going_down
15            
16            if going_down:
17                current_row += 1
18            else:
19                current_row -= 1
20        
21        return "".join(rows)