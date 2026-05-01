1from typing import List
2
3class Solution:
4    def maxRotateFunction(self, nums: List[int]) -> int:
5        n = len(nums)
6        
7        # Calculate F(0)
8        f0 = 0
9        total_sum = 0
10        for i, num in enumerate(nums):
11            f0 += i * num
12            total_sum += num
13        
14        max_val = f0
15        current = f0
16        
17        # Calculate F(k) from F(k-1)
18        # Formula: F(k) = F(k-1) + total_sum - n * nums[n - k]
19        for k in range(1, n):
20            current = current + total_sum - n * nums[n - k]
21            max_val = max(max_val, current)
22        
23        return max_val