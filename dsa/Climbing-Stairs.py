1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n <= 2:
4            return n
5        
6        # dp[i] = number of ways to reach step i
7        dp = [0] * (n + 1)
8        dp[1] = 1  # 1 way to reach step 1
9        dp[2] = 2  # 2 ways to reach step 2: 1+1 or 2
10        
11        for i in range(3, n + 1):
12            dp[i] = dp[i - 1] + dp[i - 2]
13        
14        return dp[n]