1class Solution:
2    def permuteUnique(self, nums):
3        nums.sort()  # Step 1: sort to group duplicates
4        result = []
5        used = [False] * len(nums)
6        
7        def backtrack(path):
8            if len(path) == len(nums):
9                result.append(path[:])
10                return
11            
12            for i in range(len(nums)):
13                # Skip already used elements
14                if used[i]:
15                    continue
16                
17                # Skip duplicates
18                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
19                    continue
20                
21                # Choose
22                used[i] = True
23                path.append(nums[i])
24                
25                # Explore
26                backtrack(path)
27                
28                # Undo
29                path.pop()
30                used[i] = False
31        
32        backtrack([])
33        return result