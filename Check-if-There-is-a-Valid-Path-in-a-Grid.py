1from collections import deque
2
3class Solution:
4    def hasValidPath(self, grid):
5        m, n = len(grid), len(grid[0])
6
7        # Directions for each street type
8        dirs = {
9            1: [(0, -1), (0, 1)],     # left, right
10            2: [(-1, 0), (1, 0)],     # up, down
11            3: [(0, -1), (1, 0)],     # left, down
12            4: [(0, 1), (1, 0)],      # right, down
13            5: [(0, -1), (-1, 0)],    # left, up
14            6: [(0, 1), (-1, 0)]      # right, up
15        }
16
17        visited = [[False]*n for _ in range(m)]
18        q = deque([(0, 0)])
19        visited[0][0] = True
20
21        while q:
22            i, j = q.popleft()
23
24            if i == m - 1 and j == n - 1:
25                return True
26
27            for dx, dy in dirs[grid[i][j]]:
28                ni, nj = i + dx, j + dy
29
30                if not (0 <= ni < m and 0 <= nj < n):
31                    continue
32                if visited[ni][nj]:
33                    continue
34
35                # Check if next cell connects back
36                for bdx, bdy in dirs[grid[ni][nj]]:
37                    if ni + bdx == i and nj + bdy == j:
38                        visited[ni][nj] = True
39                        q.append((ni, nj))
40                        break
41
42        return False