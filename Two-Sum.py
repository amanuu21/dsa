1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        seen = {}
4
5        for i, num in enumerate(nums):
6            complement = target - num
7
8            if complement in seen:
9                return [seen[complement], i]
10
11            seen[num] = i