1from typing import List
2
3class Solution:
4    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
5        if not grid or not grid[0]:
6            return -1
7        
8        m, n = len(grid), len(grid[0])
9        
10        # dp[i][j] will be a dictionary mapping cost -> max score to reach (i, j)
11        dp = [[{} for _ in range(n)] for _ in range(m)]
12        
13        # Initialize starting cell
14        start_cost = 1 if grid[0][0] == 2 else grid[0][0]
15        start_score = grid[0][0]
16        
17        # Only add the starting cell if its cost doesn't exceed k
18        if start_cost <= k:
19            dp[0][0][start_cost] = start_score
20        
21        # Fill the DP table
22        for i in range(m):
23            for j in range(n):
24                if i == 0 and j == 0:
25                    continue
26                
27                # Current cell's cost and score contribution
28                cell_value = grid[i][j]
29                current_cost = 1 if cell_value == 2 else cell_value
30                current_score = cell_value
31                
32                # Try coming from top (i-1, j)
33                if i > 0:
34                    for prev_cost, prev_score in dp[i-1][j].items():
35                        total_cost = prev_cost + current_cost
36                        total_score = prev_score + current_score
37                        
38                        if total_cost <= k:
39                            if total_cost not in dp[i][j] or dp[i][j][total_cost] < total_score:
40                                dp[i][j][total_cost] = total_score
41                
42                # Try coming from left (i, j-1)
43                if j > 0:
44                    for prev_cost, prev_score in dp[i][j-1].items():
45                        total_cost = prev_cost + current_cost
46                        total_score = prev_score + current_score
47                        
48                        if total_cost <= k:
49                            if total_cost not in dp[i][j] or dp[i][j][total_cost] < total_score:
50                                dp[i][j][total_cost] = total_score
51        
52        # If we can't reach the bottom-right cell, return -1
53        if not dp[m-1][n-1]:
54            return -1
55        
56        # Return the maximum score among all valid costs
57        return max(dp[m-1][n-1].values())