1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        # Create DP table
4        dp = [[1] * n for _ in range(m)]
5        
6        # Fill the DP table
7        for i in range(1, m):
8            for j in range(1, n):
9                dp[i][j] = dp[i-1][j] + dp[i][j-1]
10        
11        return dp[m-1][n-1]
12
13
14# Space-optimized DP (O(n) space)
15class SolutionOptimized:
16    def uniquePaths(self, m: int, n: int) -> int:
17        # Use 1D array to save space
18        dp = [1] * n
19        
20        for i in range(1, m):
21            for j in range(1, n):
22                dp[j] += dp[j-1]
23        
24        return dp[n-1]