1from typing import List
2
3class Solution:
4    def searchInsert(self, nums: List[int], target: int) -> int:
5        left, right = 0, len(nums) - 1
6        
7        while left <= right:
8            mid = (left + right) // 2
9            
10            if nums[mid] == target:
11                return mid
12            elif nums[mid] < target:
13                left = mid + 1
14            else:
15                right = mid - 1
16        
17        return left