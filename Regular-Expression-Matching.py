1class Solution:
2    def isMatch(self, s, p):
3        m, n = len(s), len(p)
4
5        dp = [[False] * (n + 1) for _ in range(m + 1)]
6        dp[m][n] = True
7
8        for i in range(m, -1, -1):
9            for j in range(n - 1, -1, -1):
10                first_match = i < m and (s[i] == p[j] or p[j] == '.')
11
12                if j + 1 < n and p[j + 1] == '*':
13                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
14                else:
15                    dp[i][j] = first_match and dp[i + 1][j + 1]
16
17        return dp[0][0]