1class Solution:
2    def isValidSudoku(self, board: list[list[str]]) -> bool:
3        rows = [set() for _ in range(9)]
4        cols = [set() for _ in range(9)]
5        boxes = [set() for _ in range(9)]
6        
7        for r in range(9):
8            for c in range(9):
9                val = board[r][c]
10                
11                if val == '.':
12                    continue
13                
14                # Compute box index
15                box_index = (r // 3) * 3 + (c // 3)
16                
17                # Check duplicates
18                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
19                    return False
20                
21                # Mark as seen
22                rows[r].add(val)
23                cols[c].add(val)
24                boxes[box_index].add(val)
25        
26        return True