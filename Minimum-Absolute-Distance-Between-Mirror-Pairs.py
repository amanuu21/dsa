1class Solution:
2    def minMirrorPairDistance(self, nums):
3        def reverse(x):
4            return int(str(x)[::-1])
5        
6        seen = {}  # maps reverse(nums[i]) -> latest index i
7        min_dist = float('inf')
8        
9        for j, num in enumerate(nums):
10            # check if current matches reverse of a previous number
11            if num in seen:
12                min_dist = min(min_dist, j - seen[num])
13            
14            # store/update reverse of current number (IMPORTANT: overwrite)
15            seen[reverse(num)] = j
16        
17        return min_dist if min_dist != float('inf') else -1