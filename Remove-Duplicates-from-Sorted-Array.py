1from typing import List
2
3class Solution:
4    def removeDuplicates(self, nums: List[int]) -> int:
5        if not nums:
6            return 0
7        
8        # Pointer for the position of the next unique element
9        k = 1
10        
11        # Start from the second element
12        for i in range(1, len(nums)):
13            # If current element is different from the previous unique element
14            if nums[i] != nums[k - 1]:
15                nums[k] = nums[i]
16                k += 1
17        
18        return k
19
20
21# Alternative solution using two pointers (more explicit)
22class Solution2:
23    def removeDuplicates(self, nums: List[int]) -> int:
24        if len(nums) <= 1:
25            return len(nums)
26        
27        # i: slow pointer (points to last unique element position)
28        # j: fast pointer (scans through the array)
29        i = 0
30        
31        for j in range(1, len(nums)):
32            if nums[j] != nums[i]:
33                i += 1
34                nums[i] = nums[j]
35        
36        return i + 1
37
38
39# Test the solution
40if __name__ == "__main__":
41    sol = Solution()
42    
43    # Example 1
44    nums1 = [1, 1, 2]
45    k1 = sol.removeDuplicates(nums1)
46    print(f"k = {k1}, nums = {nums1[:k1]}")  # Output: k = 2, nums = [1, 2]
47    
48    # Example 2
49    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
50    k2 = sol.removeDuplicates(nums2)
51    print(f"k = {k2}, nums = {nums2[:k2]}")  # Output: k = 5, nums = [0, 1, 2, 3, 4]
52    
53    # Edge case: empty array
54    nums3 = []
55    k3 = sol.removeDuplicates(nums3)
56    print(f"k = {k3}, nums = {nums3[:k3]}")  # Output: k = 0, nums = []
57    
58    # Edge case: single element
59    nums4 = [5]
60    k4 = sol.removeDuplicates(nums4)
61    print(f"k = {k4}, nums = {nums4[:k4]}")  # Output: k = 1, nums = [5]