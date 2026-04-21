1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3        
4        def findFirst(nums, target):
5            left, right = 0, len(nums) - 1
6            first = -1
7            while left <= right:
8                mid = (left + right) // 2
9                if nums[mid] == target:
10                    first = mid
11                    right = mid - 1  # Keep searching left
12                elif nums[mid] < target:
13                    left = mid + 1
14                else:
15                    right = mid - 1
16            return first
17        
18        def findLast(nums, target):
19            left, right = 0, len(nums) - 1
20            last = -1
21            while left <= right:
22                mid = (left + right) // 2
23                if nums[mid] == target:
24                    last = mid
25                    left = mid + 1  # Keep searching right
26                elif nums[mid] < target:
27                    left = mid + 1
28                else:
29                    right = mid - 1
30            return last
31        
32        return [findFirst(nums, target), findLast(nums, target)]