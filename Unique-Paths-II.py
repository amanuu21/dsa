1from typing import List
2
3class Solution:
4    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
5        m = len(obstacleGrid)
6        n = len(obstacleGrid[0])
7        
8        # If start or end is obstacle, no path
9        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
10            return 0
11        
12        # dp table
13        dp = [[0] * n for _ in range(m)]
14        
15        # Starting point
16        dp[0][0] = 1
17        
18        # Fill first column
19        for i in range(1, m):
20            if obstacleGrid[i][0] == 0:
21                dp[i][0] = dp[i-1][0]
22        
23        # Fill first row
24        for j in range(1, n):
25            if obstacleGrid[0][j] == 0:
26                dp[0][j] = dp[0][j-1]
27        
28        # Fill rest of the grid
29        for i in range(1, m):
30            for j in range(1, n):
31                if obstacleGrid[i][j] == 0:
32                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
33        
34        return dp[m-1][n-1]