1class Solution:
2    def minPathSum(self, grid: List[List[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4
5        # Fill first row
6        for j in range(1, n):
7            grid[0][j] += grid[0][j - 1]
8
9        # Fill first column
10        for i in range(1, m):
11            grid[i][0] += grid[i - 1][0]
12
13        # Fill the rest
14        for i in range(1, m):
15            for j in range(1, n):
16                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
17
18        return grid[m - 1][n - 1]
19        