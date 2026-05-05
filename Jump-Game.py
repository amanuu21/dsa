1from typing import List
2
3class Solution:
4    def canJump(self, nums: List[int]) -> bool:
5        farthest = 0  # Tracks the farthest index we can reach
6        
7        for i in range(len(nums)):
8            # If current index is beyond our farthest reachable point, we're stuck
9            if i > farthest:
10                return False
11            
12            # Update the farthest index we can reach from current position
13            farthest = max(farthest, i + nums[i])
14            
15            # Early exit: if we can already reach the last index
16            if farthest >= len(nums) - 1:
17                return True
18        
19        return True