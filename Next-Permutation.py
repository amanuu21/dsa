1from typing import List
2
3class Solution:
4    def nextPermutation(self, nums: List[int]) -> None:
5        n = len(nums)
6        
7        # Step 1: find pivot
8        i = n - 2
9        while i >= 0 and nums[i] >= nums[i + 1]:
10            i -= 1
11        
12        # Step 2: if pivot exists, swap
13        if i >= 0:
14            j = n - 1
15            while nums[j] <= nums[i]:
16                j -= 1
17            nums[i], nums[j] = nums[j], nums[i]
18        
19        # Step 3: reverse suffix
20        left, right = i + 1, n - 1
21        while left < right:
22            nums[left], nums[right] = nums[right], nums[left]
23            left += 1
24            right -= 1