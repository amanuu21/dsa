1from typing import List
2
3class Solution:
4    def findMin(self, nums: List[int]) -> int:
5        left, right = 0, len(nums) - 1
6        
7        while left < right:
8            mid = (left + right) // 2
9            
10            # If middle element is greater than rightmost, 
11            # minimum is in the right half
12            if nums[mid] > nums[right]:
13                left = mid + 1
14            # If middle element is less than rightmost,
15            # minimum is in the left half (including mid)
16            elif nums[mid] < nums[right]:
17                right = mid
18            # If equal, we can't determine which side has minimum,
19            # so reduce search space by moving right pointer left
20            else:
21                right -= 1
22        
23        return nums[left]