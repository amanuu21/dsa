1from typing import List
2
3class Solution:
4    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
5        m, n = len(boxGrid), len(boxGrid[0])
6
7        # Step 1: Apply gravity in the original box
8        for r in range(m):
9            # Use two pointers to move stones down in the current row
10            # Actually, gravity pulls down -> from bottom to top in each column
11            # But easier: from bottom of each column, move stones down
12            for c in range(n):
13                if boxGrid[r][c] == '#':
14                    # Find next empty spot below
15                    fall_to = c
16                    for k in range(c + 1, n):
17                        if boxGrid[r][k] == '*':
18                            break
19                        if boxGrid[r][k] == '.':
20                            fall_to = k
21                    # Swap if needed
22                    if fall_to != c:
23                        boxGrid[r][fall_to] = '#'
24                        boxGrid[r][c] = '.'
25
26        # Step 2: Rotate 90 degrees clockwise
27        rotated = [['.' for _ in range(m)] for _ in range(n)]
28        for r in range(m):
29            for c in range(n):
30                # After rotation: new row = c, new col = m - 1 - r
31                rotated[c][m - 1 - r] = boxGrid[r][c]
32
33        return rotated