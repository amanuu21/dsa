1class Solution:
2    def threeSum(self, nums):
3        nums.sort()
4        result = []
5        n = len(nums)
6
7        for i in range(n - 2):
8            # Skip duplicate values for i
9            if i > 0 and nums[i] == nums[i - 1]:
10                continue
11
12            left, right = i + 1, n - 1
13
14            while left < right:
15                total = nums[i] + nums[left] + nums[right]
16
17                if total == 0:
18                    result.append([nums[i], nums[left], nums[right]])
19
20                    # Skip duplicates
21                    while left < right and nums[left] == nums[left + 1]:
22                        left += 1
23                    while left < right and nums[right] == nums[right - 1]:
24                        right -= 1
25
26                    left += 1
27                    right -= 1
28
29                elif total < 0:
30                    left += 1
31                else:
32                    right -= 1
33
34        return result