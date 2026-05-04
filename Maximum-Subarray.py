1from typing import List
2
3class Solution:
4    def maxSubArray(self, nums: List[int]) -> int:
5        """
6        Returns the sum of the subarray with the largest sum.
7        """
8        if not nums:
9            return 0
10        
11        max_sum = nums[0]      # Initialize with first element
12        current_sum = nums[0]  # Running sum of current subarray
13        
14        for i in range(1, len(nums)):
15            # Either start a new subarray at i, or extend the existing one
16            current_sum = max(nums[i], current_sum + nums[i])
17            # Update the global maximum
18            max_sum = max(max_sum, current_sum)
19        
20        return max_sum