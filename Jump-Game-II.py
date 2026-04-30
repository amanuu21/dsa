1class Solution:
2    def jump(self, nums):
3        n = len(nums)
4        
5        jumps = 0
6        current_end = 0
7        farthest = 0
8        
9        for i in range(n - 1):  # no need to process last index
10            
11            farthest = max(farthest, i + nums[i])
12            
13            # when we reach the end of current range
14            if i == current_end:
15                jumps += 1
16                current_end = farthest
17        
18        return jumps