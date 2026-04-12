1class Solution:
2    def fourSum(self, nums, target):
3        nums.sort()
4        n = len(nums)
5        res = []
6
7        for i in range(n - 3):
8            # Skip duplicate for i
9            if i > 0 and nums[i] == nums[i - 1]:
10                continue
11
12            for j in range(i + 1, n - 2):
13                # Skip duplicate for j
14                if j > i + 1 and nums[j] == nums[j - 1]:
15                    continue
16
17                left, right = j + 1, n - 1
18
19                while left < right:
20                    total = nums[i] + nums[j] + nums[left] + nums[right]
21
22                    if total == target:
23                        res.append([nums[i], nums[j], nums[left], nums[right]])
24
25                        left += 1
26                        right -= 1
27
28                        # Skip duplicates for left and right
29                        while left < right and nums[left] == nums[left - 1]:
30                            left += 1
31                        while left < right and nums[right] == nums[right + 1]:
32                            right -= 1
33
34                    elif total < target:
35                        left += 1
36                    else:
37                        right -= 1
38
39        return res