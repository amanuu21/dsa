1from typing import List
2
3class Solution:
4    def firstMissingPositive(self, nums: List[int]) -> int:
5        n = len(nums)
6        
7        # place numbers in correct positions
8        for i in range(n):
9            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
10                correct_idx = nums[i] - 1
11                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
12        
13        # find first missing
14        for i in range(n):
15            if nums[i] != i + 1:
16                return i + 1
17        
18        return n + 1