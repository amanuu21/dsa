1class Solution:
2    def threeSumClosest(self, nums, target):
3        nums.sort()
4        n = len(nums)
5        
6        closest_sum = nums[0] + nums[1] + nums[2]
7        
8        for i in range(n - 2):
9            left, right = i + 1, n - 1
10            
11            while left < right:
12                current_sum = nums[i] + nums[left] + nums[right]
13                
14                # Update closest sum
15                if abs(current_sum - target) < abs(closest_sum - target):
16                    closest_sum = current_sum
17                
18                # Move pointers
19                if current_sum < target:
20                    left += 1
21                elif current_sum > target:
22                    right -= 1
23                else:
24                    return current_sum  # exact match
25        
26        return closest_sum