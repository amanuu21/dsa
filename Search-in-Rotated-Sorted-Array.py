1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        if not nums:
4            return -1
5        
6        left, right = 0, len(nums) - 1
7        
8        while left <= right:
9            mid = (left + right) // 2
10            
11            # Found the target
12            if nums[mid] == target:
13                return mid
14            
15            # Left half is sorted
16            if nums[left] <= nums[mid]:
17                # Target is in the left sorted half
18                if nums[left] <= target < nums[mid]:
19                    right = mid - 1
20                else:
21                    left = mid + 1
22            
23            # Right half is sorted
24            else:
25                # Target is in the right sorted half
26                if nums[mid] < target <= nums[right]:
27                    left = mid + 1
28                else:
29                    right = mid - 1
30        
31        return -1