1from typing import List
2
3class Solution:
4    def maximumJumps(self, nums: List[int], target: int) -> int:
5        n = len(nums)
6        # dp[i] represents maximum jumps to reach index i from index 0
7        # initialize with -1 (unreachable)
8        dp = [-1] * n
9        dp[0] = 0  # 0 jumps to reach starting position
10        
11        # For each position i, try to come from all previous positions j
12        for i in range(1, n):
13            for j in range(i):
14                # Check if we can jump from j to i
15                diff = nums[i] - nums[j]
16                if -target <= diff <= target and dp[j] != -1:
17                    # We can reach j, so we can reach i with one more jump
18                    dp[i] = max(dp[i], dp[j] + 1)
19        
20        # Return the maximum jumps to reach last index, or -1 if unreachable
21        return dp[n - 1]